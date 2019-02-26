import sys, os
from cx_Freeze import setup, Executable

__version__ = "2.1.0"

include_files = ['autosave.lkm', 'icon.ico', 'LKMini.gif', r"C:\Program Files (x86)\Python37-32\DLLs\tcl86t.dll", r"C:\Program Files (x86)\Python37-32\DLLs\tk86t.dll"]
packages = ["tkinter", "mido", "ast","sys"]
os.environ['TCL_LIBRARY'] = r'C:\Program Files (x86)\Python37-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files (x86)\Python37-32\tcl\tk8.6'

setup(
    name = "Launchkey Mini Pad Coloring Tool",
    description='Tool for configuring the pad colors on the Launchkey Mini',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'include_msvcr': True,
}},
executables = [Executable("LKMedit.py",base="Win32GUI")]
)
