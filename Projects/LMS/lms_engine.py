
"""
def engine(i_masterdata,i_cust_name,i_cust_creditscore,i_cust_loan_amt):
    #Function to check whether the customer is eligible for the loan or not
    eligible = False
    for c in i_masterdata:
        if i_cust_creditscore>= c["cs_start"] and i_cust_creditscore<= c["cs_end"] and i_cust_loan_amt>=c["loan_amt_start"]and i_cust_loan_amt<c["loan_amt_end"]:
           eligible = True
           print(f"\nCongratulations {i_cust_name}!!! You are eligible for the loan")
           print("Duration for payment is:",c["duration"])
           print("Your interest rate will be:",c["interest"])   
           print("The total amount to be paid will be:", i_cust_loan_amt + (i_cust_loan_amt)*(c["interest"])/100)

    if eligible != True:
        print(f"\n Hi {i_cust_name}, your credit score is too less to provide the loan. \n Please improve the credit score and then apply for the loan. \n Thank you")
"""       
# changed the code to write output into a text file      
def engine(i_masterdata,i_cust_name,i_cust_creditscore,i_cust_loan_amt):
    """ Function to check whether the customer is eligible for the loan or not """
    eligible = False
    for c in i_masterdata:
        if i_cust_creditscore>= c["cs_start"] and i_cust_creditscore<= c["cs_end"] and i_cust_loan_amt>=c["loan_amt_start"]and i_cust_loan_amt<c["loan_amt_end"]:
           eligible = True
           eli_duration = c["duration"]
           eli_interest = c["interest"]
           eli_totalamt = i_cust_loan_amt + (i_cust_loan_amt)*(c["interest"])/100
           fileName = "C:\\PythonLearning\\Projects\\LMS\\Text_Files\\"+i_cust_name+".txt"
           file_open = open(fileName,'w')
           file_open.write("\nCongratulations " + i_cust_name+"!!! You are eligible for the loan\n")
           file_open.write("Duration for payment is: " + str(eli_duration) + "\n")
           file_open.write("Your interest rate will be: " + str(eli_interest)+ "\n")
           file_open.write("The total amount to be paid will be: " + str(eli_totalamt) + "\n")
           file_open.close()
    if eligible != True:
        print(f"\n Hi {i_cust_name}, your credit score is too less to provide the loan. \n Please improve the credit score and then apply for the loan. \n Thank you")
        
    