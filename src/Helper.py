import os
import shutil
import http.client as httplib
from os.path import join
from os.path import isabs
from urllib.parse import urlparse


class InputValidator:
    def __init__(self):
        self.criteria = {
            "file_type": True,
            "exist": True,
            "connection": True
        }
        self.is_okey = True

    def __del__(self):
        pass

    def validation(self, inp):
        (src, on_web, file_type) = inp

        if file_type not in Properties.supported_file_types:
            self.criteria["file_type"] = False
        if on_web:
            if self.__internet_on():
                if not self.__on_web(src):
                    self.criteria["exist"] = False
                    self.is_okey = False
            else:
                self.criteria["connection"] = False
                self.is_okey = False
        else:
            if not os.path.isfile(src):
                self.criteria["exist"] = False
                self.is_okey = False

        return self.is_okey

    def __internet_on(self):
        return self.__connect(Properties.referance_url, "/")

    def __connect(self, url, path):
        conn = httplib.HTTPConnection(url, timeout=5)
        try:
            conn.request("HEAD", path)
            conn.close()
            return True
        except:
            conn.close()
            return False

    def __on_web(self, url):
        return self.__connect(url, urlparse(url, ).path)


class Properties:
    debug = True

    supported_file_types = [
        "pdf", "html", "txt"
    ]

    error_messages = {
        "unsupported_file_type": "\nError: Unsupported file type! Please enter a valid file type!"
    }

    referance_url = "www.google.com"

    zemberek_path: str = join('Dependencies', 'Zemberek-Python', 'bin', 'zemberek-full.jar')

    error_file_name = "Errors.txt"

    def __init__(self):
        pass

    def __del__(self):
        pass


def rm_r(self, path):
    if os.path.isdir(path) and not os.path.islink(path):
        shutil.rmtree(path)
    elif os.path.exists(path):
        os.remove(path)


def chunk_size(self):
    return 8192
