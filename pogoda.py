import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from pogodaUI import Ui_MainWindow
import sys
import time

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
            return self.ui.label_info.setText('Введите город Казахстана, например Алматы')
        else:
            search = "Температура в"
            url = "https://www.google.com/search?q={0}".format(content)
            r = requests.get(url)
            s = BeautifulSoup(r.text, "html.parser")
            update = s.find("div", class_="BNeawe").text
            named_tuple = time.localtime()
            time_now = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
            strings = search + " " + update + " (" + time_now + ")"
            return self.ui.label_info.setText(strings)

if __name__ in "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())
