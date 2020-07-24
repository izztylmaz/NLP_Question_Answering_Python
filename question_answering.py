import src.Helper as helper
from src.data_receiving import InputValidator
from src.Helper import Properties
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

    if not input_validator.is_okey:
        print("ERROR\nProblems:")
        print([cr for cr, st in input_validator.criteria.items() if not st])
        exit(1)
    print("VALIDATION DONE")

    #####################################################################################

    #########################
    """ DATA RECEIVING """  #
    #####################################################################################
    receiver = DataReceiver()

    """ PRE-PROCESSING """


if __name__ == '__main__':
    main()
