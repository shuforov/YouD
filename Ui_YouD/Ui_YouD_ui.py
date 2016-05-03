import sys
import pafy
import urllib

from PyQt4 import QtGui,QtCore
class Icon(QtGui.QWidget):
    def __init__(self):
        super(Icon, self).__init__()

        grid = QtGui.QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        self.setLayout(grid)

        self.setWindowTitle("Ui_YouD_ui")
        self.setGeometry(150, 150, 450, 350)
        self.initUi()

    def createFirstExclusiveGroup(self):
        groupBox = QtGui.QGroupBox("Exclusive Radio Buttons")

        radio1 = QtGui.QRadioButton("&Radio button 1")
        radio2 = QtGui.QRadioButton("R&adio button 2")
        radio3 = QtGui.QRadioButton("Ra&dio button 3")

        radio1.setChecked(True)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def initUi(self):

        #url button
        self.tb = QtGui.QPushButton('Take information', self)
        self.tb.setGeometry(10, 40, 130, 30)
        self.tb.clicked.connect(self.take_inf)

        #line url
        self.le = QtGui.QLineEdit(self)
        self.le.setGeometry(11,20,350,20)

        #line path
        self.le = QtGui.QLineEdit(self)
        self.le.setGeometry(11, 200, 350, 20)

        self.ql = QtGui.QLabel('Image', self)
        self.ql.setGeometry(13, 55, 200, 200)
        self.ql.setPixmap(QtGui.QPixmap('image.jpg'))

        self.show()

    def take_inf(self):
        text = self.le.text()
        print text
        url = pafy.new(text)
        print '------------------'
        image_url = url.thumb
        urllib.urlretrieve(image_url, "image.jpg")

        print url.thumb
        print 'Title:', url.title
        print 'Duration:', url.duration
        print '------------------'

def main():

    app = QtGui.QApplication(sys.argv)
    icon = Icon()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


#https://www.youtube.com/watch?v=9ZetitIsaSM