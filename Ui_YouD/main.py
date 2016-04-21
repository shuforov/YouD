import sys
from PyQt4 import QtCore, QtGui


app = QtGui.QApplication(sys, argv)
window = QtGui.QWidget()
ui = Ui_YouD_ui.Ui_Dialog()
ui.setupUi(window)

QtCore.QObject.connect(ui.pushButton, QtCore.SIGNAL("clicked()"), lambda: test(ui))

def test(ui):
    ui = Ui_YouD_ui.Ui_Form
    ui.textEdit.setText("Button")

window.show()
sys.exit(app.exec_())