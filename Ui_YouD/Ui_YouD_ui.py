import sys
import pafy
import urllib

from PyQt4 import QtGui,QtCore
class Icon(QtGui.QWidget):
    def __init__(self):
        super(Icon, self).__init__()

        grid = QtGui.QGridLayout()
        grid.addWidget(self.UrlGroup(), 0, 0)
        grid.addWidget(self.FormatGroup(),1,0)
        grid.addWidget(self.PathGroup(),2,0)
        self.setLayout(grid)

        self.setWindowTitle("Ui_YouD_ui")
        self.setGeometry(150, 150, 450, 350)
        # self.initUi()


    def UrlGroup(self):
        groupBox = QtGui.QGroupBox("Type your link here")

        # line url
        le = QtGui.QLineEdit()
        # self.le.setGeometry(11, 0, 350, 20)

        def takeInfo(self):
            text = le.text()
            print text
            url = pafy.new(text)
            print '------------------'
            image_url = url.thumb
            urllib.urlretrieve(image_url, "image.jpg")
            print url.thumb
            print 'Title:', url.title
            print 'Duration:', url.duration
            print '------------------'

        # url button
        tb = QtGui.QPushButton('Take information')
        # self.tb.setGeometry(10, 40, 130, 30)
        tb.clicked.connect(takeInfo)



        vbox = QtGui.QHBoxLayout()
        vbox.addWidget(le)
        vbox.addWidget(tb)
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

    def FormatGroup(self):
        groupBox = QtGui.QGroupBox('Format video')

        cb1 = QtGui.QComboBox()

        cb2 = QtGui.QComboBox()

        vbox = QtGui.QHBoxLayout()
        vbox.addWidget(cb1)
        vbox.addWidget(cb2)
        groupBox.setLayout(vbox)

        return groupBox

    def PathGroup(self):
        groupBox = QtGui.QGroupBox("Path")

        le = QtGui.QLineEdit()

        tb = QtGui.QPushButton('Download')

        vbox = QtGui.QHBoxLayout()
        vbox.addWidget(le)
        vbox.addWidget(tb)
        groupBox.setLayout(vbox)

        return groupBox

    def take_inf(self):
        text = self.UrlGroup.le.text()
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
    icon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


#https://www.youtube.com/watch?v=9ZetitIsaSM