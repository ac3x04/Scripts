#!/usr/bin/python3

"""
This script is used to generate all the metadata of a script file
"""
__author__ = "Ace Xor"
__copyright__ = "Copyright 2023"
__credits__ = ["The internet"]
__license__ = "GPL"
__maintainer__ = "Ace Xor"
__email__ = "ac3x04@gmail.com"
__status__ = "Dev"
__version__ = "0.0.1"


import sys
from datetime import datetime

scriptName = str(sys.argv[1])
with open(scriptName, "x") as file:
    file.write('#!<enter your execute path here>\n\n')
    file.write('"""\n<These are comments explaining what the script is and what it will do>\n"""\n')
    file.write('__author__ = "Ace Xor"\n')
    file.write('__copyright__ = "Copyright {}"\n'.format(datetime.now().year))
    file.write('__credits__ = ["<credits here>"]\n')
    file.write('__license__ = "GPL"\n')
    file.write('__maintainer__ = "Ace Xor"\n')
    file.write('__email__ = "ac3x04@gmail.com"\n')
    file.write('__status__ = "Dev"\n')
    file.write('__version__ = "0.0.1"\n')
    file.write('__language__ = "<language here>"\n\n')