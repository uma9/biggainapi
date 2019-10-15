# Generated by Django 2.2.4 on 2019-09-27 10:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('phone', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='phone number must be enterered ', regex='^\\+?1?\\d{9,14}$')])),
                ('user_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_advartiser', models.BooleanField(default=False)),
                ('is_shopinguser', models.BooleanField(default=False)),
                ('is_subscriber', models.BooleanField(default=False)),
                ('is_vendor', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('first_login', models.BooleanField(default=False)),
                ('date_of_Birth', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='phone number must be enterered ', regex='^\\+?1?\\d{9,14}$')])),
                ('otp', models.CharField(blank=True, max_length=9, null=True)),
                ('count', models.IntegerField(default=0, help_text='number of otps sent')),
                ('validated', models.BooleanField(default=False, help_text='if it is true ,that means user have validate otp correctly in second api')),
            ],
        ),
    ]