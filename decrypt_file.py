from PyPDF2 import PdfFileReader, PdfFileWriter

def remove_password(file_name, password):
    pdfReader = PdfFileReader(file_name)
    pdfWriter = PdfFileWriter()

    if pdfReader.isEncrypted:
        pdfReader.decrypt(password)
    else:
        print('File not encrypted')

    for page in range(0, pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(page))
    
    decrypted_file = file_name.split('_')[0] + 'asdv' + '.pdf'
    print(decrypted_file)
    resultPdf = open(decrypted_file, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
