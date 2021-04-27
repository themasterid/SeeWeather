# by https://wttr.in/:help?lang=ru

import requests
from PyQt5 import QtWidgets
from pogodaUI import Ui_MainWindow
import sys


weather_parameters = {
    '0': '',
    'T': ''
    }

request_headers = {
    'Accept-Language': 'ru'
}


listkz = ['Алматы', 'Нур-Султан', 'Астана', 'Шымкент', 'Актобе', 'Караганда', 'Тараз', 'Павлодар', 'Усть-Каменогорск', 'Семей',
          'Атырау', 'Костанай', 'Кызылорда', 'Уральск', 'Петропавловск', 'Актау', 'Темиртау', 'Туркестан',
          'Талдыкорган', 'Кокшетау', 'Экибастуз', 'Рудный', 'Жезказган', 'Жанаозен', 'Балхаш', 'Кентау', 'Каскелен',
          'Сатпаев', 'Кульсары', 'Риддер', 'Щучинск', 'Степногорск', 'Капшагай', 'Арыс', 'Сарань', 'Талгар', 'Жаркент',
          'Аксу', 'Байконур', 'Байконыр', 'Аягоз', 'Шахтинск', 'Шу', 'Алтай', 'Лисаковск', 'Кандыагаш', 'Аксай',
          'Житикара', 'Аральск', 'Есик', 'Сарыагаш', 'Текели', 'Каратау', 'Атбасар', 'Шардара', 'Абай', 'Аркалык',
          'Шалкар', 'Хромтау', 'Ленгер', 'Жетысай', 'Уштобе', 'Жанатас', 'Алга', 'Шемонаиха', 'Макинск', 'Ушарал',
          'Зайсан', 'Акколь', 'Приозёрск', 'Курчатов', 'Эмба', 'Тайынша', 'Сарканд', 'Есиль', 'Ерейментау',
          'Серебрянск', 'Каркаралинск', 'Каражал', 'Булаево', 'Сергеевка', 'Мамлютка', 'Шар', 'Форт-Шевченко',
          'Державинск', 'Казалинск', 'Степняк', 'Темир', 'Жем']


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.action)

    def action(self):
        content = self.ui.lineEdit_city.text()
        if content not in listkz:
            return self.ui.text_out.setText('Введите город Казахстана, например Алматы')
        else:
            url = f'https://wttr.in/{content}'
            return self.ui.text_out.setText(requests.get(url,
                                                            params=weather_parameters,
                                                            headers=request_headers).text)

if __name__ in "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())
