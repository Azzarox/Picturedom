# Generated by Django 3.2.6 on 2021-08-07 07:03

import Picturedom.core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, validators=[django.core.validators.MaxLengthValidator(15), django.core.validators.EmailValidator, Picturedom.core.validators.validate_email_ending]),
        ),
    ]