import requests
import os
from pathlib import Path
from src.Helper import Properties


class DataReceiver:
    def __init__(self, data_address, on_web, data_type):

        self.src = data_address
        self.on_web = on_web
        self.type = data_type

        self.raw_text = str()
        self.file_data_dir = os.getcwd() + "/data/file_data"
        self.file_name = self.make_name(data_address, on_web)

        print("File name is: {self.file_name}")

        exit(1)

        self.create_repository()

    def __del__(self):
        pass

    def receive(self):
        if self.on_web:
            try:
                data = self.__download()
                if data == -1:
                    print("ERROR")
            except:
                print("Error while downloading!")
        else:
            try:
                self.copy(self.src)
            except:
                print("Error while copying!")

    def __download(self):
        r = requests.get(self.file_name, allow_redirects=True)
        with open(self.file_data_dir + self.file_name, "wb") as f:
            f.write(r.content)
        return r.content

    def create_repository(self):
        Path(self.file_data_dir).mkdir(parents=True, exist_ok=True)
        self.file_data_dir += '/'

    def copy(self, src):
        r = requests.get(src, allow_redirects=True)
        if not r.content:
            print("EMPTY CONTENT")
            return -1
        else:
            with open(self.file_data_dir + self.file_name, "wb+") as f:
                f.write(r.content)
            print("COPIED!")
            return r.content

    def make_name(self, name, on_web):
        name = name.lower()
        if name[-1] == '/':
            name = name[:-1]
        if not name.endswith(tuple(Properties.supported_file_types)):
            name = name + '.' + self.type
        name = name.split('/')[-1] if on_web else os.path.basename(name)
        return name
