# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_YouD.ui'
#
# Created: Wed May 18 13:03:00 2016
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

class Ui_Ui_YouD(object):
    def setupUi(self, Ui_YouD):
        Ui_YouD.setObjectName(_fromUtf8("Ui_YouD"))
        Ui_YouD.resize(400, 353)
        self.verticalLayout = QtGui.QVBoxLayout(Ui_YouD)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.UrlGroup = QtGui.QGroupBox(Ui_YouD)
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
        self.FormatGroup = QtGui.QGroupBox(Ui_YouD)
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
        self.DownloadGroup = QtGui.QGroupBox(Ui_YouD)
        self.DownloadGroup.setObjectName(_fromUtf8("DownloadGroup"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.DownloadGroup)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_path = QtGui.QLineEdit(self.DownloadGroup)
        self.lineEdit_path.setObjectName(_fromUtf8("lineEdit_path"))
        self.horizontalLayout_2.addWidget(self.lineEdit_path)
        self.Path_button = QtGui.QPushButton(self.DownloadGroup)
        self.Path_button.setObjectName(_fromUtf8("Path_button"))
        self.horizontalLayout_2.addWidget(self.Path_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.progressBar_download = QtGui.QProgressBar(self.DownloadGroup)
        self.progressBar_download.setProperty("value", 0)
        self.progressBar_download.setObjectName(_fromUtf8("progressBar_download"))
        self.verticalLayout_5.addWidget(self.progressBar_download)
        self.DownloadButton = QtGui.QPushButton(self.DownloadGroup)
        self.DownloadButton.setObjectName(_fromUtf8("DownloadButton"))
        self.verticalLayout_5.addWidget(self.DownloadButton)
        self.verticalLayout.addWidget(self.DownloadGroup)

        self.retranslateUi(Ui_YouD)
        QtCore.QMetaObject.connectSlotsByName(Ui_YouD)

    def retranslateUi(self, Ui_YouD):
        Ui_YouD.setWindowTitle(_translate("Ui_YouD", "YouD", None))
        self.UrlGroup.setTitle(_translate("Ui_YouD", "Type your url link here", None))
        self.UrlButton.setText(_translate("Ui_YouD", "Chack url", None))
        self.FormatGroup.setTitle(_translate("Ui_YouD", "Chose type of format", None))
        self.DownloadGroup.setTitle(_translate("Ui_YouD", "Type path to download plase", None))
        self.Path_button.setText(_translate("Ui_YouD", "Chose Dir", None))
        self.DownloadButton.setText(_translate("Ui_YouD", "Download", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Ui_YouD = QtGui.QWidget()
    ui = Ui_Ui_YouD()
    ui.setupUi(Ui_YouD)
    Ui_YouD.show()
    sys.exit(app.exec_())

