import os
from pandos.version import Version

version = Version.from_path(name="toolbox", dirpath=os.path.dirname(__file__))
