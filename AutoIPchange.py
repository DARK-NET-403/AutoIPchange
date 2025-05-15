#Tool Make By : Ariyan Rabbi(Dʌʀĸ-Nɘt)
#Don't Use My coded File And copy
#Are Your use copy my file Your Father 100 man
#use this tool and give me star
#Don't Copy my file

import os
import time
import requests
from stem import Signal
from stem.control import Controller
from colorama import Fore, Style, init
import pyfiglet
import random

# Initialize colorama
init(autoreset=True)

# Banner
def banner():
    os.system("clear" if os.name == "posix" else "cls")
    ascii_banner = pyfiglet.figlet_format("AutoIPchange")
    print(Fore.CYAN + ascii_banner)
    print(Fore.MAGENTA + "  Coded by: Ariyan Rabbi (Dʌʀĸ-Nɘt)")
    print(Fore.YELLOW + "  FB: facebook.com/share/12Ju91Lznxb/")
    print(Fore.YELLOW + "  TG: t.me/DARK_NET_40")
    print(Fore.YELLOW + "  GH: github.com/DARK-NET-403\n")
    print(Fore.GREEN + "[*] Auto Tor IP Changer Tool Running...\n")

# Get current IP
def get_ip():
    try:
        r = requests.get('http://icanhazip.com', proxies={"http": "socks5h://127.0.0.1:9050",
                                                           "https": "socks5h://127.0.0.1:9050"})
        return r.text.strip()
    except:
        return "Error: Tor not running!"

# Change IP
def change_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="torpassword")  # <-- Edit this if needed
            controller.signal(Signal.NEWNYM)
    except Exception as e:
        print(Fore.RED + f"[!] Failed to change IP: {e}")

# Main loop
def main():
    banner()
    interval = input(Fore.CYAN + "[+] Enter time interval in minutes to change IP: ")

    try:
        interval = int(interval)
    except:
        print(Fore.RED + "[!] Invalid input. Use numbers only.")
        return

    while True:
        print(Fore.BLUE + f"\n[•] Checking current IP...")
        ip = get_ip()
        print(Fore.GREEN + f"[✓] Your current IP is: {ip}")

        print(Fore.YELLOW + f"\n[!] Waiting {interval} minutes before changing IP...")
        time.sleep(interval * 60)

        print(Fore.MAGENTA + "[#] Changing IP using Tor...")
        change_ip()
        time.sleep(5)  # Give Tor a moment to change

        new_ip = get_ip()
        print(Fore.GREEN + f"[✓] New IP: {new_ip}")
        print(Fore.CYAN + "-" * 50)

# Start
if __name__ == "__main__":
    main()
