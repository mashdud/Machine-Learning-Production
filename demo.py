from us_visa.exception import USvisaException

import sys

try:
    x = 1 / 0  # Division by zero error
except Exception as e:
    raise(e,sys)
