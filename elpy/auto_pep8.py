"""Glue for the "autopep8" library.

"""

from elpy.rpc import Fault
import os


try:
    import autopep8
except ImportError:  # pragma: no cover
    autopep8 = None


def fix_code(code, directory, linelength):
    """Formats Python code to conform to the PEP 8 style guide.

    """
    if linelength is None:
        linelength = 79
    if not autopep8:
        raise Fault('autopep8 not installed, cannot fix code.',
                    code=400)
    old_dir = os.getcwd()
    try:
        os.chdir(directory)
        options = {'max_line_length': linelength}
        return autopep8.fix_code(code, options=options, apply_config=True)
    finally:
        os.chdir(old_dir)
