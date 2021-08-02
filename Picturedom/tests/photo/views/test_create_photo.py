import os

from Picturedom import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.core.files import File

from Picturedom.photo.models import Category, Photo


class TestCreatePhotoView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')

    def test_create_photo_GET_not_login(self):
        response = self.client.get(reverse('create photo'))
        redirected_url = response['Location']
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('photos/create_photo.html')
        self.assertEqual(redirected_url, '/login/?next=/photo/create/')

    def test_create_photo_GET_login(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('create photo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/create_photo.html')

    def test_create_photo_POST__success(self):
        self.user = User.objects.create_user('user','email','pass')
        self.client.force_login(self.user)
        category = Category.objects.create(title='category')
        path_to_image = os.path.join(settings.BASE_DIR, "tests/temp/test_image.webp")

        image = File(open(path_to_image, 'rb'))
        data = {
            'image': image,
            'category':category.id,
        }
        response = self.client.post(reverse('create photo'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Photo.objects.count(), 1)
        self.assertEqual(Photo.objects.first().posted_by, self.user)
