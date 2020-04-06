import os
import ffmpy3
import shutil

class Convertor():
    CONVERTOR_FROM_TYPES = ['.webm', '.m4a']
    CONVERT_AUDIO_TO = '.mp3'
    ROOT_PATH = ['./']
    FILE_PATHS = ['./music', './video', ROOT_PATH]

    def create_converted_dir():
        try:
            os.makedirs('./music/converted')
        except OSError:
            print("Directory converted already exist")

    def convert_music():
        create_converted_dir()
        os.chdir('./music')
        for file in os.listdir(ROOT_PATH):
            if file.endswith(".webm"):
                ff = ffmpy3.FFmpeg(
                    inputs={file: None},
                    outputs={file[:-5]+CONVERT_AUDIO_TO: None})
                ff.run()
            elif file.endswith(".m4a"):
                ff = ffmpy3.FFmpeg(
                        inputs={file: None},
                        outputs={file[:-4]+CONVERT_AUDIO_TO: None})
                ff.run()
            else:
                pass
        for file in os.listdir(ROOT_PATH):
            if file.endswith(CONVERT_AUDIO_TO):
                shutil.move(file, './converted')
        for file in os.listdir(ROOT_PATH):
            if file.endswith(".webm") or file.endswith(".m4a"):
                os.remove(file)
