from datetime import date

from PyPDF2 import PdfFileReader, PdfFileWriter

file_name = raw_input('Name of file to put password on: ')
pre_encrypted = raw_input('Is file pre-encrypted(Y/N): ')

if pre_encrypted == 'Y' or pre_encrypted == 'y':
    pre_encrypted = True
    pre_encrypted_password = raw_input('Enter password that file is encrypted with: ')
else:
    pre_encrypted = False

user_password = raw_input('Enter user password: ')
owner_password = raw_input('Enter owner password: ')


def add_password(file_name, user_password, owner_password, cust_id):
    pdfReader = PdfFileReader(file_name)
    pdfWriter = PdfFileWriter()

    if pre_encrypted:
        decrypted = pdfReader.decrypt(pre_encrypted_password)
        if not decrypted:
            exit(0)

    for page in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(page))

    pdfWriter.encrypt(user_password, owner_password)

    date_today = str(date.today()).replace('-', '')
    encrypted_file = file_name.replace('.pdf', '') + '_' + cust_id + '_' + date_today + '.pdf'
    print encrypted_file
    resultPdf = open(encrypted_file, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()


add_password(file_name, user_password, owner_password, '0')
