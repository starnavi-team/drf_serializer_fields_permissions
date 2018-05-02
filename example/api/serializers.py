from rest_framework import serializers

from .models import Project
from .permissions import TeamMemberOrHide

from fields_permissions.mixins import FieldPermissionMixin


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
