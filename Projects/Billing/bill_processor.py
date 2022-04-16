import product_details
import json
import os, shutil

# File paths
file_path_read = "C:\\Kalai\\Python\\Projects\\Billing\\Bills\\"
file_path_error = "C:\\Kalai\\Python\\Projects\\Billing\\Error_bills\\"
file_path_processed = "C:\\Kalai\\Python\\Projects\\Billing\\Processed_bills\\"
file_path_archive = "C:\\Kalai\\Python\\Projects\\Billing\\Archive\\"
#Change the directory
os.chdir(file_path_read)

def read_files():
    for file in os.listdir():
        print("File Name:", file)
        if file.endswith(".json"):
            path = f"{file_path_read}{file}"
            new_file = open(path, "r")
            var_text = json.loads(new_file.read())
            new_file.close()
            #Funtion to process the files
            Bill_Details(var_text,file)
            

def Bill_Details(json_file,fileName): 
    prodIDlist = list_prodID()
    billID = json_file["BillID"]
    billDetail_json = {"BillID": billID}
    billTotal_json = {"BillID": billID}
    billTotal_json["BillDate"] = json_file["BillDate"]
    billTotal_json["StoreID"] = json_file["StoreID"]
    filepath = file_path_processed+billID
    bill_list = process_files(json_file["BillDetails"],prodIDlist,fileName,billTotal_json)    
    if bill_list:
        billDetail_json["Items"] = bill_list  
        # Functions to write the processed files
        write_Detailprocessedfile(filepath+"_billDetails.json",billDetail_json)
        write_totalprocessedfile(filepath+"_billTotal.json",billTotal_json)
        move_toArchiveFolder(file_path_read+fileName,file_path_archive+fileName)
    
def get_LineTotal(unitPrice,value):
    return unitPrice * value
    
def list_prodID():
    list_prodID = []
    for prod in product_details.billing_masterData:
        list_prodID.append(prod["prodid"])
    return list_prodID
    
def process_files(billDetails,prodIDlist,fileName,billTotal_json):
    Totalamount = 0
    billDetail_linetotal = {}
    billDetail_list=[]
    for key,value in billDetails.items():
        if key in prodIDlist:
            for prod in product_details.billing_masterData:
                if prod["prodid"] == key:
                    billDetail_linetotal["ProductID"] = key
                    billDetail_linetotal["Quantity"] = value
                    lineTotal = get_LineTotal(prod["unitPrice"],value)
                    billDetail_linetotal["LineTotal"] = lineTotal
                    billDetail_list.append(billDetail_linetotal)
                    billDetail_linetotal={}
                    Totalamount = Totalamount + lineTotal
                    break
            billTotal_json["bill_total"] = Totalamount
        else:
            #Move the error files to the Error folder and return empty list
            move_toErrorFolder(file_path_read+fileName,file_path_error+fileName)
            return []
            
    return billDetail_list

def write_Detailprocessedfile(filepath,jsonfile):
    new_file = open(filepath, "w")
    new_file.write(json.dumps(jsonfile))
    new_file.close()   

def write_totalprocessedfile(filepath,jsonfile):
    new_file = open(filepath, "w")
    new_file.write(json.dumps(jsonfile))
    new_file.close()
    
def move_toArchiveFolder(srcfile,destfile):
    shutil.move(srcfile,destfile)
    
def move_toErrorFolder(srcfile,destfile):
    shutil.move(srcfile,destfile)
    

