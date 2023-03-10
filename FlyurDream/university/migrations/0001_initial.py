# Generated by Django 4.1.4 on 2022-12-30 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('univ_name', models.CharField(default='', max_length=100, verbose_name='University Name')),
                ('country', models.CharField(default='', max_length=100, verbose_name='Select Country')),
                ('univ_desc', models.TextField(default='', max_length=1000, verbose_name='University Description')),
                ('univ_logo', models.ImageField(blank=True, default='', upload_to='uploads/uni_logoimages')),
                ('univ_address', models.CharField(default='', max_length=200, null=True, verbose_name='University Address')),
                ('univ_phone', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, null=True, region=None, verbose_name='University Phone')),
                ('univ_email', models.EmailField(default='', max_length=254, null=True, verbose_name='University Email')),
                ('univ_web', models.CharField(default='', max_length=50, null=True, verbose_name='University Web')),
                ('select_default_assign_employee', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Select Default Assign employee')),
            ],
        ),
    ]
