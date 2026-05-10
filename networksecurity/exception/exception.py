import sys

from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message,error_detail:sys):
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        

    def __str__(self):
        return "Error occured in python script name [{0}] at line number [{1}] error message [{2}]".format(
            self.file_name,self.lineno,self.error_message)   

if __name__ == "__main__":
    try:
        logger.logging.info("This is an info message")
        a = 1/0
    except Exception as e:
        logger.logging.error("An error occurred")
        raise NetworkSecurityException(e,sys)
     

  