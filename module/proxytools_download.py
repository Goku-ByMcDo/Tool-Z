from colorama import *
import os 


banner = """
   _____           _      _____
  |_   _|__   ___ | |    |__  /
    | |/ _ \ / _ \| |_____ / / 
    | | (_) | (_) | |_____/ /_ 
    |_|\___/ \___/|_|    /____|

"""

def ProxyTools_download():
    os.system('cls')
    os.system('title Tool-Z')
    print(Fore.BLUE + banner + Fore.RESET)
    print(Fore.GREEN + " * "+ Fore.RESET + "L'installation de ProxyTools est impossible car le créateur est en train de le re faire...")
    try:
        os.system('cls')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.GREEN + " * " + Fore.RESET + "ProxyTools installer avec succès")
        input("")
    except:
            print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue à l'installation de ProxyTools")
            input("")