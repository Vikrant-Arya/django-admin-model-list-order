=============================
django-admin-model-list-order
=============================


Custom ordering for models in the admin app. You can define your order by ```admin_order``` in ModelAdmin


Install
----------

Install django-modeladmin-reorder:

.. code-block:: bash

    pip install django-admin-modellist-order


Configuration
-------------

1. Add `admin_reorder` to `INSTALLED_APPS`:

   .. code-block:: python

    INSTALLED_APPS = (
        ...
        'admin_reorder',
        ...
    )


2. Add the `ModelAdminReorder` to `MIDDLEWARE_CLASSES`:

   .. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'admin_model_list_order.middleware.AdminModelListOrder',
        ...
    )

3. Add the setting `admin_order` to your admin.py:
   .. code-block:: python

    class YourModelAdmin(admin.ModelAdmin):
        model = YourModel
        admin_order = 1
