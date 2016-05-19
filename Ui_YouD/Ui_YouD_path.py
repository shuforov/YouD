# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_YouD_path.ui'
#
# Created: Thu May 19 11:50:34 2016
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

class Ui_path_form(object):
    def setupUi(self, path_form):
        path_form.setObjectName(_fromUtf8("path_form"))
        path_form.resize(392, 313)
        # path_form.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(path_form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeView_dir = QtGui.QTreeView(path_form)
        self.treeView_dir.setObjectName(_fromUtf8("treeView_dir"))
        self.verticalLayout.addWidget(self.treeView_dir)
        self.chose_dir_path = QtGui.QPushButton(path_form)
        self.chose_dir_path.setObjectName(_fromUtf8("chose_dir_path"))
        self.verticalLayout.addWidget(self.chose_dir_path)
        self.cancel_button = QtGui.QPushButton(path_form)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.verticalLayout.addWidget(self.cancel_button)

        self.retranslateUi(path_form)
        QtCore.QMetaObject.connectSlotsByName(path_form)

    def retranslateUi(self, path_form):
        path_form.setWindowTitle(_translate("path_form", "Path Dir", None))
        self.chose_dir_path.setText(_translate("path_form", "Chose Dir", None))
        self.cancel_button.setText(_translate("path_form", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    path_form = QtGui.QDialog()
    ui = Ui_path_form()
    ui.setupUi(path_form)
    path_form.show()
    sys.exit(app.exec_())

