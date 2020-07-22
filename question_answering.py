import src.Helper as helper
from src.Helper import InputValidator, Properties
from src.data_receiving.DataReceiver import DataReceiver
from src.pre_processing.PreProcessor import PreProcessor as pp


def main():

    ###########################
    """ INPUT VALIDATION """  #
    #####################################################################################

    file_name = input("Enter file: ")
    on_web = True if input("Is file on the web(yes/no)?").lower() == 'yes' else False
    file_type = input(
        "Please Enter file type " + "Supported file types are -> " + ", ".join(
            Properties.supported_file_types) + " : ").lower()

    input_validator = InputValidator()

    input_validator.validation((file_name, on_web, file_type))

    if input_validator.is_okey:
        print("OKAY")
    else:
        print("ERROR")
        print([cr for cr, st in input_validator.criteria.items() if not st])

    #####################################################################################

    """ DATA RECEIVING """
    #receiver = DataReceiver()


    """ PRE-PROCESSING """


if __name__ == '__main__':
    main()
