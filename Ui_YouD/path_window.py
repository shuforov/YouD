import sys

from PyQt4 import QtGui, QtCore
from Ui_YouD_path import Ui_path_form

class YouD_path(QtGui.QWidget, Ui_path_form):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        Ui_path_form.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = YouD_path()
    window.show()
    sys.exit(app.exec_())