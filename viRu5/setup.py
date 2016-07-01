from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')

includes = ["win32crypt"]
dll_excludes=["Crypt32.dll"]


setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True,'dll_excludes': dll_excludes,'includes': includes}},
    windows = [{'script': "GoogleChromeAutoLaunch.py","icon_resources": [(0, "icon.ico")]}],
    zipfile = None,
)