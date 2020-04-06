import os

class FolderCreator:
    def __init__(self, root_path):
        self.root_path = root_path
        self.path = os.path.dirname(self.root_path)

    def create_new_folders(self):
        if self.check_folder_present('music'):
            pass
        else:
            self.create_main_folders('music')
        if self.check_folder_present('video'):
            pass
        else:
            self.create_main_folders('video')

    def check_folder_present(self, name):
        return os.path.isdir(f"{self.path}\{name}")

    def create_main_folders(self, dir_name):
        try:
            print(f'Creating {dir_name} directory....')
            make_dir = os.mkdir(f"{self.path}\\{dir_name}")
            print(f'Done, folder created at {make_dir}')
        except OSError:
            print(f'Dirrectory {dir_name} already exist')
