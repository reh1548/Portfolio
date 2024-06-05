from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.forms import CustomUserCreationForm

# Create your tests here.
# accounts/tests.py



class CustomUserCreationFormTests(TestCase):

    def test_custom_user_creation_form_valid_data(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })

        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')

    def test_custom_user_creation_form_invalid_data(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'first_name': '',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)


class UserViewsTests(TestCase):

    def test_register_user_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })

        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_user_view_invalid_data(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'first_name': '',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })

        self.assertEqual(response.status_code, 200)  # Form should be re-rendered
        self.assertIn('form', response.context)
        self.assertIn('first_name', response.context['form'].errors)
        self.assertFalse(User.objects.filter(username='testuser').exists())
