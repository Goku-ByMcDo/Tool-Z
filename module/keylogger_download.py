from colorama import *
import os 


banner = """
   _____           _      _____
  |_   _|__   ___ | |    |__  /
    | |/ _ \ / _ \| |_____ / / 
    | | (_) | (_) | |_____/ /_ 
    |_|\___/ \___/|_|    /____|

"""

def KeyLogger_download():
    os.system('cls')
    os.system('title Tool-Z')
    print(Fore.BLUE + banner + Fore.RESET)
    print(Fore.GREEN + " * "+ Fore.RESET + "Installation de KeyLogger")
    try:
        os.system('git clone https://github.com/KanekiX2/KeyLogger.git >nul')
        os.system('cls')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.GREEN + " * " + Fore.RESET + "KeyLogger installer avec succès")
        input("")
    except:
            print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue à l'installation de KeyLogger")
            input("")