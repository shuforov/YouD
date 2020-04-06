from classes import Downloader
from classes import Convertor

class Options:
    def __init__(self):
        self.youd = Downloader.Downloader
        self.type_link = input("Type your url link here \n=>")

    def chose_options(self, option):
        if option == 'O':
            self.youd().download_single(self.type_link)
            return True
        elif option == 'P':
            self.youd().download_playlist(self.type_link)
            return True
        elif option == 'C':
            self.youd().convert_music()
            return True
        elif option == 'Q':
            return False
        else:
            return False