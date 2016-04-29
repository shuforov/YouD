import sys
import pafy

from PyQt4 import QtGui,QtCore

class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(150,150,450,350)
        self.setWindowTitle("Ui_YouD_ui")

        self.tb = QtGui.QPushButton('Take information', self)
        self.tb.setGeometry(10,10, 130, 30)
        self.tb.clicked.connect(self.take_inf)

        self.le = QtGui.QLineEdit(self)
        self.le.setGeometry(11,40,350,20)

        self.ql = QtGui.QLabel('Image', self)
        self.ql.setGeometry(13,55,200,200)
        self.ql.setPixmap(QtGui.QPixmap('image.jpg'))



    def take_inf(self):
        text = self.le.text()
        print text
        url = pafy.new(text)
        print '------------------'
        image_url = 'Image', url.bigthumb
        print url.bigthumb
        print 'Title:', url.title
        print 'Duration:', url.duration
        print '------------------'

app = QtGui.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())


#https://www.youtube.com/watch?v=9ZetitIsaSM