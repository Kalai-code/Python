import pymysql

# Create Connection Object
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='LMS')
cursor = conn.cursor()

#Reading multiple datatypes and print to screen
cursor.execute("select cs_start, cs_end, loan_amt_start, loan_amt_end, duration, interest from lms_md_lookup;")


g_lkp_data = []
for l_cs_start, l_cs_end, l_loan_amt_start, l_loan_amt_end, l_duration, l_interest in cursor.fetchall():
    g_lkp_data.append({ "cs_start":l_cs_start
                       ,"cs_end":l_cs_end
                       ,"loan_amt_start":l_loan_amt_start
                       ,"loan_amt_end":l_loan_amt_end
                       ,"duration":l_duration
                       ,"interest":l_interest})
    


# Close the Cursor
cursor.close()

# Close the Connection
conn.close()
