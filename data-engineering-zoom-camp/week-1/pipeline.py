import pandas as pd
import sys

# print the arguments passed to the command line command
print(sys.argv)

# get the first argument passed to the command line command
day = sys.argv[1]

# some fancy stuff with pandas
print(f'job finished successfully for day = {day}')