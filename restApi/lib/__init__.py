""" Lib """

LIBS_PATH = "../vendored"

# add vendored folder to sys path
import sys, os
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, LIBS_PATH))

# Manually load OS libraries
# ref: https://serverlesscode.com/post/deploy-scikitlearn-on-lamba/
import ctypes
for d, dirs, files in os.walk(LIBS_PATH):
    for f in files:
        if ".so" in f:
            ctypes.cdll.LoadLibrary(os.path.join(d, f))


# expose libraries in module scope
from single import single_all
from multi import multi_create, multi_show
from continent import continent_by_country_name