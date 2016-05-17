# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_ui.ui'
#
# Created: Tue May 17 17:25:33 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 322)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.UrlGroup = QtGui.QGroupBox(Form)
        self.UrlGroup.setObjectName(_fromUtf8("UrlGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.UrlGroup)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.UrlGroup)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.UrlButton = QtGui.QPushButton(self.UrlGroup)
        self.UrlButton.setObjectName(_fromUtf8("UrlButton"))
        self.horizontalLayout.addWidget(self.UrlButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.UrlGroup)
        self.FormatGroup = QtGui.QGroupBox(Form)
        self.FormatGroup.setObjectName(_fromUtf8("FormatGroup"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.FormatGroup)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.comboBox_format_type = QtGui.QComboBox(self.FormatGroup)
        self.comboBox_format_type.setObjectName(_fromUtf8("comboBox_format_type"))
        self.verticalLayout_3.addWidget(self.comboBox_format_type)
        self.listWidget_type = QtGui.QListWidget(self.FormatGroup)
        self.listWidget_type.setObjectName(_fromUtf8("listWidget_type"))
        self.verticalLayout_3.addWidget(self.listWidget_type)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.FormatGroup)
        self.DownloadGroup = QtGui.QGroupBox(Form)
        self.DownloadGroup.setObjectName(_fromUtf8("DownloadGroup"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.DownloadGroup)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_path = QtGui.QLineEdit(self.DownloadGroup)
        self.lineEdit_path.setObjectName(_fromUtf8("lineEdit_path"))
        self.horizontalLayout_2.addWidget(self.lineEdit_path)
        self.DownloadButton = QtGui.QPushButton(self.DownloadGroup)
        self.DownloadButton.setObjectName(_fromUtf8("DownloadButton"))
        self.horizontalLayout_2.addWidget(self.DownloadButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.DownloadGroup)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.UrlGroup.setTitle(_translate("Form", "Type your url link here", None))
        self.UrlButton.setText(_translate("Form", "Chack url", None))
        self.FormatGroup.setTitle(_translate("Form", "Chose type of format", None))
        self.DownloadGroup.setTitle(_translate("Form", "Type path to download plase", None))
        self.DownloadButton.setText(_translate("Form", "Download", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

