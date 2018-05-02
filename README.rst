drf_fields_permissions
======================================

|build-status-image| |pypi-version|

Overview
--------

This package provides a mixin for setting permissions to separate fields of ModelSerializer which uses `DRF permission
classes`_. You can hide or set a field as read-only for specific users.

.. _DRF permission classes: http://www.django-rest-framework.org/api-guide/permissions/

Requirements
------------

-  Python (3.5, 3.6)
-  Django (2.0)
-  Django REST Framework (3.8)

Installation
------------

Install using ``pip``\ …

.. code:: bash

    $ pip install drf_fields_permissions

Example
-------

To show a field only for staff users you need to add ``show_only_to`` field to the ``Meta`` class of a serializer.
``show_only_for`` field must be a ``dict`` with two keys - ``fields`` and ``permission_classes``.
``permission_classes`` is a ``list`` or a ``tuple`` of permission classes. You can use built-in DRF permission or create your
own, but you must override ``has_permission`` method of ``BasePermission`` class.
``fields`` is list or tuple of serializer fields which will be shown only to staff users, in our case.


.. code:: python
   
   from rest_framework import serializers
   from rest_framework import permissions

   from .models import Project

   from fields_permissions.mixins import FieldPermissionMixin


   class ProjectSerializer(FieldPermissionMixin, serializers.ModelSerializer):

       class Meta:
           model = Project
           fields = ('id', 'name', 'status', 'description', 'team_lead_user')

           show_only_for = {
               'fields': ('team_lead_user',),
               'permission_classes': (permissions.IsAdminUser,)
           }
           write_only_for = {
               'fields': ('status', 'description'),
               'permission_classes': (permissions.IsAdminUser,)
           }


Testing
-------

Install testing requirements.

.. code:: bash

    $ pip install -r requirements.txt

Run with runtests.

.. code:: bash

    $ ./runtests.py

You can also use the excellent `tox`_ testing tool to run the tests
against all supported versions of Python and Django. Install tox
globally, and then simply run:

.. code:: bash

    $ tox

.. _tox: http://tox.readthedocs.org/en/latest/

.. |build-status-image| image:: https://travis-ci.org/starnavi-team/drf_fields_permissions.svg?branch=master
   :target: https://travis-ci.org/starnavi-team/drf_fields_permissions?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/drf-fields-permissions.svg
   :target: https://pypi.org/project/drf-fields-permissions
