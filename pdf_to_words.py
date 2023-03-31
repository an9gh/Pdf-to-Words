import PyPDF2


def extractText(pdfname):

    pdfreader = PyPDF2.PdfFileReader(open(pdfname, 'rb'))

    for page in range(pdfreader.numPages):
        pageobj = pdfreader.getPage(page)
        extractObj = pageobj.extract_text()
        return extractObj


words = extractText('twopage.pdf')
print(words)
