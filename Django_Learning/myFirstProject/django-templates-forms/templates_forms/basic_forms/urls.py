from django.urls import path
from . import views

urlpatterns = [
    path('form_post/', views.simple_form, name='simple_form'),
]


# Testing
# ####################################################################
# http://localhost:8000/basic_forms/form_post/
