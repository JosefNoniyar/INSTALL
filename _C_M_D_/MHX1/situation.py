# Import All Colours
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _C_M_D_.MHX1.colour import *

# Situation Veriables Definition
ask = cyan + '\n[' + white + '?' + cyan + '] '+ yellow
success = cyan + '\n[' + white + '√' + cyan + '] '+ green
error = cyan + '\n[' + white + 'X' + cyan + '] '+ red
advice = cyan + '\n[' + white + '!' + cyan + '] '+ yellow
pw = cyan + '\n[' + white + '+' + cyan + ']'+' Please Wait...'