from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections, transaction

# Import model from current App
from .model_lookupdata import LmsMdLookup

# Create your views here.
def my_custom_sql():

    #USe LMS DB connection from settings.py
    with connections['LMS'].cursor() as cursor:

        cursor.execute("select cs_start, cs_end, loan_amt_start, loan_amt_end, duration, interest from lms_md_lookup;")
        g_lkp_data = []
        for l_cs_start, l_cs_end, l_loan_amt_start, l_loan_amt_end, l_duration, l_interest in cursor.fetchall():
            g_lkp_data.append({ "cs_start":l_cs_start
                       ,"cs_end":l_cs_end
                       ,"loan_amt_start":l_loan_amt_start
                       ,"loan_amt_end":l_loan_amt_end
                       ,"duration":l_duration
                       ,"interest":l_interest})


    return g_lkp_data

def check_eligibility(request,i_cust_name,i_cust_creditscore,i_cust_loan_amt):
    i_masterdata = my_custom_sql()
    eligible = False    
    for c in i_masterdata:
            if i_cust_creditscore>= c["cs_start"] and i_cust_creditscore<= c["cs_end"] and i_cust_loan_amt>=c["loan_amt_start"]and i_cust_loan_amt<c["loan_amt_end"]:
               eligible = True
               output_text = ""
               eli_duration = c["duration"]
               eli_interest = c["interest"]
               eli_totalamt = i_cust_loan_amt + (i_cust_loan_amt)*(c["interest"])/100
               output_text = "\nCongratulations " + i_cust_name+"!!! You are eligible for the loan\n"
               output_text += "Duration for payment is: " + str(eli_duration) + "\n"
               output_text += "Your interest rate will be: " + str(eli_interest)+ "\n"
               output_text += "The total amount to be paid will be: " + str(eli_totalamt) + "\n"
    if eligible != True:
        output_text = f"\n Hi {i_cust_name}, your credit score is too less to provide the loan. \n Please improve the credit score and then apply for the loan. \n Thank you"
            
    return HttpResponse(output_text)