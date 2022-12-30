from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from course.models import Course

# Create your models here.

class University(models.Model):
    univ_name = models.CharField(max_length=100,verbose_name="University Name",default="")
    country = models.CharField(max_length=100,default="",verbose_name="Select Country")
    univ_desc = models.TextField(max_length=1000,verbose_name="University Description", default="",)
    univ_logo = models.ImageField(upload_to='uploads/uni_logoimages', default="", blank=True)
    select_default_assign_employee = models.ForeignKey('auth.user', on_delete=models.CASCADE,verbose_name="Select Default Assign employee", default="")
    univ_address = models.CharField(max_length=200, null=True, default='',verbose_name="University Address")
    univ_phone = PhoneNumberField(null=True, default='', verbose_name="University Phone")
    univ_email = models.EmailField(null=True, default='', verbose_name="University Email")
    univ_web = models.CharField(max_length=50, null=True, default='', verbose_name="University Web")
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.univ_name





    # course = models.ManyToManyField(Course)
    # class  Paperbased_Form_Required (models.TextChoices):
    #        Yes = 'YES', ('YES')
    #        No = 'NO', ('NO')
    # paperbased_form_required = models.CharField(verbose_name='Is Paperbsed Form Required?', max_length=10,choices=Paperbased_Form_Required.choices,default="")


