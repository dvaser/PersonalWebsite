from django.contrib import admin
from .models import CustomUser, Certificate, Experience, Link, Project


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Certificate)
admin.site.register(Experience)
admin.site.register(Link)
admin.site.register(Project)