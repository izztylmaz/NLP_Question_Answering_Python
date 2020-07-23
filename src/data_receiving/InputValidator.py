from ..Helper import Properties
from urllib.parse import urlparse
import os
import requests


class InputValidator:
    def __init__(self):
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
        (src, on_web, file_type) = inp

        if file_type not in Properties.supported_file_types:
            self.criteria["file_type"] = False
        if on_web:
            if self.__internet_on():
                if not self.__on(urlparse(src).netloc):
                    self.criteria["website_available"] = False
                    self.criteria["exist"] = False
                    self.is_okey = False
                elif not self.__page_available(src):
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

    def __on(self, host_name):
        return True if os.system("ping -c 1 " + host_name) == 0 else False

    def __internet_on(self):
        return self.__on(Properties.referance_url)

    def __page_available(self, url):
        request = requests.get(url)
        return request.status_code < 400
