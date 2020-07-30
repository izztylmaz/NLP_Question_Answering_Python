import src.Helper
from src.data_receiving.InputValidator import InputValidator
from src.Helper import Properties
from src.data_receiving.DataReceiver import DataReceiver
from src.pre_processing.PreProcessor import PreProcessor


def main():
    ###########################
    """ INPUT VALIDATION """  #
    #####################################################################################

    file_address = input("Enter file: ")
    # on_web = input("Is file on the web(yes/no): ").lower() == 'yes'
    # file_type = input(
    #     "Please Enter file type " + "Supported file types are -> " + ", ".join(
    #         Properties.supported_file_types) + " : ").lower()
    # file_address = "data/test.txt"
    file_type = "html"
    on_web = True

    input_validator = InputValidator()
    input_validator.validation((file_address, on_web, file_type))

    # print(input_validator.is_okey)
    if not input_validator.is_okey:
        # print("ERROR\nProblems:")
        # print([cr for cr, st in input_validator.criteria.items() if not st])
        return
    #####################################################################################

    #########################
    """ DATA RECEIVING """  #
    #####################################################################################
    receiver = DataReceiver(file_address, on_web, file_type)
    data_inf = receiver.receive()
    if not data_inf:
        print("empty")
        return
    raw_data, file_name = data_inf
    #####################################################################################

    #########################
    """ PRE-PROCESSING """  #
    #####################################################################################
    PreProcessor(raw_data, file_name, file_type)


if __name__ == '__main__':
    main()
