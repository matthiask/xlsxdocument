VERSION = (1, 3, 8)
__version__ = ".".join(map(str, VERSION))


try:
    # Convenience.
    from .document import *  # noqa
except ImportError:
    pass
