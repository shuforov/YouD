# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_YouD_path.ui'
#
# Created: Sun May 22 14:10:57 2016
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
        self.verticalLayout_3 = QtGui.QVBoxLayout(path_form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.treeView_dir = QtGui.QTreeView(path_form)
        self.treeView_dir.setObjectName(_fromUtf8("treeView_dir"))
        self.verticalLayout_3.addWidget(self.treeView_dir)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(path_form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(path_form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_name = QtGui.QLabel(path_form)
        self.label_name.setText(_fromUtf8(""))
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.verticalLayout_2.addWidget(self.label_name)
        self.label_path = QtGui.QLabel(path_form)
        self.label_path.setText(_fromUtf8(""))
        self.label_path.setObjectName(_fromUtf8("label_path"))
        self.verticalLayout_2.addWidget(self.label_path)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.chose_dir_path = QtGui.QPushButton(path_form)
        self.chose_dir_path.setObjectName(_fromUtf8("chose_dir_path"))
        self.verticalLayout_3.addWidget(self.chose_dir_path)
        self.cancel_button = QtGui.QPushButton(path_form)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.verticalLayout_3.addWidget(self.cancel_button)

        self.retranslateUi(path_form)
        QtCore.QMetaObject.connectSlotsByName(path_form)

    def retranslateUi(self, path_form):
        path_form.setWindowTitle(_translate("path_form", "Path Dir", None))
        self.label_3.setText(_translate("path_form", "Name :", None))
        self.label_4.setText(_translate("path_form", "Path :", None))
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

