import lms_masterdataDB
from lms_engine import LMSEngine
import sys, logging
import datetime


"""
# Unit Test for one customer
l_CustName="Ryan"
l_CustCreditScore=333
l_CustReqLoanAmount=23500

lms_engine = LMSEngine(lms_masterdataDB.g_lkp_data,l_CustName,l_CustCreditScore,l_CustReqLoanAmount)
# Function call for one customer
lms_engine.engine()
"""
today = datetime.datetime.today()
l_log_file_name = "logPython_"+today.strftime("%d%b%y%H%M%S")+".log"

# STEP 1. Create a LOGGING Object
tiFileLog = logging.getLogger('LogLMS-file')

# STEP 2. Create a Log File Handler, the log messages will be created in this file
LogFile = logging.FileHandler('C:\\Kalai\\Python\\Projects\\LMS\\Logs\\' +l_log_file_name)

# STEP 3. Add the handler to the logging object
tiFileLog.addHandler(LogFile)

# STEP 4. Set Log Level
tiFileLog.setLevel(logging.INFO)

# Unit Test for few customers who are eligible and not eligible for the loan
customers  = [{ "CustName":"Alan"
  ,"CustCreditScore":200
  ,"CustReqLoanAmount":23500},
 { "CustName":"Ben"
  ,"CustCreditScore":400
  ,"CustReqLoanAmount":23500},
  { "CustName":"David"
  ,"CustCreditScore":400
  ,"CustReqLoanAmount":65000},
{ "CustName":"Flex"
  ,"CustCreditScore":100
  ,"CustReqLoanAmount":23500},
{ "CustName":"Jan"
  ,"CustCreditScore":333
  ,"CustReqLoanAmount":23500}  
  ]

tiFileLog.info("Processing Step: Processing started")
# loop through each customer and check if they are eligible for loan or not and return the output
for c1 in customers:
    lms_engine = LMSEngine(lms_masterdataDB.g_lkp_data,c1["CustName"],c1["CustCreditScore"],c1["CustReqLoanAmount"],tiFileLog)
    lms_engine.engine()
tiFileLog.info("Processing Step: Processing completed")
"""   
# Unit Test for Customer who is not eligible for loan

l_CustName="Adam"
l_CustCreditScore=90
l_CustReqLoanAmount=23500

# Function call for Customer who is not eligible for loan
lms_engine.engine(lms_masterdataDB.g_lkp_data,l_CustName,l_CustCreditScore,l_CustReqLoanAmount)

"""