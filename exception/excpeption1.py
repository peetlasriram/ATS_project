import sys
import logging 


def error_message_details(error,error_details:sys):
    _,_,exc_tab=error_details.exc_info()
    file_name=exc_tab.tb_frame.f_code.co_filename
    error_mess="error occured in the python script[{0}] and line number[{1}]and error message[{2}]".format(file_name,exc_tab.tb_lineno,str(error))
    return error_mess


class CustomException(Exception):
    def __init__(self,message,error_detail:sys):
        super().__init__(message)
        self.messgae=error_message_details(message,error_details=error_detail)
        
        
    def __str__(self):
        return self.messgae