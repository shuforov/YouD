import pafy
import os
import ffmpy
import shutil


def download_single(url_link):
    """ Download single video url """
    url = pafy.new(url_link)
    print '------------------'
    print 'Title:', url.title
    print 'Thumb:', url.thumb
    print 'Duration:', url.duration
    print '------------------'
    print 'Chose the list of available formats and enter the number:'
    temp_list = ['audio streams', 'streams', 'all streams']
    counter_for_inf = 1
    for x in temp_list:
        print counter_for_inf, x
        counter_for_inf += 1
    number = int(raw_input('->'))
    list_of_formats = []
    counter = 0
    if number == 1:
        list_of_formats = url.audiostreams
        for x in url.audiostreams:
            print counter, x
            counter += 1
    elif number == 2:
        list_of_formats = url.streams
        for x in url.streams:
            print counter, x
            counter += 1
    elif number == 3:
        list_of_formats = url.allstreams
        for x in url.allstreams:
            print counter, x
            counter += 1

    format_url = int(raw_input('Chose format to download ->'))
    print 'Type the path where will be downloaded file'
    print 'Example for windows "D:/" or "D:/downloads"'
    print 'Example for linux "/home/<user_name>"'
    print 'leave empty to download in app director'
    path_file = raw_input('->')
    list_of_formats[format_url].download(filepath=path_file)


def download_playlist(url_link):
    """ Download all videos from playlist """
    playlist_link = pafy.get_playlist(url_link)
    chose = raw_input("Chose format (A)audio or (V)video download\n=>")
    if chose == 'A':
        for element in range(len(playlist_link['items'])):
            link_video = playlist_link['items'][element]['pafy'].getbestaudio()
            link_video.download(filepath='./music')
    elif chose == 'V':
        for element in range(len(playlist_link['items'])):
            link_video = playlist_link['items'][element]['pafy'].getbest()
            link_video.download(filepath='video')
    print "Download finished"


def convert_music():
    try:
        os.makedirs('./music/converted')
    except OSError:
        print "Directory converted already exist"
    os.chdir('./music')
    for file in os.listdir("./"):
        if file.endswith(".webm"):
            ff = ffmpy.FFmpeg(
                inputs={file: None},
                outputs={file[:-5]+'.mp3': None})
            ff.run()
        elif file.endswith(".m4a"):
            ff = ffmpy.FFmpeg(
                    inputs={file: None},
                    outputs={file[:-4]+'.mp3': None})
            ff.run()
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            shutil.move(file, './converted')


def main():
    chose_exit = True
    while chose_exit:
        chose = raw_input("(O)Download one video, (P)Download playlist,\n\
(C)Convert all music to mp3 format, (Q)Quit\n=>")
        if chose == 'O':
            url = raw_input("Type your url link here \n=>")
            download_single(url)
        elif chose == 'P':
            try:
                print "Chack if exist music directory...."
                os.makedirs('./music')
                print "OK"
            except OSError:
                print 'Dirrectory music already exist'
            try:
                print "Chack if exist video directory...."
                os.makedirs('./video')
                print 'OK'
            except OSError:
                print 'Dirrectory video already exist'
            url = raw_input("Type your url link here \n=>")
            download_playlist(url)
        elif chose == 'C':
            convert_music()
        elif chose == 'Q':
            chose_exit = False
        else:
            print "Wronge chose, please try agen"

if __name__ == "__main__":
    main()
