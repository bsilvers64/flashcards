#! python3

from PyQt5.QtGui import QPalette, QColor
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt
import PyQt5.QtGui as qtg
import pdfplumber as pp
import random



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


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        word_dict, words = dict(), list()

        self.setWindowTitle("Flashcards")
        self.setGeometry(200, 200, 400, 300)
        self.setLayout(qtw.QVBoxLayout())
        #self.setWindowOpacity(0.9)
        self.setWindowIcon(qtg.QIcon('thunder.png'))

        label = qtw.QLabel("Revise Gre words ⚡⚡")
        label_2 = qtw.QLabel()
        label.setFont(qtg.QFont('Montserrat', 18))
        self.layout().addWidget(label)
        self.layout().addWidget(label_2)

        option_1_btn = qtw.QPushButton("Wordlist-1",
                                       clicked = lambda: book_select("wordlist booklet 01.pdf"))
        option_2_btn = qtw.QPushButton("Wordlist-2",
                                       clicked = lambda: book_select("wordlist booklet 02.pdf"))
        option_3_btn = qtw.QPushButton("Wordlist-3",
                                       clicked = lambda: book_select("wordlist booklet 03.pdf"))
        option_4_btn = qtw.QPushButton("Wordlist-4",
                                       clicked = lambda: book_select("wordlist booklet 04.pdf"))
        option_5_btn = qtw.QPushButton("Wordlist-5",
                                       clicked = lambda: book_select("wordlist booklet 05.pdf"))

        self.layout().addWidget(option_1_btn)
        self.layout().addWidget(option_2_btn)
        self.layout().addWidget(option_3_btn)
        self.layout().addWidget(option_4_btn)
        self.layout().addWidget(option_5_btn)

        def book_select(book_name):
            global word_dict, words, x
            word_dict = get_words(book_name=book_name)
            option_1_btn.hide()
            option_2_btn.hide()
            option_3_btn.hide()
            option_4_btn.hide()
            option_5_btn.hide()
            words = list(word_dict)
            self.layout().addWidget(btn)


        btn = qtw.QPushButton("Random", clicked = lambda: pressed())
        btn.resize(100,40)
        count = 0
        def pressed():
            global words, word_dict
            pressed.counter += 1
            word = random.choice(words)
            label.setText(f" {pressed.counter}.  {word}\n\n")
            label_2.setText(f"{''.join(word_dict[word])}")
            label.setFont(qtg.QFont('Montserrat', 18))
            label_2.setStyleSheet("background-color: #091217")
            label_2.setFont(qtg.QFont('Montserrat', 16))
        pressed.counter = 0


        self.show()


app = qtw.QApplication([])

# Force the style to be the same on all OSs:
app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(32,36,36))
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