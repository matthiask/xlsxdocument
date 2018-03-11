VERSION = (1, 3, 0)
__version__ = '.'.join(map(str, VERSION))


try:
    # Convenience.
    from .document import *  # noqa
except ImportError:
    pass
