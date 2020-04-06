import pafy
import re
import os

class Downloader:
    """ Downloader of video from youtube and convertor of audio files """

    AUDIO_STREAMS = ['audio:webm@50k', 'audio:webm@70k', 'audio:m4a@128k', 'audio:webm@160k']
    STREAMS = ['normal:mp4@640x360']
    ALL_STREAMS = ['audio:webm@50k', 'audio:webm@70k', 'audio:m4a@128k', 'audio:webm@160k', 'video:webm@256x144', 'video:mp4@256x144', 'video:webm@426x240', 'video:mp4@426x240', 'video:webm@640x360', 'video:mp4@640x360', 'video:webm@854x480', 'video:mp4@854x480', 'video:webm@1280x720', 'video:mp4@1280x720', 'normal:mp4@640x360']
    LIST_OF_STREAM_TYPES = ['audio streams', 'streams', 'all streams']
    OPTIONS = ['(O)Download one video', '(P)Download playlist', '(C)Convert music file to mp3 format', '(Q)Quit']
    TYPE_OF_DATA = ['(0)Audio', '(1)Video']
    ROOT_PATH = ['./']
    PLAYLIST_DOWNLOAD_FORMATS = ['getbestaudio', 'getbest']
    FILE_PATHS = ['music', 'video']

    def constant_get(self, number_constant):
        constant_get = [self.AUDIO_STREAMS, self.STREAMS, self.ALL_STREAMS, self.LIST_OF_STREAM_TYPES, self.OPTIONS, self.TYPE_OF_DATA, self.ROOT_PATH, self.PLAYLIST_DOWNLOAD_FORMATS, self.FILE_PATHS]
        return constant_get[int(number_constant)]

    def info_url(self, url):
        print('------------------')
        print('Title:', url.title)
        print('Thumb:', url.thumb)
        print('Duration:', url.duration)
        print('------------------')
        print('Chose the list of available formats and enter the number:')

    def snake_case(self, word):
        snaked = re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()
        return snaked.replace(' ', '_')

    def take_data_url_link(self, url):
        return pafy.new(url)

    def take_stream_type(self, url, number):
        return getattr(url, self.LIST_OF_STREAM_TYPES[number].replace(" ", ""))

    def download(self, type_download, number, url, format_url = None):
        path = os.path.dirname(os.path.realpath(__file__)) 
        path_folder = os.mkdir(f"{path}\{self.FILE_PATHS[number]}")
        if type_download == 'single':
            self.take_stream_type(url, number)[int(format_url)].download(filepath=path_folder)
        elif type_download == 'playlist':
            for element in range(len(url['items'])):
                link_video = getattr(url['items'][element]['pafy'], self.PLAYLIST_DOWNLOAD_FORMATS[number])()
                link_video.download(filepath=path_folder)           
        else:
            None

    def download_single(self, url_link):
        """ Download single video url """
        url = self.take_data_url_link(url_link)
        self.info_url(url)
        for indx, val in enumerate(self.LIST_OF_STREAM_TYPES): print(indx, val)
        number = input('->')
        for indx, val in enumerate(self.constant_get(number)): print(indx, val)
        format_url = input('Chose format to download ->')
        self.download('single', int(number), url, format_url)

    def download_playlist(self, url):
        """ Download all videos from playlist """
        pl_link = pafy.get_playlist(url) 
        chose = input(f"Chose format: {' '.join(self.TYPE_OF_DATA)} download\n=>")
        self.download('playlist', int(chose), pl_link)
        print("Download finished")
