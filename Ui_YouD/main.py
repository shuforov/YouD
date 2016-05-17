import sys
import pafy

from PyQt4 import QtGui, QtCore
from Ui_YouD import Ui_Form

class Form1(QtGui.QWidget, Ui_Form):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_Form.__init__(self)
        # Configure ui interface
        self.setupUi(self)
        # connect info button to check info about url and add to list widget formats
        self.connect(self.UrlButton, QtCore.SIGNAL("clicked()"),self.takeandadd)
        self.comboBox_format_type.activated[str].connect(self.chose_type)
        self.connect(self.DownloadButton, QtCore.SIGNAL("clicked()"),self.download_url)






#https://www.youtube.com/watch?v=9ZetitIsaSM
    # take url and add items to check box and list
    def takeandadd(self):
        text = self.lineEdit.text()
        try:
            if text != False:
                self.comboBox_format_type.clear()
                self.comboBox_format_type.addItem('-Chose Type-')
                self.comboBox_format_type.addItem('audio streams')
                self.comboBox_format_type.addItem('video streams')
                self.comboBox_format_type.addItem('all streams')
        except:
            pass

    def chose_type(self, text):
        text_url = self.lineEdit.text()
        url = pafy.new(text_url)
        list_form_audio = url.audiostreams
        list_form_video = url.streams
        list_form_all_type = url.allstreams
        if text == 'audio streams':
            self.listWidget_type.clear()
            string_list_form_audio = []
            for x in list_form_audio:
                string_list_form_audio.append(str(x))
            len_list_formats = len(list_form_audio)
            counter = 0
            while len_list_formats > 0:
                self.listWidget_type.addItem(string_list_form_audio[counter])
                counter += 1
                len_list_formats = len_list_formats - 1
        elif text == 'video streams':
            self.listWidget_type.clear()
            string_list_form_video = []
            for x in list_form_video:
                string_list_form_video.append(str(x))
            len_list_formats = len(list_form_video)
            counter = 0
            while len_list_formats > 0:
                self.listWidget_type.addItem(string_list_form_video[counter])
                counter += 1
                len_list_formats = len_list_formats - 1
        elif text == 'all streams':
            self.listWidget_type.clear()
            string_list_form_all_type = []
            for x in list_form_all_type:
                string_list_form_all_type.append(str(x))
            len_list_formats = len(list_form_all_type)
            counter = 0
            while len_list_formats > 0:
                self.listWidget_type.addItem(string_list_form_all_type[counter])
                counter += 1
                len_list_formats = len_list_formats - 1

    def download_url(self):

        print self.listWidget_type.currentRow()
        text_d = str(self.listWidget_type.currentItem().text())
        print text_d
        print type(text_d)

        text_url = self.lineEdit.text()
        url = pafy.new(text_url)
        list_form_audio = url.audiostreams
        list_form_video = url.streams
        list_form_all_type = url.allstreams

        dict_list_form_audio = {}
        dict_list_form_video = {}
        dict_list_form_all_type = {}

        counter = 0

        for x in list_form_audio:
            dict_list_form_audio[str(x)] = list_form_audio[counter]
            counter += 1

        counter =0
        for x in list_form_video:
            dict_list_form_video[str(x)] = list_form_video[counter]
            counter += 1

        counter = 0
        for x in list_form_all_type:
            dict_list_form_all_type[str(x)] = list_form_all_type[counter]
            counter += 1

        # print list_form_video
        # print list_form_all_type
        # print list_form_audio
        # print type(list_form_all_type[0])


        if text_d in dict_list_form_audio:
            path_file = self.lineEdit_path.text()
            dict_list_form_audio[text_d].download(filepath=path_file)
        elif text_d in dict_list_form_video:
            path_file = self.lineEdit_path.text()
            dict_list_form_video[text_d].download(filepath=path_file)
        elif text_d in dict_list_form_all_type:
            path_file = self.lineEdit_path.text()
            dict_list_form_all_type[text_d].download(filepath=path_file)


        # list_form_all_type[0].download(filepath='')





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())


