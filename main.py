import argparse
from admin import *

# Argument parser for command line inputs
parser = argparse.ArgumentParser(description='Select the mode for update_dict')
parser.add_argument('-a', '--admin', dest = 'admin', action='store_true', 
                    help='enable admin to manage bank accounts.')
args = parser.parse_args()

MODE_ADMIN = args.admin
