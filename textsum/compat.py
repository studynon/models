"""Only handel the compatibility of Python 2 & 3 for textsum
Usage:
Add the following code in the other scripts for the compatibility with Python 3,
'from compat import *'
Prerequisites:
For Python 3, you need "pip install future"
"""
import sys
if sys.version_info.major == 3:
    import queue as Queue
    from past.builtins import xrange # NEED pip install future
