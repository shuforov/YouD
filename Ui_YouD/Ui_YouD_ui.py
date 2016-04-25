import sys
from PyQt4 import QtGui,QtCore

class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(150,150,450,350)
        self.setWindowTitle("Ui_YouD_ui")

        tb = QtGui.QPushButton('Take information', self)
        tb.setGeometry(10,10, 130, 30)

        le = QtGui.QLineEdit(self)
        le.setGeometry(11,40,200,20)

        tb.clicked.connect(self.take_inf)

    def take_inf(self):
        text = self.le.text()
        print text

app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())