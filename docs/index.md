![PyPI Version](https://img.shields.io/pypi/v/drf-fields-permissions.svg)

---
# drf_fields_permissions

---

## Overview
This package provides a mixin for setting permissions to separate fields of ModelSerializer which uses [DRF permission classes](http://www.django-rest-framework.org/api-guide/permissions/). You can hide or set a field as read-only for specific users.

## Requirements

* Python (3.10, 3.11)
* Django (4.0, 4.1, 4.2)
* Django REST Framework (3.13, 3.14)

## Installation

Install using `pip`...

```bash
$ pip install django_rest_fields_permissions
```

## Example

To show a field only for staff users, you need to add `show_only_to` field to the `Meta` class of a serializer. `show_only_for` field must be a `dict` with two keys - `fields` and `permission_classes`. `permission_classes` is a `list` or a `tuple` of permission classes. You can use built-in DRF permission or create your own, but you must override `has_permission` method of `BasePermission` class. `fields` is a list or tuple of serializer fields which will be shown only to staff users, in our case.


```python
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
```

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```
