import logging
from logging import config

def logging_function():
    """A function which prints and log info. No return value"""
    
    print("\nIn Logging Function ",logging_function)
    print("logging: ",logging,flush=True)
    logger = logging.getLogger()
    print('logger without name: %s ID: %s'%(logger,id(logger)),flush=True)
    logger.warning('Warning raised by logger')
    logger = logging.getLogger(__name__)
    print("logger %s called with name \033[1;31m%s\033[1;0m, ID: %s" %(logger,__name__,id(logger)),flush=True)
    logger.warning('Warning raised by logger')




def start_logger(logger = None,cfgfile=None):

    #if logger exists (this is based only in checking it has any handler) 
    # recover the current logger without adding handlers, if not load from file
    #  or if config file is not provided, uses default options for logger
       
    print("N: ",__name__) # qui mostra non serve perche sara start_logger    
    if logger is None:
        print("logger non defined, get one.")       
        logger=logging.getLogger()
    else:
        print("logger existing")
              
    print("logger %s, ID: %s" %(logger,id(logger)))

    if len(logger.handlers) == 0:
        """not sure about original indentation here."""   
        print("logger has no handlers.")
        if cfgfile is not None:
            print("Read logger settings from conf file ",cfgfile)
            logger=logging.config.fileConfig(cfgfile)
        else:
            print("conf file not defined, use default")
            logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',force=True)  #set default   
            print('logger: ',logger,' ID: ',id(logger))
            #print('cfgfile missing, and no logger existing, not sure what happens now.')
            
    return logger

def reset_logger(logger, full=False):
    """ close all handlersr in place. 
        If full is set, logger is also shutdown (cannot be used after this without
        being reinitialized). This strictly needs to be done only after program execution."""
        
    for h in logger.handlers:
        h.close()
    if full: 
        logger.handlers.clear()
        logger.shutdown()

# legacy        
class Logger():
    
    #methods that mimic the behavior of logging.Logger
    def info(self,msg):
        print (msg)
    def debug(self,msg):
        print(msg)
        


cfgfile='logging.ini'

'''
# from http://techies-world.com/how-to-redirect-stdout-and-stderr-to-a-logger-in-python/
# To redirect stdout and stderr to a logger, use the following snippet.
# 

class StreamToLogger(object):
      """
      Fake file-like stream object that redirects writes to a logger instance.
      """
      def __init__(self, logger, log_level=logging.INFO):
            self.logger = logger
            self.log_level = log_level
            self.linebuf = ''

      def write(self, buf):
            for line in buf.rstrip().splitlines():
                  self.logger.log(self.log_level, line.rstrip())

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
filename="out.log",
filemode='a'
)

stdout_logger = logging.getLogger('STDOUT')
sl = StreamToLogger(stdout_logger, logging.INFO)
sys.stdout = sl

stderr_logger = logging.getLogger('STDERR')
sl = StreamToLogger(stderr_logger, logging.ERROR)
sys.stderr = sl

print "Test to standard out"
raise Exception('Test to standard error')

'''


