import logging, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, 'employee.log')

'''

It is good to use different logger which overwrites the ROOT
if we import employee_logging doc it runs when imported and employee.log is created but not test.log 
which is due to the log is not set seperately which is because the basicConfig is carried along

the logger basic config is not overwritten as per above which is made available for 3.8+ versions by,
logging.basicConfig(level=logging.DEBUG, force=True)

'''

logger = logging.getLogger(__name__) # we should use this in place of logging.info
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filepath) # we need to have this since logger does not write into the files directly but hands it to the file handler
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')

stream_handler = logging.StreamHandler() # this makes the log messages to appear in the console

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter) # first set the formatter to the file_handler before adding it to the logger
# file_handler.setLevel(logging.ERROR) this has more priority which will be stisfied before logger.setLevel(logging.INFO)

logger.addHandler(file_handler) # now after file_handler config we need to add it to the logger
logger.addHandler(stream_handler)

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logger.info(f'Created Employee: {self.first} - {self.last}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')

'''

x,y = 2,0
try:
    result = x / y
except ZeroDivisionError:
    logging.error(f'We cannot divide by i.e {x} cannot be divided by {y}')
else:
    return result

if i change logging.error to logging.exception then,
it also includes the traceback along with the log statement
    
''' 