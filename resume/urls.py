from django.urls import path
from . import views
from .views import custom_404

urlpatterns = [
    path('', views.resume, name='resume'),
    path('certificate/add', views.certificateAdd, name='certificate'),
    path('education/add', views.educationAdd, name='education'),
    path('experience/add', views.experienceAdd, name='experience'),
    path('contact/add', views.contactAdd, name='contact'),
    path('project/add', views.projectAdd, name='project'),
    path('delete/<str:object_type>/<int:object_id>', views.delete, name='delete')
]

handler404 = custom_404