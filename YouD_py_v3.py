import pafy
import os
import ffmpy
import shutil


class You_downloader(object):
    """ Downloader of video from youtube and convertor of audio files """

    @staticmethod
    def download_single(url_link):
        """ Download single video url """
        url = pafy.new(url_link)
        print('------------------')
        print('Title:'), url.title
        print('Thumb:'), url.thumb
        print('Duration:'), url.duration
        print('------------------')
        print('Chose the list of available formats and enter the number:')
        temp_list = ['audio streams', 'streams', 'all streams']
        counter_for_inf = 1
        for x in temp_list:
            print(counter_for_inf, x)
            counter_for_inf += 1
        number = int(raw_input('->'))
        list_of_formats = []
        counter = 0
        if number == 1:
            list_of_formats = url.audiostreams
            for x in url.audiostreams:
                print(counter, x)
                counter += 1
        elif number == 2:
            list_of_formats = url.streams
            for x in url.streams:
                print(counter, x)
                counter += 1
        elif number == 3:
            list_of_formats = url.allstreams
            for x in url.allstreams:
                print(counter, x)
                counter += 1

        format_url = int(raw_input('Chose format to download ->'))
        if number == 1:
            list_of_formats[format_url].download(filepath='./music')
        elif number == 2:
            list_of_formats[format_url].download(filepath='./video')
        elif number == 3:
            list_of_formats[format_url].download(filepath='./')

    @staticmethod
    def download_playlist(url_link):
        """ Download all videos from playlist """
        pl_link = pafy.get_playlist(url_link)
        chose = input("Chose format (A)audio or (V)video download\n=>")
        if chose == 'A':
            for element in range(len(pl_link['items'])):
                link_video = pl_link['items'][element]['pafy'].getbestaudio()
                link_video.download(filepath='./music')
        elif chose == 'V':
            for element in range(len(pl_link['items'])):
                link_video = pl_link['items'][element]['pafy'].getbest()
                link_video.download(filepath='video')
        print("Download finished")

    @staticmethod
    def convert_music():
        try:
            os.makedirs('./music/converted')
        except OSError:
            print("Directory converted already exist")
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
            else:
                pass
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                shutil.move(file, './converted')
        for file in os.listdir("./"):
            if file.endswith(".webm") or file.endswith(".m4a"):
                os.remove(file)


def main():
    youd = You_downloader()
    chose_exit = True
    while chose_exit:
        chose = input("(O)Download one video, (P)Download playlist,\n\
(C)Convert music file to mp3 format, (Q)Quit\n=>")
        if chose == 'O':
            url = input("Type your url link here \n=>")
            youd.download_single(url)
        elif chose == 'P':
            try:
                print("Chack if exist music directory....")
                os.makedirs('./music')
                print("OK")
            except OSError:
                print('Dirrectory music already exist')
            try:
                print("Chack if exist video directory....")
                os.makedirs('./video')
                print('OK')
            except OSError:
                print('Dirrectory video already exist')
            url = input("Type your url link here \n=>")
            youd.download_playlist(url)
        elif chose == 'C':
            youd.convert_music()
        elif chose == 'Q':
            chose_exit = False
        else:
            print("Wronge chose, please try agen")

if __name__ == "__main__":
    """ If you dont want use builtin main function, and use this class as lib \
        comment out main() at the bottom and uncomment pass command """
    main()
    # pass
