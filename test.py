from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('UI//mainWindow.ui', self) # Load the .ui file
        self.pushButton.clicked.connect(self.changelabeltext)
        self.show() # Show the GUI
    def changelabeltext(self):
        self.pushButton.setText("asdsadsad")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()













