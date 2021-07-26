"""
Version : 0.1.0
Assign admin_order = Integer
Lower Integer will be on TOP and Higher Integer will be on bottom
"""
from django.conf import settings
try:
    from django.urls import resolve, Resolver404
except ModuleNotFoundError:
    # Deprecated since Django 1.10, removed in Django 2.0
    from django.urls.urlresolvers import resolve, Resolver404
from django.core.exceptions import ImproperlyConfigured
from django.urls import resolve, Resolver404


class MiddlewareMixin:

    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class AdminModelListOrder(MiddlewareMixin):

    def get_app_list(self, app_list):
        self.default_priority = getattr(settings, 'ADMIN_MODEL_DEFAULT_PRIORITY', None)
        if not self.default_priority:
            # ADMIN_REORDER settings is not defined.
            raise ImproperlyConfigured('ADMIN_MODEL_DEFAULT_PRIORITY config is not defined.')

        for app in app_list:
            model_order = {}
            for model in app['models']:
                from django.contrib.admin.sites import site
                from django.apps import apps

                model_order[model['object_name']] = getattr(
                    site._registry[apps.get_model(app['app_label'], model['object_name'])],
                    'admin_order',
                    self.default_priority
                )
            app['models'].sort(key=lambda model_: model_order[model_['object_name']])
        return app_list

    def process_template_response(self, request, response):
        try:
            url = resolve(request.path_info)
        except Resolver404:
            return response
        if not url.app_name == 'admin' and \
                url.url_name not in ['index', 'app_list']:
            return response

        try:
            app_list = response.context_data['app_list']
        except KeyError:
            return response

        sorted_app_list = self.get_app_list(app_list)
        response.context_data['app_list'] = sorted_app_list
        return response
