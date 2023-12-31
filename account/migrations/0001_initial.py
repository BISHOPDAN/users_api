# Generated by Django 3.2.9 on 2022-04-30 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.base.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('verified_email', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsletterSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('reason', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsedResetToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(blank=True, choices=[('logistics', 'Logistics'), ('transportation', 'Transportation')], max_length=30)),
                ('approved', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=60, unique=True, validators=[utils.base.validators.validate_special_char])),
                ('created', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='accounts/profiles')),
                ('address', models.CharField(blank=True, max_length=60)),
                ('city', models.CharField(blank=True, max_length=60)),
                ('state', models.CharField(blank=True, max_length=60)),
                ('zip', models.CharField(blank=True, max_length=6)),
                ('about', models.TextField(blank=True, max_length=2500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
