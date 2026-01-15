from types import CodeType
from django.test import TestCase
from django.core.exceptions import ValidationError

from src.core.validators import validate_email_ending


class TestEmailEndingValidator(TestCase):
    def test_invalid_email_ending__raise_error(self):
        value = 'email@with.bad_ending'
        with self.assertRaises(ValidationError) as context:
            validate_email_ending(value)
        self.assertIsNotNone(context.exception)

    def test_invalid_email__with_dot__and_invalid_ending__raise_error(self):
        value = 'em.ail@with.bad_ending'
        with self.assertRaises(ValidationError) as context:
            validate_email_ending(value)
        self.assertIsNotNone(context.exception)

    def test_invalid_email__with_dot__and_valid_ending__raise_error(self):
        value = 'em.ail@with.com'
        with self.assertRaises(ValidationError) as context:
            validate_email_ending(value)
        self.assertIsNotNone(context.exception)

    def test_valid_email_ending__success(self):
        value = 'valid@email.com'
        validate_email_ending(value)

