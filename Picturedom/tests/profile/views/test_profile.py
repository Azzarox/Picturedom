import os
from django.http import response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files import File
from Picturedom import settings
from Picturedom.profile_user.models import Profile


class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'email', 'pass')
        self.user.save()

    def test_profile_POST___no_image_delete__success(self):
        self.client.force_login(self.user)
        # profile = Profile.objects.create(
        #     user=self.user) -> doesn't work/ doesn't save the data ? and gives UNIQUE constraint failed error
        profile = Profile(user=self.user)
        profile.save()
        path_to_image = os.path.join(
            settings.BASE_DIR, "tests/temp/test_image.webp")
        image = File(open(path_to_image, 'rb'))

        data = {
            'first_name': 'john',
            'last_name': 'scot',
            'age': 20,
            'email': 'email@abv.net',
            'image': image,
            'delete_image': False,
        }
        response = self.client.post(reverse('profile'), data)
        self.assertEqual(response.status_code, 302)
        profile.refresh_from_db()
        self.assertEqual(profile.first_name, 'john')
        self.assertEqual(profile.last_name, 'scot')
        self.assertEqual(profile.age, 20)
        self.assertEqual(profile.email, 'email@abv.net')
        self.assertTrue(bool(profile.image))

    def test_profile_POST__image_delete__success(self):
        path_to_image = os.path.join(
            settings.BASE_DIR, "tests/temp/test_image.webp")
        self.client.force_login(self.user)

        image = File(open(path_to_image, 'rb'))
        profile = Profile(
            user=self.user)
        profile.save()
        data = {
            'age': 20,
            'image': image,
            'delete_image': True,
        }
        response = self.client.post(reverse('profile'), data)
        self.assertEqual(response.status_code, 302)
        profile.refresh_from_db()
        self.assertFalse(bool(profile.image))

    def test_profile_GET__success(self):
        self.client.force_login(self.user)
        profile = Profile(
            user=self.user)
        profile.save()
        profile.user_id = self.user.id
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')
