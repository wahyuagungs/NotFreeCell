from enum import Enum


class Color(Enum):
    """
    This class uses enum as its base class, for constructing properties inside of its class
    that will allow any implementation avoid any unnecessarily mistakes, and any code repetition
    """
    BLACK = '\033[30m'
    RED = '\033[31m'
    NEUTRAL = '\033[0m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
