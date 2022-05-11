import pymysql
import csv


# Create Connection Object
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='Billing')
cursor = conn.cursor()

csv_data = csv.reader(open('C:\\Kalai\\Python\\Projects\\Billing\\products.csv'))
next(csv_data)
for row in csv_data:
    print(row)
    cursor.execute('INSERT INTO products(product_id, product_category,product_name, unit_price) VALUES(%s, %s, %s, %s)',row)
#close the connection to the database.
conn.commit()
cursor.close()
print("Done")