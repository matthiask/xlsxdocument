VERSION = (1, 3, 1)
__version__ = '.'.join(map(str, VERSION))


try:
    # Convenience.
    from .document import *  # noqa
except ImportError:
    pass
