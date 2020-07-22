from ..data_receiving import DataReceiver


def create_environment():
    pass


def pre_process(data_address, on_web, file_type):
    create_environment()

    receiver = DataReceiver.DataReceiver(data_address, on_web, file_type)


class PreProcessor:
    def __init__(self):
        pass

    def __del__(self):
        pass