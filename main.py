from PyQt5 import QtWidgets
from form import Ui_MainWindow  # assuming form.py is in the same directory
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):



    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Epub file meta")
        self.actionQuit.triggered.connect(self.close)
        self.actionOpen.triggered.connect(self.open)
        self.filename = None
        self.open()

    def open(self):
        self.hide()
        self.filename, selectedfilter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', filter="EPUB Files (*.epub)")
        self.showMaximized()
        self.setWindowTitle(self.filename)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
