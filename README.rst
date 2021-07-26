django-admin-model-list-order
=============================


Custom ordering for models in the admin app. You can define your order by ```admin_order``` in ModelAdmin


Install
----------

Install django-admin-modellist-order:



    pip install django-admin-modellist-order


Configuration
-------------

1. Add `admin_model_list_order` to `INSTALLED_APPS`:



    INSTALLED_APPS = (
        ...
        'admin_model_list_order',
        ...
    )


2. Add the `ModelAdminReorder` to `MIDDLEWARE_CLASSES`:



    MIDDLEWARE_CLASSES = (
        ...
        'admin_model_list_order.middleware.AdminModelListOrder',
        ...
    )

3. Add the setting `admin_order` to your admin.py:



    class YourModelAdmin(admin.ModelAdmin):
        model = YourModel
        admin_order = 1
