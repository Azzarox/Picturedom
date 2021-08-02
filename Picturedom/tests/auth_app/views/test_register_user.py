from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class TestRegisterUserView(TestCase):

    def test_register_user_POST__success(self):
        data = {
            'username': 'john',
            'password1': '1234',
            'password2': '1234',
        }
        # if no context
        response = self.client.post(reverse('register'), data=data)
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Account created successfully.')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('login'))
        self.assertEqual(User.objects.count(), 1)

    def test_register_user_POST__invalid(self):
        data = {
            'username': 'john',
            'password1': '123asd4',
            'password2': '123sd',
        }
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context['form'].errors, {})
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_user_GET__success(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {})
