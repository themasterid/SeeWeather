import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from pogodaUI import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItems(
            [
                "Оренбург",
                "Москва",
                "Алматы",
                "Лондон",
                "Бишкек"
            ]
        )
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox.activated.connect(self.action)

    def action(self):
        content = self.ui.comboBox.currentText()
        search = "Температура в " + content
        url = "https://www.google.com/search?q={0}".format(search)
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")
        update = s.find("div", class_="BNeawe").text
        strings = search + " " + update
        self.ui.label.setText(strings)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
