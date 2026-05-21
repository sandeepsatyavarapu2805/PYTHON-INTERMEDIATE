import logging, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, 'test.log')

# for formatting logs look for log format attributes
# so for the newer python version the logger which is at default ROOT is accssed through '%(name)s'
logging.basicConfig(filename=filepath, level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

'''

DEBUG: Detailed information, typically of interest only when diagnosing problems.

INFO: Confirmation that things are working as expected.

WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. disk space low). The software is still working as expected.

ERROR: Due to a more serious problem, the software has not been able to perform some function.

CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

'''

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = subtract(num_1, num_2)
logging.debug(f"Add: {num_1} - {num_2} = {sub_result}")

mul_result = multiply(num_1, num_2)
logging.debug(f"Add: {num_1} * {num_2} = {mul_result}")

div_result = divide(num_1, num_2)
logging.debug(f"Add: {num_1} / {num_2} = {div_result}")