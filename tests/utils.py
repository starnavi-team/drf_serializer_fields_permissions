from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.test import APITestCase

from my_app.models import Project


class BaseTestingClass(APITestCase):
    def setUp(self):
        password = 'qwerty123'
        self.team_lead = User.objects.create(
            username='team_lead', password=make_password(password), is_superuser=True, is_staff=True
        )
        self.team_member = User.objects.create(
            username='team_member', password=make_password(password), is_staff=True
        )
        self.customer = User.objects.create(
            username='customer', password=make_password(password)
        )
        self.project = Project.objects.create(
            name='Test Project', status=1, description='Project description', team_lead_user=self.team_lead
        )
