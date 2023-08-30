from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)
    # certificates = models.ManyToManyField('Certificate', related_name='customuser_set', blank=True)
    # educations = models.ManyToManyField('Education', related_name='customuser_set', blank=True)
    # links = models.ManyToManyField('Link', related_name='customuser_set', blank=True)
    # projects = models.ManyToManyField('Project', related_name='customuser_set', blank=True)
    # experiencies = models.ManyToManyField('Experience', related_name='customuser_set', blank=True)

# User's Certificates
class Certificate(models.Model):
    user = models.ForeignKey(CustomUser, related_name='certificate', on_delete=models.SET_NULL, null=True)
    certificate_name = models.CharField(max_length=100, null=True, blank=True)
    issued_by = models.CharField(max_length=100, null=True, blank=True)
    acquisition_date = models.DateField(null=True, blank=True)
    qualification_id = models.CharField(max_length=50, null=True, blank=True)
    certificate_pdf = models.FileField(upload_to='static/pdf/certificates/', null=True, blank=True)
    certificate_link = models.URLField(null=True, blank=True)

# User's Social Media Links
class Link(models.Model):
    user = models.ForeignKey(CustomUser, related_name='link', on_delete=models.SET_NULL, null=True)
    url = models.URLField(null=True, blank=True)
    icon = models.ImageField(upload_to='static/icon/link_icons/', null=True, blank=True)

# User's Experiencies
class Experience(models.Model):
    user = models.ForeignKey(CustomUser, related_name='experience', on_delete=models.SET_NULL, null=True)
    experience_name = models.CharField(max_length=100, null=True, blank=True)
    sub_description = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    experience_image = models.ImageField(upload_to='static/image/experience_images/', null=True, blank=True)

# User's Projects --> Github
class Project(models.Model):
    user = models.ForeignKey(CustomUser, related_name='project', on_delete=models.SET_NULL, null=True)
    project_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project_link = models.URLField(null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    topics = models.JSONField(null=True, blank=True)
    update_date = models.DateField(null=True, blank=True)

# User's Educations
class Education(models.Model):
    user = models.ForeignKey(CustomUser, related_name='education', on_delete=models.SET_NULL, null=True)
    school_name = models.CharField(max_length=100, null=True, blank=True)
    education_type = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    education_image = models.ImageField(upload_to='static/image/education_images/', null=True, blank=True)


'''
# Django shellini başlatın
python manage.py shell

# Örnek kullanıcı oluşturun
user = CustomUser.objects.create(username='example_user', password='example_password')

# Kullanıcıya bağlı sertifikaları oluşturun
certificate1 = Certificate.objects.create(user=user)
certificate2 = Certificate.objects.create(user=user)
# Diğer sertifika bilgilerini de ekleyebilirsiniz.

# Çıkış yapın
exit()
'''