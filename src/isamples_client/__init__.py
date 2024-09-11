# ISBClient is the main class to interact
# with the iSamples API
import importlib

# ISBClient has an __ALL__ list of all the classes
# import all variables from __ALL__ list

from .isbclient import __ALL__

# Dynamically import all classes listed in __ALL__
for class_name in __ALL__:
    globals()[class_name] = getattr(importlib.import_module('.isbclient', package=__name__), class_name)