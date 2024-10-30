#deals with the errors and raises custom exception
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent)) #to prevent error : no module named
# from exception import CustomException
from logger import logging #no need to define the module name, can directly access as already specifies in line 3
def error_msg_detail(error,error_detail:sys): 
    _,_,exc_tb=error_detail.exc_info() # provides the details about the error , file name and all that
    file_name=exc_tb.tb_frame.f_code.co_filename #provides the filename where error occured
    error_message="Error occured at [{0}], line no [{1}], error message [{2}]".format(
        file_name, exc_tb.tb_lineno,str(error))
    return error_message
       
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_msg_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message

    