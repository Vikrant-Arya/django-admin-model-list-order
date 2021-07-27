django-admin-model-list-order
=============================


Custom ordering for models in the admin app. You can define your order by ```admin_order``` in ModelAdmin


Install
----------

Install django-admin-model-list-order:

.. code-block:: bash

    pip install django-admin-model-list-order


Configuration
-------------

1. Add `admin_model_list_order` to `INSTALLED_APPS`:

.. code-block:: bash

    INSTALLED_APPS = (
        ...
        'admin_model_list_order',
        ...
    )


2. Add the `AdminModelListOrder` to `MIDDLEWARE_CLASSES`:

.. code-block:: bash

    MIDDLEWARE_CLASSES = (
        ...
        'admin_model_list_order.middleware.AdminModelListOrder',
        ...
    )

3. Add the setting ```ADMIN_MODEL_DEFAULT_PRIORITY``` to your settings.py, It will add default priority 100 to modelAdmin:

.. code-block:: bash

    ADMIN_MODEL_DEFAULT_PRIORITY = 100

4. Add the setting `admin_order` to your admin.py:

.. code-block:: bash

    class YourModelAdmin(admin.ModelAdmin):
        model = YourModel
        admin_order = 1


Example
-------

.. code-block:: bash

    class Model1(admin.ModelAdmin):
        model = Model 1
        admin_order = 1

    .. code-block:: bash

    class Model2(admin.ModelAdmin):
        model = Model 2
        admin_order = 2

It will come in app in this order
```Model 1```
```Model 2```