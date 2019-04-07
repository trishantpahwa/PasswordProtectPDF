from encrypt_file import add_password
from decrypt_file import remove_password
from database import database


db = database('books')
cust_id = db.print_records(['CUST_ID'], {'CUST_ID': 'MAX'})[0][0]
file_name = raw_input('Name of file to put password on: ')
pre_encrypted = raw_input('Is file pre-encrypted(Y/N): ')

if pre_encrypted == 'Y' or pre_encrypted == 'y':
    pre_encrypted_password = raw_input('Enter password that file is encrypted with: ')
    remove_password(file_name, pre_encrypted_password)
if pre_encrypted == 'N' or pre_encrypted == 'n':
    user_password = raw_input('Enter user password: ')
    owner_password = raw_input('Enter owner password: ')
    add_password(file_name, user_password, owner_password, cust_id)
else:
    print('Invalid option')
    exit(0)
