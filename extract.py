import pdfplumber as pp

with pp.open("wordlist.pdf") as pdf:
    page_num = len(pdf.pages)
    word_dict = dict()
    for i in range(4,page_num):
        page = pdf.pages[i].extract_text().split("\n")
        print(page[4:len(page)-3])
