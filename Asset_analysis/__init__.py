import os
from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
print "This is the value of modules: " +modules
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not os.path.basename(f).startswith('_')]
print "This is the value of __all__: " +__all__