from classes import Options
from classes import FolderCreator
import os

def main():
    OPTIONS = ['(O)Download one video', '(P)Download playlist', '(C)Convert music file to mp3 format', '(Q)Quit']

    chose_stay_at_app = True
    main_menu = True
    FolderCreator.FolderCreator(os.path.dirname(os.path.realpath(__file__))).create_new_folders()
    while chose_stay_at_app:
        if main_menu:
            print("\n".join(OPTIONS))
            option = input('->')
            if option == 'Q': chose_stay_at_app = False
            end_time = Options.Options().chose_options(option)
            main_menu = end_time
            chose_stay_at_app = end_time

if __name__ == "__main__":
    """ If you dont want use builtin main function, and use this class as lib \
        comment out main() at the bottom and uncomment pass command """
    main()
    # pass
