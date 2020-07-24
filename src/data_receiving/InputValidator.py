from ..Helper import Properties
from src import Helper
from urllib.parse import urlparse
import os
import requests
import subprocess


class InputValidator:
    def __init__(self):
        print("Input validation starting...")
        self.criteria = {
            "file_type": True,
            "exist": True,
            "internet_connection": True,
            "website_available": True,
        }

        self.is_okey = True

    def __del__(self):
        pass

    def validation(self, inp):
        print("Input validation started!")
        (src, on_web, file_type) = inp

        if file_type not in Properties.supported_file_types:
            self.criteria["file_type"] = False
            Helper.debug("file_type", False)
        else:
            Helper.debug("file_type", True)
        if on_web:
            if self.__internet_on():
                Helper.debug("internet_connection", True)
                if not self.__on(urlparse(src).netloc):
                    Helper.debug("website_available", False)
                    self.criteria["website_available"] = False
                    self.criteria["exist"] = False
                    self.is_okey = False
                elif not self.__page_available(src):
                    Helper.debug("website_available", True)
                    Helper.debug("file_exists", False)
                    self.criteria["exist"] = False
                    self.is_okey = False
                else:
                    Helper.debug("website_available", True)
                    Helper.debug("file_exists", True)
            else:
                Helper.debug("internet_connection", False)
                self.criteria["connection"] = False
                self.is_okey = False
        else:
            if not os.path.isfile(src):
                Helper.debug("file_exist", False)
                self.criteria["exist"] = False
                self.is_okey = False

        return self.is_okey

    def __on(self, host_name):
        # if Properties.DEBUG:
        #     return os.system("ping -c 1 " + host_name) == 0
        with open(os.devnull, 'w') as DEVNULL:
            try:
                subprocess.check_call(
                    ['ping', '-c', '1', host_name],
                    stdout=DEVNULL,
                    stderr=DEVNULL
                )
                return True
            except subprocess.CalledProcessError:
                return False
        # return True if os.system("ping -c 1 " + host_name) == 0 else False

    def __internet_on(self):
        return self.__on(Properties.referance_url)

    def __page_available(self, url):
        request = requests.get(url)
        return request.status_code < 400
