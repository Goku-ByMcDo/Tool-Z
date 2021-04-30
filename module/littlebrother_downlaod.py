from colorama import *
import os 


banner = """
   _____           _      _____
  |_   _|__   ___ | |    |__  /
    | |/ _ \ / _ \| |_____ / / 
    | | (_) | (_) | |_____/ /_ 
    |_|\___/ \___/|_|    /____|

"""

def littlebrother_download():
    os.system('cls')
    os.system('title Tool-Z')
    print(Fore.BLUE + banner + Fore.RESET)
    print(Fore.GREEN + " * "+ Fore.RESET + "Installation de LittleBrother")
    try:
        os.system('git clone https://github.com/lulz3xploit/LittleBrother.git >nul')
        os.system('cls')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.GREEN + " * " + Fore.RESET + "LittleBrother installer avec succès")
        input("")
    except:
            print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue à l'installation de LittleBrother")
            input("")