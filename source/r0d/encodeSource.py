import base64
import subprocess
import tempfile
import _winreg
import platform
import time
import os
import socket
import urllib

source = ''
with open('source.py','r') as file:
    for line in file:
        #byPass imprt commands
        if "import" in line:
            pass
        else:
            source += line
encode = base64.b64encode(source)
exec (base64.b64decode(encode))