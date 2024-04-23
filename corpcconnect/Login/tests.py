from django.test import TestCase, Client
from django.contrib.auth import get_user_model, authenticate, login
from django.urls import reverse
from corpcconnect.models import NewUser, AdminUser
from Login.forms import NewUserRegistrationForm, CustomUserLoginForm
from django.contrib.auth.hashers import make_password

#hrp = ""
def del_user(username):    
    try:
        u = AdminUser.objects.get(username = username)
        u.delete()
        print(username, "'s account is deleted")
        #messages.sucess(request, "The user is deleted")
    except:
        print(username, " doesn't have an account")
      #messages.error(request, "The user not found")
class LoginViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create HR user
        #nonlocal hrp
        del_user("HR")
        hr_user = AdminUser.objects.create_user(username='HR', password="Hr@Pa$$w0rd")
        self.assertTrue(hr_user, "HR user creation failed.")
        print(hr_user)


    def test_register_and_approve_users(self):
        # Check if HR user exists
        hr_user_exists = AdminUser.objects.filter(username='HR').exists()
        self.assertTrue(hr_user_exists, "HR user does not exist. Make sure to create it.")
        #nonlocal hrp
        # Authenticate the HR user
        hr_password = 'Hr@Pa$$w0rd'
        #print(hr_password)
        hr_user = authenticate(username='HR', password=hr_password)
        
        self.assertIsNotNone(hr_user, "HR user authentication failed. Check credentials.")

        self.client.force_login(hr_user)

        # Rest of the test logic to register and approve users
        num_users = 5
        for i in range(num_users):
            user_data = {
                'username': f'user{i}',
                'email': f'user{i}@example.com',
                'password1': f'TestP@ss{i}',  # Example password meeting complexity requirements
                'password2': f'TestP@ss{i}',
                'company': f'Company{i}',
                'position': f'Position{i}'
            }
            response = self.client.post(reverse('register'), data=user_data)
            self.assertEqual(response.status_code, 302)

        # Approve users
        registered_users = NewUser.objects.all()
        num_approved_users = 3
        for user in registered_users[:num_approved_users]:
            approve_response = self.client.get(reverse('approve_user', kwargs={'new_user_id': user.pk}))
            self.assertEqual(approve_response.status_code, 302)

        approved_users = NewUser.objects.filter(is_approved=True)
        self.assertEqual(approved_users.count(), num_approved_users)

        # Test login with approved users
        for user in approved_users:
            login_data = {
                'username': user.username,
                'password': f'TestP@ss{i}',
            }
            # Print login data for debugging
            print("Login Data:", login_data)
            login_response = self.client.post(reverse('login'), data=login_data, follow=True)
            print("Login Response:", login_response)
            self.assertTrue(login_response.context['user'].is_authenticated)

