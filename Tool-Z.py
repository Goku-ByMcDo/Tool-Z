import os
try:
    print("Installing requirements...")
    os.system('pip install colorama >nul')
    os.system('pip install art >nul')
    input("Requirements install successfully, press enter to continue")
except:
    print(" ! An error occurred while installing the requirements please use this command in a cmdpip install colorama, pip install art")
    input("")



# REQUIREMENTS


from colorama import *
import os
from art import * 
from module.sqlmap_download import *
from module.littlebrother_downlaod import * 
from module.email_osint import *
from module.daprofiler_download import *
from module.nmap_download import *
from module.UnHasher_download import * 
from module.keylogger_download import *
from module.proxytools_download import *
from module.webhook_spammer_download import *

from other.discord_choice import *





banner = """
   _____           _      _____
  |_   _|__   ___ | |    |__  /
    | |/ _ \ / _ \| |_____ / / 
    | | (_) | (_) | |_____/ /_ 
    |_|\___/ \___/|_|    /____| Version bêta

"""

categorie_download = """
       [1] - Discord
       [2] - Web
       [3] - Dox
       [4] - Cracking
 


"""
catego_discord = """
       [1] - Webhook Spammer
       [2] - KeyLogger
"""

catego_dox = """
       [1] - LittleBrother
       [2] - DaProfiler
       [3] - Email-Osint
"""
catego_web = """
       [1] - SQLMAP
       [2] - nmap
"""

catego_crack = """
       [1] - SQLMAP
       [2] - nmap
"""

all_download_banner = """
       [1] - LittleBrother
       [2] - DaProfiler
       [3] - Email Osint
       [4] - SQLMAP
       [5] - nmap
       [6] - UnHasher
       [7] - KeyLogger
       [8] - ProxyTools
       [9] - Webhook Spammer
 
 """

tool_banner = """
       [1] - All download
       [2] - catégorie
       [c] - clear
       [e] - exit
 """


# PARTIE DOWNLOAD ALL


def all_download():
    choice_all = input("/"+Fore.RED+"~"+Fore.RESET+"> ")

    # ALL DONWLOAD CHOCIE
    try:
        if choice_all == "1":
            littlebrother_download()

        elif choice_all == "2":
            DaProfiler_download()

        elif choice_all == "3":
            EmailOsint_download()

        elif choice_all == "4":
            sqlmap_download()

        elif choice_all == "5":
            nmap_download()

        elif choice_all == "6":
            UnHasher_download()

        elif choice_all == "7":
            KeyLogger_download()
        
        elif choice_all == "8":
            ProxyTools_download()

        elif choice == "9":
            Webhook_Spammer_download()
        
        else:
            print(Fore.RED + " ! Message ! " + Fore.RESET + "Veuillez choisir un nombre attribuer a un logiciel")
    except:
        print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue lors du choix ! ")
                





# MENU

def menu():
    os.system('cls')
    os.system('title Tool-Z')
    print(Fore.BLUE + banner + Fore.RESET)
    print(Fore.MAGENTA + tool_banner + Fore.RESET)
    choice = input("/"+Fore.RED+"~"+Fore.RESET+"> ")

    # CHOICE

    if choice == "1":
        os.system('cls')
        os.system('title Tool-Z')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.MAGENTA + all_download_banner + Fore.RESET)
        all_download()

    elif choice == "2":
        os.system('cls')
        os.system('title Tool-Z')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.MAGENTA + categorie_download + Fore.RESET)
        catego_choice = input("/"+Fore.RED+"~"+Fore.RESET+"> ")

        if catego_choice == "1":
            catego__discord()
            
    
    elif choice == "c":
        os.system('cls')
        menu()

    elif choice == "e":
        print(Fore.BLUE + banner + Fore.RESET)
        os.system('exit')

    else:
        print(Fore.RED + " ! " + Fore.RESET + "Veuillez entrez une commande valide...")
        input("")
menu()