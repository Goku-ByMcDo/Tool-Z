from colorama import * 
import os

banner = """
   _____           _      _____
  |_   _|__   ___ | |    |__  /
    | |/ _ \ / _ \| |_____ / / 
    | | (_) | (_) | |_____/ /_ 
    |_|\___/ \___/|_|    /____|

"""

def sqlmap_download():
    try:
        os.system('cls')
        os.system('title Tool-Z')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.GREEN + " * " + Fore.RESET + "Installation de SQLMAP")
        try:
            os.system('git clone https://github.com/sqlmapproject/sqlmap.git')
            print(Fore.GREEN + " * " + Fore.RESET + "SQLMAP installer avec succès !")
            input("")
        except:
            print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue lors de du clone de SQLMAP...")
            input("")
    except:
        print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue lors du clone de SQLMAP")
        input("")
