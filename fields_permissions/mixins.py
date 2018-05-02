import itertools

from rest_framework.permissions import BasePermission


class _permission_field_iterator:
    def __init__(self, fields, permission_classes, request, view):
        self.fields = fields
        self.permission_classes = permission_classes
        self.request = request
        self.view = view

    def __iter__(self):
        self.permission_iter = itertools.product(self.fields, self.permission_classes)
        return self

    def __next__(self):
        field, permission_class = next(self.permission_iter)

        assert issubclass(permission_class, BasePermission), \
            'Permission class should be inherited from "BasePermission"'

        permission_instance = permission_class()

        assert hasattr(permission_class,
                       'has_permission'), 'Permission class "{class_name}" should implement "has_permission" method' \
                                          ' of BasePermission class'.format(
            class_name=permission_instance.__class__.__name__)

        if not permission_instance.has_permission(self.request, self.view):
            return field
        else:
            self.__next__()


class FieldPermissionMixin:

    def _keys_assertions(self, fields, permission_classes, attr_name):
        assert fields is not None, \
            '{attr_name} field should have "fields" key'.format(attr_name=attr_name)

        assert permission_classes is not None, \
            '{attr_name} field should have "permission_classes" key'.format(attr_name=attr_name)

        assert isinstance(fields, list) or isinstance(fields, tuple), \
            'Key "field" of {attr_name} attribute should be list or tuple'.format(attr_name=attr_name)

        assert isinstance(permission_classes, list) or isinstance(permission_classes, tuple), \
            'Key "permission_classes" of {attr_name} attribute should be list or tuple'.format(attr_name=attr_name)

    def _get_permission_attribute(self, attr_name):
            try:
                permission_attribute = getattr(self.Meta, attr_name)
            except AttributeError:
                return {'fields': tuple(), 'permission_classes': tuple()}

            assert isinstance(permission_attribute, dict), \
                '"{attr_name}" attribute should be a dictionary with fields ' \
                'and permission_classes keys'.format(attr_name=attr_name)

            fields = permission_attribute.get('fields')
            permission_classes = permission_attribute.get('permission_classes')

            self._keys_assertions(fields, permission_classes, 'write_only_for')

            return permission_attribute

    def _set_write_only_fields(self, fields, request, view):

        write_only_for = self._get_permission_attribute('write_only_for')

        for write_only_field in _permission_field_iterator(
                write_only_for['fields'], write_only_for['permission_classes'], request, view):
            fields.get(write_only_field).read_only = True

    def _set_now_show_fields(self, fields, request, view):

        show_only_for = self._get_permission_attribute('show_only_for')

        for now_show_fields in _permission_field_iterator(
                show_only_for['fields'], show_only_for['permission_classes'], request, view):
            fields.pop(now_show_fields)

    def get_fields(self):
        fields = super().get_fields()

        request = self.context.get('request')
        view = self.context.get('view')

        self._set_now_show_fields(fields, request, view)
        self._set_write_only_fields(fields, request, view)

        return fields
