from datetime import date
from PyPDF2 import PdfFileReader, PdfFileWriter

def add_password(file_name, user_password, owner_password, cust_id):
    pdfReader = PdfFileReader(file_name)
    pdfWriter = PdfFileWriter()

    for page in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(page))

    pdfWriter.encrypt(user_password, owner_password)

    date_today = str(date.today()).replace('-', '')
    encrypted_file = file_name.replace('.pdf', '') + '_' + cust_id + '_' + date_today + '.pdf'
    resultPdf = open(encrypted_file, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
