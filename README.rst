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

.. code:: python
   
   from rest_framework import serializers

   from fields_permissions.mixins import FieldPermissionMixin

   from .models import Project
   from .permissions import TeamMemberOrHide


   class ProjectSerializer(FieldPermissionMixin, serializers.ModelSerializer):

       class Meta:
           model = Project
           fields = ('id', 'name', 'status', 'description', 'team_lead_user')

           show_only_for = {
               'fields': ('team_lead_user',),
               'permission_classes': (TeamMemberOrHide,)
           }
           write_only_for = {
               'fields': ('status', 'description'),
               'permission_classes': (TeamMemberOrHide,)
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

.. |build-status-image| image:: https://travis-ci.org/starnavi-team/django_rest_fields_permissions?branch=master
   :target: https://travis-ci.org/starnavi-team/django_rest_fields_permissions?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/drf-fields-permissions.svg
   :target: https://pypi.org/project/drf-fields-permissions
