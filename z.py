from PyQt5.QtGui import QPalette, QColor
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
import PyQt5.QtGui as qtg
import pdfplumber as pp
import random
import json
from PyDictionary import PyDictionary

dictionary=PyDictionary()

def get_words(book_name):
    word_dict = dict()
    with pp.open(book_name) as pdf:
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


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        word_dict, words = dict(), list()

        self.setWindowTitle("Flashcards")
        self.setGeometry(200, 200, 400, 300)
        self.setLayout(qtw.QVBoxLayout())
        self.setWindowOpacity(0.9)
        self.setWindowIcon(qtg.QIcon('thunder.png'))

        label = qtw.QLabel("Revise Gre words ⚡⚡")
        label.setFont(qtg.QFont('Montserrat', 18))
        self.layout().addWidget(label)

        option_1_btn = qtw.QPushButton("Wordlist-3",
                                       clicked = lambda: book_select("wordlist.pdf"))
        option_2_btn = qtw.QPushButton("Wordlist-4",
                                       clicked = lambda: book_select("wordlist_2.pdf"))


        self.layout().addWidget(option_1_btn)
        self.layout().addWidget(option_2_btn)

        def book_select(book_name):
            global word_dict, words, x
            word_dict = get_words(book_name=book_name)
            option_1_btn.hide()
            option_2_btn.hide()
            words = list(word_dict)
            self.layout().addWidget(btn)


        btn = qtw.QPushButton("Random", clicked = lambda: pressed())
        btn.resize(100,40)

        def pressed():
            global words, word_dict
            word = random.choice(words)
            label.setText(f" {word}\n\n\n{''.join(word_dict[word])}"
                          f"\n\n\n{json.dumps(dictionary.meaning(word.split()[0]), indent=4)}")
            label.setFont(qtg.QFont('Montserrat', 18))



        self.show()


app = qtw.QApplication([])

# Force the style to be the same on all OSs:
app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)


mw = MainWindow()

app.exec_()