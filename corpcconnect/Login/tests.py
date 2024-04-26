from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CustomUser

User = get_user_model()

class TestAdminWorkflow(TestCase):
    def setUp(self):
        # Create users
        for i in range(1, 6):
            username = f'user{i}'
            team = f'team{i}'
            role = f'role{i}'
            access_level = i
            CustomUser.objects.create_user(username=username, team=team, role=role, access_level=access_level)

    def test_change_user_activation(self):
        # Log in as Altaf
        self.client.login(username='altaf', password='v123456789')

        # Change is_active to True for 3 random users
        users_to_activate = CustomUser.objects.order_by('?')[:3]
        for user in users_to_activate:
            user.is_active = True
            user.save()

        # Try to log in as one of the activated users
        activated_user = users_to_activate.first()
        self.client.logout()
        response = self.client.post(reverse('login'), {'username': activated_user.username, 'password': 'v123456789'})
        self.assertEqual(response.status_code, 302)  # Redirects to the success URL

    def test_approve_users(self):
        # Log in as Altaf
        self.client.login(username='altaf', password='v123456789')

        # Try to approve the remaining users
        remaining_users = CustomUser.objects.filter(is_active=False)
        for user in remaining_users:
            response = self.client.post(reverse('approve_user', args=[user.pk]))
            self.assertNotEqual(response.status_code, 200)  # Approval should fail

        # Log out
        self.client.logout()

    def test_login_approved_user(self):
        # Log in as an approved user
        approved_user = CustomUser.objects.filter(is_active=True).first()
        self.client.login(username=approved_user.username, password='v123456789')

        # Try to approve another user
        response = self.client.post(reverse('approve_user', args=[approved_user.pk]))
        self.assertNotEqual(response.status_code, 200)  # Approval should fail

        # Log out
        self.client.logout()



