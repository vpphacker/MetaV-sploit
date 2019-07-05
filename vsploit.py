import os
import time
import sys

print("\033[92m ")
os.system("clear")
os.system("figlet MSFInstall")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5.9 / 100)
print("\033[93m+------------------------------------------------+")
slowprint("|         Install MSF Without No Errors          |")
print("+------------------------------------------------+")
print('''\033[95m

[*] Unstable Repo
[*] x11 Repo
[*] Metasploit Framework''')
print("\033[91m                      ")
print("*********************************************")
slowprint("|               [!] Note [!]                |")
print("|                                           |")
slowprint("[!] Do Not Install Any Bash tool or script  |")
slowprint("[!] If You Install Bash Script              |")
slowprint("[!] You Face Too Many Erros                 |")
slowprint("[!] This is best way to Install MSF         |")
slowprint("[!] If you got error then                   |")
slowprint("[!] contact Me on Instagram: VPP Hacker     |")
slowprint("[!] Msf Need 600mb Space and Data first time|")
print("*********************************************")

slowprint('''\033[96m
[01] Install
[02] Exit ''')
print("       ")
z = input("\033[97mEnter Your Choice : ")

if (z == 1) :
             os.system("clear")
             slowprint("[#] Collecting Data................................")
             slowprint("[#] Installing ....................................")
             os.system("apt update")
             os.system("apt upgrade -y")
             os.system("figlet Repo Installing")
             os.system("apt install unstable-repo -y")
             os.system("apt install x11-repo -y")
             os.system("figlet Complete")
             os.system("figlet MSF Installing")
             os.system("apt install metasploit -y")
             os.system("figlet MSF Install")
             slowprint("[*]Starting Metasploit Framework Console..............")
             os.system("msfconsole")

if (z == 2) :
             slowprint("\033[93mSee You Next Time")
             sys.exit()
