from PyQt5 import QtWidgets, uic
import sys
import os


# print(os.getcwd())
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('qt_design_try.ui')

print(window.pushButton)
window.show()

def my_f():
    pass
    print('Принт')

window.pushButton.clicked.connect(my_f)

sys.exit(app.exec_())


