from src.core.validators import validate_bot_field
from django.test import TestCase
from django.core.exceptions import ValidationError


class TestBotCatcherValidator(TestCase):
    def test_bot_caught__raise(self):
        value = 'string'
        with self.assertRaises(ValidationError) as context:
            validate_bot_field(value)
        self.assertEquals(context.exception.args[0], 'Bot has been detected!')

    def test_bot_caught__success(self):
        value = ''
        validate_bot_field(value)