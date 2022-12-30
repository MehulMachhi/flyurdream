from django.db import models

# from university.models import University

class Course_Requirement(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.name

class Intake_Year(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.name

class Course_Level(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.name


class Course_Status(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.name

class Intake_Month(models.Model):
    name = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.name

# Create your models here.

class Course(models.Model):
    country = models.CharField(max_length=100, default="")
    # university = models.ForeignKey('university.University', on_delete=models.CASCADE, null=True)
    course_level = models.ForeignKey('Course_Level', on_delete=models.CASCADE, null=True)
    course_name = models.CharField(max_length=100)
    course_image = models.ImageField(upload_to="uploads/course_image", null=True, blank=True)
    course_intake_month = models.ManyToManyField('Intake_Month')
    course_intake_year = models.ManyToManyField('Intake_Year')
    documents_required = models.ManyToManyField('Document')
    course_requirements = models.ManyToManyField('Course_Requirement')

    class course_status(models.TextChoices):
        active = 'active', ('active')
        in_active = 'in_active', ('in_active')

    course_status = models.ForeignKey('Course_Status', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.course_name


