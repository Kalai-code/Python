import lms_masterdata
import lms_engine


# Unit Test for one customer
l_CustName="Alex"
l_CustCreditScore=333
l_CustReqLoanAmount=23500

# Function call
lms_engine.engine(lms_masterdata.lms_masterdata,l_CustName,l_CustCreditScore,l_CustReqLoanAmount)

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
 
 # loop through each customer and check if they are eligible for loan or not and return the output
for c1 in customers:
    lms_engine.engine(lms_masterdata.lms_masterdata,c1["CustName"],c1["CustCreditScore"],c1["CustReqLoanAmount"])
    

# Unit Test for Customer who is not eligible for loan

l_CustName="Adam"
l_CustCreditScore=90
l_CustReqLoanAmount=23500

# Function call
lms_engine.engine(lms_masterdata.lms_masterdata,l_CustName,l_CustCreditScore,l_CustReqLoanAmount)

