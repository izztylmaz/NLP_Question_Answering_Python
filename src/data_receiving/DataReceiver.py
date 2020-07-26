import os
import requests
from pathlib import Path
from src import Helper
from src.Helper import Properties


class DataReceiver:
    def __init__(self, data_address, on_web, data_type):
        Helper.debug("Data Receiving", 0, "situation")
        self.src = data_address
        self.on_web = on_web
        self.type = data_type

        self.raw_text = str()
        self.file_data_dir = os.getcwd() + "/data/file_data"

        self.file_name = self.make_name(data_address, on_web)
        Helper.debug("extract_name", True, "module_debug")

        print("\t\tFile name:", self.file_name)

        self.create_repository()
        Helper.debug("create_repository", True, "module_debug")
        print("\t\tRepository location:", self.file_data_dir)

    def __del__(self):
        pass

    def receive(self):
        Helper.debug("Data Receiving", 1, "situation")
        if self.on_web:
            try:
                data = self.__download()
                if not data:
                    Helper.debug("download_file", False, "module_debug")
                else:
                    Helper.debug("download_file", True, "module_debug")
            except:
                Helper.debug("download_file", False, "module_debug")
        else:
            try:
                self.copy(self.src)
                Helper.debug("copy_file", True, "module_debug")
            except:
                Helper.debug("copy_file", False, "module_debug")
        Helper.debug("Data receiving", 2, "situation")

    def __download(self):
        r = requests.get(self.src, allow_redirects=True)
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
            return False
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
