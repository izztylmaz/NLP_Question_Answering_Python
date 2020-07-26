import src.Helper as helper
from src.data_receiving.InputValidator import InputValidator
from src.Helper import Properties
from src.data_receiving.DataReceiver import DataReceiver
from src.pre_processing.PreProcessor import PreProcessor as pp


def main():
    ###########################
    """ INPUT VALIDATION """  #
    #####################################################################################

    file_name = input("Enter file: ")
    on_web = input("Is file on the web(yes/no): ").lower() == 'yes'
    file_type = input(
        "Please Enter file type " + "Supported file types are -> " + ", ".join(
            Properties.supported_file_types) + " : ").lower()

    input_validator = InputValidator()
    input_validator.validation((file_name, on_web, file_type))

    # print(input_validator.is_okey)
    if not input_validator.is_okey:
        # print("ERROR\nProblems:")
        # print([cr for cr, st in input_validator.criteria.items() if not st])
        return
    #####################################################################################

    #########################
    """ DATA RECEIVING """  #
    #####################################################################################
    receiver = DataReceiver(file_name, on_web, file_type)
    receiver.receive()
    """ PRE-PROCESSING """


if __name__ == '__main__':
    main()
