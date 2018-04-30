from rest_framework import viewsets
from rest_framework import permissions

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
