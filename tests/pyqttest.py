from PyQt5 import QtWidgets, uic


file = 'select_baze.ui'

app = QtWidgets.QApplication([])

# Загрузка UI файла
window = uic.loadUi(file)
# Подключение обработчика кнопки
window.pushButton.clicked.connect(lambda: window.label.setText(window.lineEdit.text()))
window.show()
app.exec_()