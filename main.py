from datetime import date

from encrypt_file import add_password
from decrypt_file import remove_password
from database import database


db = database('books')
cust_id = str(db.print_records(['CUST_ID'], {'CUST_ID': 'MAX'})[0][0])
if cust_id == 'None':
    cust_id = '1'
date = str(date.today()).split('-')
date = date[2] + '-' + date[1] + '-' + date[0]
file_name = raw_input('Name of file to put password on or remove password from: ')
pre_encrypted = raw_input('Is file pre-encrypted(Y/N): ')

if pre_encrypted == 'Y' or pre_encrypted == 'y':
    pre_encrypted_password = raw_input('Enter password that file is encrypted with: ')
    decrypted_file_name = remove_password(file_name, pre_encrypted_password)
    db.delete_records({'PDF_File_Name': file_name})
    print 'Decrypted file to ' + decrypted_file_name
if pre_encrypted == 'N' or pre_encrypted == 'n':
    name = raw_input('Enter name: ')
    phone_number = raw_input('Enter phone number: ')
    address = raw_input('Enter address: ')
    user_password = raw_input('Enter user password: ')
    owner_password = raw_input('Enter owner password: ')
    encrypted_file_name = add_password(file_name, user_password, owner_password, cust_id)
    db.insert_records([cust_id, name, phone_number, address, encrypted_file_name, user_password, owner_password, date])
    print 'Encrypted file to ' + encrypted_file_name
