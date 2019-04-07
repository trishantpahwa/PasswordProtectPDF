'''from database import database
import datetime


date = str(datetime.date.today()).split('-')
date = date[2] + '-' + date[1] + '-' + date[0]
# Initialize database
db = database('books')
# Insert records in database
db.insert_records(['1', 'Trishant', '9717271991', 'Sector 15', 'file1.pdf', 'user_password', 'owner_password', date])
db.insert_records(['2', 'Ajay', '9910055388', 'Old Faridabad', 'file2.pdf' ,'user_password', 'owner_password', date])
db.insert_records(['3', 'Vinay', '9811637191', 'Sector 85', 'file2.pdf', 'user_password', 'owner_password', date])
# Print records from database
records = db.print_records()
for record in records:
    print record
# Updated records in database
db.update_records({'User_Password': 'user_password'}, {'User_Password': 'password_changed'})
# Print records from database
records = db.print_records()
for record in records:
    print record
# Delete records in database
db.delete_records({'CUST_ID': '3'})
# Print records from database
records = db.print_records()
for record in records:
    print record
# Disconnect from server
print('\n\n\nPrinting with clause\n\n\n')
records = db.print_records(['CUST_ID'], {'CUST_ID': 'MAX'})
for record in records:
    print record
db.disconnect_from_server'''
from .database import database