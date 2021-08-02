from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError

from Picturedom.core.validators import validate_profile_image_file_size


class TestProfileImageFileSizeValidator(TestCase):
    def test_profile_image_size_over_limit__raise_error(self):
        image = SimpleUploadedFile(name='test_file.jpg', content=b'', content_type='image/jpeg')
        image.size = 2 * 1024 * 1024
        with self.assertRaises(ValidationError) as context:
            validate_profile_image_file_size(image)
        self.assertIsNotNone(context.exception)

    def test_profile_image_size_equeal_limit_raise_error(self):
        image = SimpleUploadedFile(name='test_file.jpg', content=b'', content_type='image/jpeg')
        image.size = 1024 * 1024
        with self.assertRaises(ValidationError) as context:
            validate_profile_image_file_size(image)
        self.assertIsNotNone(context.exception)

    def test_profile_image_size__success(self):
        image = SimpleUploadedFile(name='test_file.jpg', content=b'', content_type='image/jpeg')
        image.size = 0.5 * 1024 * 1024
