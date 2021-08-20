# by https://wttr.in/:help?lang=ru

import sys

import requests
from PyQt5 import QtWidgets

from list_weather import list_city
from pogodaUI import Ui_MainWindow


class Pogoda(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pogoda, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(list_city)
        self.ui.comboBox.activated.connect(self.get_weather)

    def get_weather(self):
        weather_parameters = {
            '0': '',
            'T': ''
            }

        request_headers = {
            'Accept-Language': 'ru'
        }
        return self.ui.text_out.setText(
            requests.get(
                f'https://wttr.in/{self.ui.comboBox.currentText()}',
                params=weather_parameters,
                headers=request_headers).text)


if __name__ in "__main__":
    app = QtWidgets.QApplication([])
    application = Pogoda()
    application.show()
    sys.exit(app.exec())
