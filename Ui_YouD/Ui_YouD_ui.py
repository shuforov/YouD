# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_YouD.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(576, 462)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.Link = QtGui.QLineEdit(self.groupBox_2)
        self.Link.setMinimumSize(QtCore.QSize(0, 20))
        self.Link.setText(_fromUtf8(""))
        self.Link.setObjectName(_fromUtf8("Link"))
        self.verticalLayout_6.addWidget(self.Link)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.LogoImage = QtGui.QLabel(self.groupBox_3)
        self.LogoImage.setObjectName(_fromUtf8("LogoImage"))
        self.verticalLayout_7.addWidget(self.LogoImage)
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.Description = QtGui.QLabel(self.groupBox_4)
        self.Description.setText(_fromUtf8(""))
        self.Description.setObjectName(_fromUtf8("Description"))
        self.horizontalLayout_7.addWidget(self.Description)
        self.horizontalLayout_5.addWidget(self.groupBox_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.TakeInformation = QtGui.QPushButton(self.tab_2)
        self.TakeInformation.setObjectName(_fromUtf8("TakeInformation"))
        self.horizontalLayout_6.addWidget(self.TakeInformation)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.TypeOfStream = QtGui.QComboBox(self.tab)
        self.TypeOfStream.setObjectName(_fromUtf8("TypeOfStream"))
        self.TypeOfStream.addItem(_fromUtf8(""))
        self.TypeOfStream.addItem(_fromUtf8(""))
        self.TypeOfStream.addItem(_fromUtf8(""))
        self.verticalLayout_5.addWidget(self.TypeOfStream)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.ListOfStream = QtGui.QListView(self.tab)
        self.ListOfStream.setObjectName(_fromUtf8("ListOfStream"))
        self.horizontalLayout_2.addWidget(self.ListOfStream)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.PathDownload = QtGui.QLineEdit(self.groupBox)
        self.PathDownload.setObjectName(_fromUtf8("PathDownload"))
        self.horizontalLayout_4.addWidget(self.PathDownload)
        self.PathButton = QtGui.QToolButton(self.groupBox)
        self.PathButton.setObjectName(_fromUtf8("PathButton"))
        self.horizontalLayout_4.addWidget(self.PathButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.Download = QtGui.QPushButton(self.tab)
        self.Download.setObjectName(_fromUtf8("Download"))
        self.horizontalLayout_3.addWidget(self.Download)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.TakeInformation, QtCore.SIGNAL('clicked()'), )
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.tabWidget, self.Download)
        Form.setTabOrder(self.Download, self.ListOfStream)
        Form.setTabOrder(self.ListOfStream, self.TypeOfStream)
        Form.setTabOrder(self.TypeOfStream, self.PathDownload)
        Form.setTabOrder(self.PathDownload, self.PathButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_2.setTitle(_translate("Form", "Past your link here", None))
        self.groupBox_3.setTitle(_translate("Form", "Logo", None))
        self.LogoImage.setText(_translate("Form", "Some text", None))
        self.groupBox_4.setTitle(_translate("Form", "Description", None))
        self.TakeInformation.setText(_translate("Form", "Take Information", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Information", None))
        self.TypeOfStream.setItemText(0, _translate("Form", "Audio Streams", None))
        self.TypeOfStream.setItemText(1, _translate("Form", "Video Streams", None))
        self.TypeOfStream.setItemText(2, _translate("Form", "All Streams", None))
        self.groupBox.setTitle(_translate("Form", "Path download", None))
        self.PathButton.setText(_translate("Form", "...", None))
        self.Download.setText(_translate("Form", "Download", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Download", None))

def printsome(self):
    self.LogoImage


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())