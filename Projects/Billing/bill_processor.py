import json
import os, shutil
import pymysql
import glob
import time, datetime
import zipfile
# File paths
file_path_read = "C:\\PythonLearning\\Projects\\Billing\\Bills\\"
file_path_error = "C:\\PythonLearning\\Projects\\Billing\\Error_bills\\"
file_path_processed = "C:\\PythonLearning\\Projects\\Billing\\Processed_bills\\"
# make changes to database details when needed
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='Billing')
cursor = conn.cursor()
# read the products data from DB and create a list
def getProductData():   
    cursor.execute("select product_id, product_category,product_name, unit_price from products;")

    l_product_lookup =[]
    for l_col1, l_col2, l_col3, l_col4 in cursor.fetchall():
            
        l_data = {"product_id":l_col1,"product_category":l_col2,"product_name":l_col3, "unit_price":l_col4}
        l_product_lookup.append(l_data)
        
    return l_product_lookup

g_product_master = getProductData()

# process bill line details and bill total
def processBillJSON(json_file):
    l_bill_details = []
    l_bill_total = 0
    for product,qty in json_file["BillDetails"].items():
        l_bill_total = l_bill_total + getBillLineTotal(product,qty)[2]
        
        l_bill_details.append({ "BillID":json_file["BillID"]
                               ,"ProductID":int(product)
                               ,"Qty":qty
                               ,"LineTotal":getBillLineTotal(product,qty)[2]})
                               
    l_bill_listTotal = { "BillID": json_file["BillID"]
                   ,"BillDate": json_file["BillDate"]
                   ,"StoreID": json_file["StoreID"]
                   ,"bill_total":l_bill_total }
    return l_bill_listTotal,l_bill_details

# method to calculate bill Line total
def getBillLineTotal(p_product,p_qty):
    for c1 in g_product_master:
        if c1["product_id"]==int(p_product):
            return [c1["product_category"], c1["product_name"], c1["unit_price"]*int(p_qty)]
            
def InsertTotalBillData(l_bill_listTotal):
    d = datetime.datetime.strptime(l_bill_listTotal["BillDate"], "%m/%d/%Y %H:%M:%S")
    date_time_str = d.strftime("%Y-%m-%d %H:%M:%S")
    mysql_insert_query = """INSERT INTO bills(bill_id, bill_date,store_id, bill_total) VALUES(%s, %s, %s, %s)"""
    record = [l_bill_listTotal["BillID"],date_time_str,l_bill_listTotal["StoreID"],l_bill_listTotal["bill_total"]]
    cursor.execute(mysql_insert_query,record)
    conn.commit()

def InsertBillDetailsData(l_bill_details):
    mysql_insert_query = """INSERT INTO billdetails(bill_id, product_id,qty, line_total) VALUES(%s, %s, %s, %s)"""
    for bill_detail in l_bill_details:
        record = [bill_detail["BillID"],bill_detail["ProductID"],bill_detail["Qty"],bill_detail["LineTotal"]]
        cursor.execute(mysql_insert_query,record)
        conn.commit()
def ZipProcessedFiles():
    l_json_files_list = glob.glob(file_path_processed + '*.json')
    zip_filename = datetime.datetime.today().strftime("%Y%m%d%H%M%S") + "_zip.zip"
    zip_filename = file_path_processed + zip_filename
    if l_json_files_list:
        zip_file = zipfile.ZipFile(zip_filename, 'w',zipfile.ZIP_DEFLATED)
        with zip_file:
            for file in l_json_files_list:
                zip_file.write(filename=file, arcname=os.path.basename(file))
                os.remove(file)
while True:
    l_json_files_list = glob.glob(file_path_read + '*.json')
    if l_json_files_list:
        for json_file in l_json_files_list:
            try:
                with open(json_file) as fileObj:
                    jdata = json.load(fileObj)
                    #Funtion to process the files - returns total and details list
                    l_bill_listTotal,l_bill_details =  processBillJSON(jdata)
                    InsertTotalBillData(l_bill_listTotal)
                    InsertBillDetailsData(l_bill_details)
                    fileObj.close()
                    # Post Processing
                    # Move the processed files from Bill to processed folder
                    shutil.move(json_file, file_path_processed)
            except:
                print("Error in files")
                # Move the error files from Bill to error folder
                shutil.move(json_file, file_path_error)
        ZipProcessedFiles()
        time.sleep(10)
        print("Done")
    else:
        break
cursor.close()
    
