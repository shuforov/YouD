<p align="center">
  <img src="https://github.com/shuforov/YouD/blob/youd/Ui_YouD/YouDico.png?raw=true" >
</p>
YouD is free software application with which you can download videos from YouTube. 
There are two version of it, Terminal and Ui:

* T_YouD is terminal version of YouD, it use only python interpreter python and pafy module.
* Ui_YouD is user interface application version of T_YouD.  

### Prerequisites
For Linux

* `p7zip-full` should be installed

##  Install T_YouD on linux
Application install to your home directory and add to PATH
```shell
cd
mkdir youd
cd youd
wget -O YouD.zip https://github.com/shuforov/YouD/archive/master.zip
7z x YouD.zip
mkdir ~/.YouD
cd YouD-master
cp ./T_YouD/youd_t ~/.YouD/
export PATH=$PATH:~/.YouD/
cd
```
To run application in terminal
```shell
youd_t
```
##  Install Ui_YouD on linux
Application install to your home directory and add to PATH
```shell
cd
mkdir youd
cd youd
wget -O YouD.zip https://github.com/shuforov/YouD/archive/master.zip
7z x YouD.zip
mkdir ~/.YouD
cd YouD-master
cp ./Ui_YouD/Linux_build/youd ~/.YouD/
export PATH=$PATH:~/.YouD/
cd
```
To run application in terminal 
```shell
youd
```

## Terminal Downloader (T_YouD)
### On linux

Dependency:

* python 2.7
* pafy

##### Install [Pafy](https://github.com/mps-youtube/pafy)
```shell
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install install pafy
sudo pip install --upgrade youtube_dl
```

### On Windows

Install [Python 2.7](https://www.python.org/downloads/windows/)
Make sure that during installation feature "Add python.exe to Path" will be set.In other way add python.exe to PATH manually.
##### Add python.exe to PATH manually

1. My computer property
2. Control Panel\System 
3. Advanced system settings
4. Environment Variables
**In System Variables "Edit" the "PATH" and add to the end next** 
5. C:\Python27\;C:\Python27\Scripts\
                
##### Install [Pafy](https://github.com/mps-youtube/pafy)
1. Open Command prompt (cmd) and do next:
```shell
pip install pafy
pip install --upgrade youtube-dl
```


## Ui Downloader (Ui_YouD)

### On Linux

Dependency:

* python 2.7
* pafy

##### Install [Pafy](https://github.com/mps-youtube/pafy)
```shell
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install install pafy
sudo pip install --upgrade youtube_dl
```


### On Windows

Install [Python 2.7](https://www.python.org/downloads/windows/)
Make sure that during installation feature "Add python.exe to Path" will be set.In other way add python.exe to PATH manually.
##### Add python.exe to PATH manually

1. My computer property
2. Control Panel\System 
3. Advanced system settings
4. Environment Variables
**In System Variables "Edit" the "PATH" and add to the end next** 
5. C:\Python27\;C:\Python27\Scripts\
                
##### Install [Pafy](https://github.com/mps-youtube/pafy)
1. Open Command prompt (cmd) and do next:
```shell
pip install pafy
pip install --upgrade youtube-dl
```

##### Install [Pyqt4](http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x32.exe)
