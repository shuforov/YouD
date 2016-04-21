import sys
from PyQt4 import QtGui,QtCore

class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(150,150,450,350)
        self.setWindowTitle("Ui_YouD_ui")

        quit = QtGui.QPushButton('Take information', self)
        quit.setGeometry(10,10, 100, 20)

        le = QtGui.QLineEdit(self)
        le.setGeometry(11,30,200,20)

app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())