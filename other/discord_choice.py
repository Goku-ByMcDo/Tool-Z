from colorama import *
import os
from module.webhook_spammer_download import *
from module.keylogger_download import * 
banner = """
   _____           _      _____
  |_   _|__   ___ | |    |__  /
    | |/ _ \ / _ \| |_____ / / 
    | | (_) | (_) | |_____/ /_ 
    |_|\___/ \___/|_|    /____|

"""

catego_discord = """
       [1] - Webhook Spammer
       [2] - KeyLogger
"""

def catego__discord():
    try:
        os.system('cls')
        os.system('title Tool-Z')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.MAGENTA + catego__discord + Fore.RESET)
        discord_choice = input("/"+Fore.RED+"~"+Fore.RESET+"> ")

        if discord_choice == "1":
            Webhook_Spammer_download()
        
        elif discord_choice == "2":
            KeyLogger_download()
        
        else:
            print(Fore.RED +" ! " + Fore.RESET + "Veuillez choisire un nombre correcte...")
            input("")


    except:
        print(Fore.RED + " ! "+Fore.RESET +"Une erreur est survenue lors des l'affichage des la catégorie discord...")
        input("")
