import shutil
import os


class FileManagerController:
    __path = "C:/Users/thali/Downloads"
    __extension = None

    def __init__(self):
        for file in self.view_files():
            self.__create_directory(file)
            self.__move_file_to_directory(file)

    def view_files(self):
        return [file for file in os.listdir(self.__path) if os.path.isfile(f"{self.__path}/{file}")]

    def __check_directory(self, file: str):
        self.__extension = file.split('.')[-1]
        if os.path.isdir(f"{self.__path}/{self.__extension}") or self.__extension == "ini":
            return True
        else:
            return False

    def __create_directory(self, file: str):
        if not self.__check_directory(file):
            os.mkdir(f"{self.__path}/{self.__extension}")

    def __verify_dir(self, file: str):
        if self.__check_directory(file):
            os.rmdir(f"{self.__path}/{self.__extension}")

    def __move_file_to_directory(self, file: str):
        self.__extension = file.split('.')[-1]
        file_path = f"{self.__path}/{file}"
        if self.__extension == 'exe':
            shutil.move(file_path, f'{self.__path}/exe')
        elif self.__extension == 'torrent':
            shutil.move(file_path, f'{self.__path}/torrent')
        elif self.__extension == 'png':
            shutil.move(file_path, f'{self.__path}/png')
        elif self.__extension == 'jpg':
            shutil.move(file_path, f'{self.__path}/jpg')
        elif self.__extension == 'iso':
            shutil.move(file_path, f'{self.__path}/iso')
        elif self.__extension == 'mp4':
            shutil.move(file_path, f'{self.__path}/mp4')
        elif self.__extension == 'mkv':
            shutil.move(file_path, f'{self.__path}/mkv')
        elif self.__extension == 'pdf':
            shutil.move(file_path, f'{self.__path}/pdf')
        elif self.__extension == 'doc':
            shutil.move(file_path, f'{self.__path}/doc')
        elif self.__extension == 'txt':
            shutil.move(file_path, f'{self.__path}/txt')
        elif self.__extension == 'zip':
            shutil.move(file_path, f'{self.__path}/WinRAR ZIP archive')
