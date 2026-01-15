from django.test import TestCase
from django.core.exceptions import ValidationError

from src.core.validators import validate_profile_age


class TestProfileAgeValidator(TestCase):

    def test_profile_age_is_over_limit_should_raise(self):
        value = 101
        with self.assertRaises(ValidationError) as context:
            validate_profile_age(value)
        self.assertIsNotNone(context.exception)

    def test_profile_age_is_equal_to_limit_should_raise(self):
        value = 100
        with self.assertRaises(ValidationError) as context:
            validate_profile_age(value)
        self.assertIsNotNone(context.exception)

    def test_profile_age_is_valid(self):
        value = 99
        validate_profile_age(value)

    def test_profile_age_is_zero_should_valid(self):
        value = 0
        validate_profile_age(value)
