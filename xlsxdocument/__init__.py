VERSION = (1, 2, 0)
__version__ = '.'.join(map(str, VERSION))


try:
    # Convenience.
    from .document import *  # noqa
except ImportError:
    pass
