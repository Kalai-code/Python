from django.urls import path
from . import views

urlpatterns = [
    # For URL: localhost:8000
    path('st_python', views.simple_template_python, name='st_python'),
    path('st_java', views.simple_template_java, name='st_java'),
]