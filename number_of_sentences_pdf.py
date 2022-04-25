# from PyPDF2 import PdfFileReader

import PyPDF2


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information


if __name__ == '__main__':
    #   '/home/muhammed/Downloads/pcm_a4.pdf'
    # from PyPDF2 import PdfFileReader

    # reader = PdfFileReader("/home/muhammed/Downloads/pcm_a4.pdf")
    # number_of_pages = reader.numPages
    # page = reader.pages[100]
    # text = page.extractText()
    # print(type(text))

    pdfFileObj = open("/home/muhammed/Downloads/pcm_a4.pdf", "rb")
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(100)

    # extracting text from page
    print(pageObj.extractText())

    # closing the pdf file object
    pdfFileObj.close()
