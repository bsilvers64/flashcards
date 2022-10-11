import pdfplumber as pp


def get_words(book_name):
    word_dict = dict()
    with pp.open(f"D:\pythonpro\\flashcards\\{book_name}") as pdf:
        lim = len(pdf.pages)
        for k in range(lim):
            text = pdf.pages[k].extract_text().split("\n")
            text = text[4:len(text)-3]

            for i in text:
                i = i.split('.')
                if i[0].isnumeric():
                    if i[1].strip().isupper():
                        word_dict[i[1].strip()] = i[2:]

        #print("\n".join("{}\t{}".format(k, v) for k, v in word_dict.items()))
        #print(len(word_dict))
        return word_dict


a = get_words(book_name="wordlist booklet 05.pdf")

words = list(a)
for i in words:
    print(*a[i], sep='; ')