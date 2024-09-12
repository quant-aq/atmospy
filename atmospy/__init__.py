from importlib.metadata import version

import matplotlib as mpl

from .rcmod import *
from .relational import *
from .rose import *
from .stats import *
from .trends import *
from .utils import *

# Capture the original matplotlib rcParams
_orig_rc_params = mpl.rcParams.copy()

# Determine the atmospy version
__version__ = version("atmospy")
