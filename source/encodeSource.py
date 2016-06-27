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
        source += line
encode = base64.b64encode(source)
print encode
exec (base64.b64decode(encode))