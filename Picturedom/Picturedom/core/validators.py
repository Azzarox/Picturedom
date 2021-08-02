from django.core.exceptions import ValidationError


def validate_against_forbidden_words(value):
    words = set(value.split())
    forbidden_words = ['fuck', 'suck', 'bitch', ]
    if words.intersection(forbidden_words):
        raise ValidationError('You have used a forbidden word!')


def validate_profile_age(value):
    if value >= 100:
        raise ValidationError('Please enter age lower than 100')


def validate_profile_names_are_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Please enter only letters')


def validate_email_ending(value):
    valid_endings = ['bg', 'com', 'edu', 'net', 'org']
    value_ending = value.split('.')[1]
    if value_ending not in valid_endings:
        raise ValidationError(
            'Please enter email that doesn\'t contain dot(.) except for the ending or one that ends with .bg .com .edu .net or .org')


def validate_profile_image_file_size(value):
    mb_limit = 1024 * 1024
    if value and value.size >= mb_limit:
        raise ValidationError('Image file size is over 1 MB. Please resize the image or upload another.')


def validate_image_file_size(value):
    mb_limit = 8 * 1024 * 1024
    if value and value.size >= mb_limit:
        raise ValidationError('Image file size is over 8 MB. Please resize the image or upload another.')
