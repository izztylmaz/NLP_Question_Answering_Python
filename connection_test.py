from src.Helper import Properties
import os
from urllib.parse import urlparse


def internet_on(hostname):
    return True if os.system("ping -c 1 " + hostname) == 0 else False


print(internet_on("stackoverflow.com"))
print("https://stackoverflow.com/questions/2535055/check-if-remote-host-is-up-in-python")
print(urlparse("https://stackoverflow.com/questions/2535055/check-if-remote-host-is-up-in-python").netloc)
