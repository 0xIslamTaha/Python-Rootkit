import os
import time
import tempfile
import shutil

#open photos
os.startfile('test.jpg')
time.sleep(1)
os.startfile('test.jpg')

# copy file to temp
tempDirectory = tempfile.gettempdir()
shutil.copy('test.jpg',tempDirectory)