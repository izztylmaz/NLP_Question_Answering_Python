class DataReceiver:
    def __init__(self, data_address, on_web, data_type):
        self.raw_text = str()
        self.src = data_address
        self.on_web = on_web
        self.type = data_type

    def __del__(self):
        pass

    def receive(self):
        if self.on_web:
            self.__download()
        else:
            pass

    def __download(self):
        pass
