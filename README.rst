django_rest_fields_permissions
======================================

|build-status-image| |pypi-version|

Overview
--------

Permissions for django-rest fields

Requirements
------------

-  Python (3.5, 3.6)
-  Django (2.0)
-  Django REST Framework (3.8)

Installation
------------

Install using ``pip``\ …

.. code:: bash

    $ pip install django_rest_fields_permissions

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

           not_show_field_to = {
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

.. |build-status-image| image:: https://travis-ci.org/starnavi-team/django_rest_fields_permissions.svg?branch=master
   :target: https://travis-ci.org/starnavi-team/django_rest_fields_permissions?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/django_rest_fields_permissions.svg
   :target: https://pypi.python.org/pypi/django_rest_fields_permissions
