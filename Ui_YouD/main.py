# -*- coding: utf-8 -*-
import sys
import pafy
import os, signal
from PyQt4 import QtGui, QtCore
from Ui_YouD import Ui_Ui_YouD

class YouD(QtGui.QWidget, Ui_Ui_YouD):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        Ui_Ui_YouD.__init__(self)
        # Configure ui interface
        self.setupUi(self)
        # Config buttons
        self.connect(self.UrlButton, QtCore.SIGNAL("clicked()"),self.takeandadd)
        self.connect(self.DownloadButton, QtCore.SIGNAL("clicked()"),self.download_url)
        self.connect(self.Path_button, QtCore.SIGNAL("clicked()"),self.YouD_path_f)
        self.connect(self.listWidget_type, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.active_down_group)
        self.comboBox_format_type.activated[str].connect(self.chose_type)
        # Global variables
        self.new_path_dir = ''
        self.path_file = os.getcwd()
        self.tempo_decod = self.path_file.decode('utf8')
        self.base_path = self.tempo_decod
        # Set base focus
        self.FormatGroup.setEnabled(False)
        self.DownloadGroup.setEnabled(False)
        #log file
        self.oldstdout = sys.stdout
        sys.stdout = file(self.base_path + '/log', "w")


    def active_down_group(self):
        self.DownloadGroup.setEnabled(True)

    # Take url and add items type of media to check box
    def takeandadd(self):
        print 'takeandadd start'
        text = self.lineEdit.text()
        try:
            url = pafy.new(text)
            print url
            self.FormatGroup.setEnabled(True)
            self.comboBox_format_type.clear()
            self.comboBox_format_type.addItem('-----')
            self.comboBox_format_type.addItem('Audio')
            self.comboBox_format_type.addItem('Video')
            self.comboBox_format_type.addItem('All')
            self.listWidget_type.clear()
            print 'takeandadd end \n'
        except ValueError:
            print '!!takeandadd exept exec'
            self.FormatGroup.setEnabled(False)
            self.DownloadGroup.setEnabled(False)
            msg = QtGui.QMessageBox()
            msg.setWindowModality(QtCore.Qt.ApplicationModal)
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.setText("Please check you entered is correct")
            msg.setWindowTitle("Invalid link")
            msg.exec_()

    # Chose type of media from widget list   
    def chose_type(self, text):

        print 'chose_type start'
        if self.comboBox_format_type.itemText(0) == '-----':
            self.comboBox_format_type.removeItem(0)
        text_url = self.lineEdit.text()
        url = pafy.new(text_url)
        list_form_audio = url.audiostreams
        list_form_video = url.streams
        list_form_all_type = url.allstreams
        if text == 'Audio':
            self.listWidget_type.clear()
            self.lineEdit_path.setText(self.base_path)
            string_list_form_audio = []
            for x in list_form_audio:
                string_list_form_audio.append(str(x))
            len_list_formats = len(list_form_audio)
            counter = 0
            while len_list_formats > 0:
                self.listWidget_type.addItem(string_list_form_audio[counter])
                counter += 1
                len_list_formats = len_list_formats - 1
        elif text == 'Video':
            self.listWidget_type.clear()
            self.lineEdit_path.setText(self.base_path)
            string_list_form_video = []
            for x in list_form_video:
                string_list_form_video.append(str(x))
            len_list_formats = len(list_form_video)
            counter = 0
            while len_list_formats > 0:
                self.listWidget_type.addItem(string_list_form_video[counter])
                counter += 1
                len_list_formats = len_list_formats - 1
        elif text == 'All':
            self.listWidget_type.clear()
            self.lineEdit_path.setText(self.base_path)
            string_list_form_all_type = []
            for x in list_form_all_type:
                string_list_form_all_type.append(str(x))
            len_list_formats = len(list_form_all_type)
            counter = 0
            while len_list_formats > 0:
                self.listWidget_type.addItem(string_list_form_all_type[counter])
                counter += 1
                len_list_formats = len_list_formats - 1
        print 'shose_type end \n'
    # Set puth download
    def YouD_path_f(self):
        print 'youd_path_f start'
        path_dir = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
        print 'path dir- >', path_dir
        self.new_path_dir = unicode(path_dir)
        self.lineEdit_path.setText(self.new_path_dir)
        print 'youd_path_f end\n'

    # Execute script of downloading, using pafy module.
    def download_url(self):
        print 'download_url start'
        text_d = str(self.listWidget_type.currentItem().text())
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
        if text_d in dict_list_form_audio:
            def progress(total, recvd, ratio, rate, eta):
                # print ratio
                number = ratio
                dec = str(number - int(number))[2:4]
                self.UrlGroup.setEnabled(False)
                self.FormatGroup.setEnabled(False)
                self.DownloadGroup.setEnabled(False)
                if int(ratio) == 0:
                    self.completed = int(dec)
                    self.progressBar_download.setValue(self.completed)
                elif int(ratio) == 1:
                    self.completed = 100
                    self.progressBar_download.setValue(self.completed)
                    self.UrlGroup.setEnabled(True)
                    self.FormatGroup.setEnabled(True)
                    self.DownloadGroup.setEnabled(True)
                    print number
                    print 'download_url end \n'
            if self.new_path_dir == '':
                path_file = unicode(self.lineEdit_path.text())
            elif self.new_path_dir != '':
                path_file = self.new_path_dir
            dict_list_form_audio[text_d].download(filepath=path_file, quiet=True, callback=progress)
        elif text_d in dict_list_form_video:
            def progress(total, recvd, ratio, rate, eta):
                number = ratio
                dec = str(number - int(number))[2:4]
                self.UrlGroup.setEnabled(False)
                self.FormatGroup.setEnabled(False)
                self.DownloadGroup.setEnabled(False)
                if int(ratio) == 0:
                    self.completed = int(dec)
                    self.progressBar_download.setValue(self.completed)
                elif int(ratio) == 1:
                    self.completed = 100
                    self.progressBar_download.setValue(self.completed)
                    self.UrlGroup.setEnabled(True)
                    self.FormatGroup.setEnabled(True)
                    self.DownloadGroup.setEnabled(True)
                    print number
                    print 'download_url end \n'
            if self.new_path_dir == '':
                path_file = unicode(self.lineEdit_path.text())
            elif self.new_path_dir != '':
                path_file = self.new_path_dir
            dict_list_form_video[text_d].download(filepath=path_file, quiet=True, callback=progress)
        elif text_d in dict_list_form_all_type:
            def progress(total, recvd, ratio, rate, eta):
                number = ratio
                dec = str(number - int(number))[2:4]
                self.UrlGroup.setEnabled(False)
                self.FormatGroup.setEnabled(False)
                self.DownloadGroup.setEnabled(False)
                if int(ratio) == 0:
                    self.completed = int(dec)
                    self.progressBar_download.setValue(self.completed)
                elif int(ratio) == 1:
                    self.completed = 100
                    self.progressBar_download.setValue(self.completed)
                    self.UrlGroup.setEnabled(True)
                    self.FormatGroup.setEnabled(True)
                    self.DownloadGroup.setEnabled(True)
                    print number
                    print 'download_url end \n'
            if self.new_path_dir == '':
                path_file = unicode(self.lineEdit_path.text())
            elif self.new_path_dir != '':
                path_file = self.new_path_dir
            dict_list_form_all_type[text_d].download(filepath=path_file, quiet=True, callback=progress)
        print 'Download complite'
        print '----------------\n'
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = YouD()
    window.show()
    sys.exit(app.exec_())
    sys.stdout.close()


