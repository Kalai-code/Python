from django.urls import path
from . import views

urlpatterns = [
    path('check_eligibility/<str:i_cust_name>/<int:i_cust_creditscore>/<int:i_cust_loan_amt>',views.check_eligibility, name = 'check_eligibility'),
    ]