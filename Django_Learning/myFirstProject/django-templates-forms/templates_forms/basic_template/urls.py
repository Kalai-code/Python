from django.urls import path
from . import views

urlpatterns = [
    # For URL: localhost:8000
    path('st_python', views.simple_template_python, name='st_python'),
    path('st_java', views.simple_template_java, name='st_java'),
    path('st_db', views.simple_template_db, name='st_db'),
]

# Testing
# ###################################################################################
# http://localhost:8000/basic_template/st_python
# http://localhost:8000/basic_template/st_java
# http://localhost:8000/basic_template/st_db
