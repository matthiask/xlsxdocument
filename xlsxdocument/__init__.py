VERSION = (1, 1, 0)
__version__ = '.'.join(map(str, VERSION))


try:
    # Convenience.
    from .document import XLSXDocument, export_selected  # noqa
except ImportError:
    pass
