# Generated by Django 4.1.4 on 2022-12-30 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Intake_Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Intake_Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='', max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='uploads/course_image')),
                ('course_intake_month', models.ManyToManyField(to='course.intake_month')),
                ('course_intake_year', models.ManyToManyField(to='course.intake_year')),
                ('course_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course_level')),
                ('course_requirements', models.ManyToManyField(to='course.course_requirement')),
                ('course_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course_status')),
                ('documents_required', models.ManyToManyField(to='course.document')),
            ],
        ),
    ]