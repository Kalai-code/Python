from django.urls import path
from . import views

urlpatterns = [
    # For URL: localhost:8000
    path('ti_caller_borders', views.caller_borders),
    path('ti_caller_table', views.caller_table),
    # path('ti_caller_accordian', views.caller_accordian),
]



# Testing
# ####################################################################
# http://localhost:8000/template_inheritance/ti_caller_borders
# http://localhost:8000/template_inheritance/ti_caller_table
# ##http://localhost:8000/template_inheritance/ti_caller_accordian##
