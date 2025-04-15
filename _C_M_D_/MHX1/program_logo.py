import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _C_M_D_.MHX1.colour import *
from _C_M_D_.MHX2.dynamic import version

logomrmhx='''
'''+green+''' __  __   ____            __  __   _   _  __  __
'''+red+'''|  \/  | |  _ \          |  \/  | | | | | \ \/ /
'''+cyan+'''| |\/| | | |_) |  _____  | |\/| | | |_| |  \  / 
'''+yellow+'''| |  | | |  _ <  |_____| | |  | | |  _  |  /  \ 
'''+blue+'''|_|  |_| |_| \_\         |_|  |_| |_| |_| /_/\_\
'''+purple+'''                                                
'''+version+'''
'''+reset_colour+'''
'''