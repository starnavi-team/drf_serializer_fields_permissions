from rest_framework.reverse import reverse

from .utils import BaseTestingClass


class ShowOnlyFieldPermissionTest(BaseTestingClass):

    def test_showing_field_for_team_lead(self):
        """
        Check if team_lead user can see 'team_lead_user' user field
        """
        self.client.force_login(user=self.team_lead)
        response = self.client.get(reverse(
            'project-detail', kwargs={'pk': self.project.pk})
        )
        team_lead_user = response.data.get('team_lead_user')
        self.assertIsNotNone(team_lead_user)

    def test_showing_field_for_team_member(self):
        self.client.force_login(user=self.team_member)
        response = self.client.get(reverse(
            'project-detail', kwargs={'pk': self.project.pk})
        )
        team_lead_user = response.data.get('team_lead_user')
        self.assertIsNotNone(team_lead_user)

    def test_showing_field_for_customer(self):
        self.client.force_login(self.customer)
        response = self.client.get(reverse(
            'project-detail', kwargs={'pk': self.project.pk})
        )
        team_lead_user = response.data.get('team_lead_user')
        self.assertIsNone(team_lead_user)
