from django.test import TestCase
from django.core.exceptions import ValidationError
from src.core.validators import validate_against_forbidden_words


class TestFobiddenWordsValidator(TestCase):
    def test_OneWordValue_is_forbidden_raise_error(self):
        value = 'suck'
        with self.assertRaises(ValidationError) as context:
            validate_against_forbidden_words(value)
        self.assertIsNotNone(context.exception)

    def test_MultipleWordValue_is_forbidden(self):
        value = 'suck word'
        with self.assertRaises(ValidationError) as context:
            validate_against_forbidden_words(value)
        self.assertIsNotNone(context.exception)

    def test_OneWord_is_valid_success(self):
        value = 'valid'
        validate_against_forbidden_words(value)

    def test_MultipleWord_is_valid_success(self):
        value = 'valid words'
        validate_against_forbidden_words(value)
