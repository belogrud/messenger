import sys
from PyQt5 import QtWidgets
import qt_design_try

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = qt_design_try.Ui_MainWindow()
ui.setupUi(window)


def hello(word):
    ui.textEdit.append(word)


def get_index():
    print(ui.comboBox.currentIndex())


try:
    class Hello:

        def __init__(self, word):
            self.word = word

        def __call__(self):
            ui.textEdit.append(self.word)


    ui.pushButton.setCheckable(True)
    ui.pushButton.clicked.connect(lambda: hello('Clicked'))
    h = Hello('Class')
    ui.pushButton.clicked.connect(h)
    ui.pushButton.clicked.connect(Hello('Clicked2'))
    ui.pushButton.clicked.connect(Hello('Clicked2'))
    # ui.pushButton.clicked.connect(app.quit)
    ui.pushButton.toggled.connect(lambda: hello('Toggled'))
    ui.pushButton.pressed.connect(lambda: hello('Pressed'))
    ui.pushButton.pressed.connect(lambda: hello('Pressed'))
    ui.pushButton.released.connect(lambda: hello('Release'))
    window.show()
    sys.exit(app.exec_())
except Exception as e:
    print(e)

