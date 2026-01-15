from django.test import TestCase
from django.core.exceptions import ValidationError
from src.core.validators import validate_profile_names_are_only_letters


class TestProfileNamesValidator(TestCase):

    def test_profile_name__with_numbers__raise_error(self):
        value = 'name123'
        with self.assertRaises(ValidationError) as context:
            validate_profile_names_are_only_letters(value)
        self.assertIsNotNone(context.exception)

    def test_profile_name__with_whitespace__raise_error(self):
        value = 'invalid word'
        with self.assertRaises(ValidationError) as context:
            validate_profile_names_are_only_letters(value)
        self.assertIsNotNone(context.exception)

    def test_profile_name__with_characters__raise_error(self):
        value = 'Name.with.characters'
        with self.assertRaises(ValidationError) as context:
            validate_profile_names_are_only_letters(value)
        self.assertIsNotNone(context.exception)

    def test_profile_name_valid_success(self):
        value = 'Name'
        validate_profile_names_are_only_letters(value)
