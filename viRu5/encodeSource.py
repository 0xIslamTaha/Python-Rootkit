import base64

source = ''
with open('source.py','r') as file:
    for line in file:
        #byPass imprt commands
        if "import" in line:
            pass
        else:
            source += line

encode = base64.b64encode(source)
for i in xrange(9):
    encode = base64.b64encode(encode)

print(encode)