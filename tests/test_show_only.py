from rest_framework import status
from rest_framework.reverse import reverse

from .utils import BaseTestingClass
from api.models import Project


class WriteOnlyFieldPermissionTest(BaseTestingClass):

    def test_edit_status_field_for_team_lead(self):
        self.client.force_login(user=self.team_lead)
        response = self.client.patch(reverse(
            'project-detail',
            kwargs={'pk': self.project.pk}),
            data={'status': 2}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=1)
        self.assertEqual(project.status, 2)

    def test_edit_status_field_for_team_member(self):
        self.client.force_login(user=self.team_member)
        response = self.client.patch(reverse(
            'project-detail',
            kwargs={'pk': self.project.pk}),
            data={'status': 2}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=1)
        self.assertEqual(project.status, 2)

    def test_edit_status_field_for_customer(self):
        self.client.force_login(user=self.customer)
        response = self.client.patch(reverse(
            'project-detail',
            kwargs={'pk': self.project.pk}),
            data={'status': 2}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=1)
        # But the field was not changed
        self.assertEqual(project.status, 1)
