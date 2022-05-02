import lms_masterdata
from lms_engine import LMSEngine
import sys



# Unit Test for one customer
l_CustName="Ryan"
l_CustCreditScore=333
l_CustReqLoanAmount=23500

lms_engine = LMSEngine(lms_masterdata.lms_masterdata,l_CustName,l_CustCreditScore,l_CustReqLoanAmount)
# Function call for one customer
lms_engine.engine()


