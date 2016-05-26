# -*- coding: utf-8 -*-

import sys
import pafy
from PyQt4 import QtGui, QtCore
from Ui_YouD import Ui_Ui_YouD

class YouD(QtGui.QWidget, Ui_Ui_YouD):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        Ui_Ui_YouD.__init__(self)
        # Configure ui interface
        self.setupUi(self)
        # connect info button to check info about url and add to list widget formats
        self.connect(self.UrlButton, QtCore.SIGNAL("clicked()"),self.takeandadd)
        self.comboBox_format_type.activated[str].connect(self.chose_type)
        self.connect(self.DownloadButton, QtCore.SIGNAL("clicked()"),self.download_url)
        self.connect(self.Path_button, QtCore.SIGNAL("clicked()"),self.YouD_path_f)

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
        # print self.listWidget_type.currentRow()
        text_d = str(self.listWidget_type.currentItem().text())
        # print text_d
        # print type(text_d)
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
            def progress(total, recvd, ratio, rate, eta):
                # print ratio
                number = ratio
                dec = str(number - int(number))[2:4]
                if int(ratio) == 0:
                    self.completed = int(dec)
                    self.progressBar_download.setValue(self.completed)
                elif int(ratio) == 1:
                    self.completed = 100
                    self.progressBar_download.setValue(self.completed)
            path_file = str(self.lineEdit_path.text())
            dict_list_form_audio[text_d].download(filepath=path_file, quiet=True, callback=progress)
        elif text_d in dict_list_form_video:
            def progress(total, recvd, ratio, rate, eta):
                # print ratio
                number = ratio
                dec = str(number - int(number))[2:4]
                if int(ratio) == 0:
                    self.completed = int(dec)
                    self.progressBar_download.setValue(self.completed)
                elif int(ratio) == 1:
                    self.completed = 100
                    self.progressBar_download.setValue(self.completed)
            path_file = str(self.lineEdit_path.text())
            dict_list_form_video[text_d].download(filepath=path_file, quiet=True, callback=progress)
        elif text_d in dict_list_form_all_type:
            def progress(total, recvd, ratio, rate, eta):
                # print ratio
                number = ratio
                dec = str(number - int(number))[2:4]
                if int(ratio) == 0:
                    self.completed = int(dec)
                    self.progressBar_download.setValue(self.completed)
                elif int(ratio) == 1:
                    self.completed = 100
                    self.progressBar_download.setValue(self.completed)
            path_file = str(self.lineEdit_path.text())
            dict_list_form_all_type[text_d].download(filepath=path_file, quiet=True, callback=progress)
        # list_form_all_type[0].download(filepath='')

    def YouD_path_f(self):
        path_dir = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
        self.lineEdit_path.setText(path_dir)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = YouD()
    window.show()
    sys.exit(app.exec_())


