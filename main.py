from PyQt5.QtWidgets import *
import sys


class App(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Analiza'
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 600
        self.target = True

        self.setWindowTitle(self.title)

        self.setFixedSize(self.width, self.height)

        # pole tekstowe
        self.pole = QLineEdit(self)
        self.pole.setGeometry(50, 500, 400, 50)
        self.pole.setText(" ")
        # font
        font = self.pole.font()
        font.setPointSize(30)
        self.pole.setFont(font)

        # guziki
        self.guziki = []
        for i in range(0, 9, 1):
            self.guziki.append(QPushButton(self))
            self.guziki[i].setText(" ")
            self.guziki[i].resize(100, 100)
            self.guziki[i].setGeometry(((i % 3) + 1) * 50 + (i % 3) * 100, (round((i-1)/3) + 1) * 50 + round((i-1)/3) *
                                       100, 100, 100)
        self.guziki[0].clicked.connect(lambda: self.zmiana(0))
        self.guziki[1].clicked.connect(lambda: self.zmiana(1))
        self.guziki[2].clicked.connect(lambda: self.zmiana(2))
        self.guziki[3].clicked.connect(lambda: self.zmiana(3))
        self.guziki[4].clicked.connect(lambda: self.zmiana(4))
        self.guziki[5].clicked.connect(lambda: self.zmiana(5))
        self.guziki[6].clicked.connect(lambda: self.zmiana(6))
        self.guziki[7].clicked.connect(lambda: self.zmiana(7))
        self.guziki[8].clicked.connect(lambda: self.zmiana(8))

        # menu
        menu = self.menuBar()
        game_menu = menu.addMenu("Gra")
        new_game = QAction("Nowa Gra", self)
        new_game.triggered.connect(self.newgame)
        game_menu.addAction(new_game)

        # magic menubar i layouty
        self.show()

    def zmiana(self, j):
        if self.guziki[j].text() == " ":
            if self.target:
                self.guziki[j].setText("O")
                self.target = False
            else:
                self.guziki[j].setText("X")
                self.target = True
            self.sprawdzwygrana()
            self.sprawdzplansze()
        else:
            print("wybierz pole, które nie jest zajęte")

    def sprawdzplansze(self):
        for i in range(0, 9, 1):
            if self.guziki[i].text() == " ":
                return
        self.pole.setText("REMIS")

    def sprawdzwygrana(self):
        for i in range(0, 3):
            if self.guziki[3*i].text() == "X" and self.guziki[3*i + 1].text() == "X" and\
                    self.guziki[3*i + 2].text() == "X":
                self.pole.setText("GRACZ \'X\' WYGRYWA!")
            if self.guziki[i].text() == "X" and self.guziki[i + 3].text() == "X" and self.guziki[i + 6].text() == "X":
                self.pole.setText("GRACZ \'X\' WYGRYWA!")
            if self.guziki[3*i].text() == "O" and self.guziki[3*i + 1].text() == "O" and\
                    self.guziki[3*i + 2].text() == "O":
                self.pole.setText("GRACZ \'O\' WYGRYWA!")
            if self.guziki[i].text() == "O" and self.guziki[i + 3].text() == "O" and self.guziki[i + 6].text() == "O":
                self.pole.setText("GRACZ \'O\' WYGRYWA!")
        if (self.guziki[0].text() and self.guziki[4].text() and self.guziki[8].text()) == "X":
            self.pole.setText("GRACZ \'X\' WYGRYWA!")
        if (self.guziki[2].text() == "X" and self.guziki[4].text() == "X" and self.guziki[6].text()) == "X":
            self.pole.setText("GRACZ \'X\' WYGRYWA!")
        if self.guziki[0].text() == "O" and self.guziki[4].text() == "O" and self.guziki[8].text() == "O":
            self.pole.setText("GRACZ \'O\' WYGRYWA!")
        if (self.guziki[2].text() == "O" and self.guziki[4].text() == "O" and self.guziki[6].text()) == "O":
            self.pole.setText("GRACZ \'O\' WYGRYWA!")
        if self.pole.text() != " ":
            for i in range(0, 9, 1):
                self.guziki[i].blockSignals(True)

    def newgame(self):
        for i in range(0, 9, 1):
            self.guziki[i].setText(" ")
            self.guziki[i].blockSignals(False)
        self.pole.setText(" ")


app = QApplication(sys.argv)
ex = App()
app.exec_()
