class LMSEngine:
    """Class to check whether the customer is eligible for the loan or not"""
    
    def __init__(self,i_masterdata,i_cust_name,i_cust_creditscore,i_cust_loan_amt):
        self.i_masterdata = i_masterdata
        self.i_cust_name = i_cust_name
        self.i_cust_creditscore = i_cust_creditscore
        self.i_cust_loan_amt = i_cust_loan_amt
    
    # changed the code to write output into a text file      
    def engine(self):
        """ Function to check whether the customer is eligible for the loan or not """
        eligible = False
        for c in self.i_masterdata:
            if self.i_cust_creditscore>= c["cs_start"] and self.i_cust_creditscore<= c["cs_end"] and self.i_cust_loan_amt>=c["loan_amt_start"]and self.i_cust_loan_amt<c["loan_amt_end"]:
               eligible = True
               eli_duration = c["duration"]
               eli_interest = c["interest"]
               eli_totalamt = self.i_cust_loan_amt + (self.i_cust_loan_amt)*(c["interest"])/100
               fileName = "C:\\PythonLearning\\Projects\\LMS\\Text_Files\\"+self.i_cust_name+".txt"
               file_open = open(fileName,'w')
               file_open.write("\nCongratulations " + self.i_cust_name+"!!! You are eligible for the loan\n")
               file_open.write("Duration for payment is: " + str(eli_duration) + "\n")
               file_open.write("Your interest rate will be: " + str(eli_interest)+ "\n")
               file_open.write("The total amount to be paid will be: " + str(eli_totalamt) + "\n")
               file_open.close()
               print("The details has been sucessfully entered in a text file")
        if eligible != True:
            print(f"\n Hi {self.i_cust_name}, your credit score is too less to provide the loan. \n Please improve the credit score and then apply for the loan. \n Thank you")
        
    