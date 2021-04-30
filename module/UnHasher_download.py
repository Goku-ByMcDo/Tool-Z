from colorama import * 
import os

banner = """
   _____           _      _____
  |_   _|__   ___ | |    |__  /
    | |/ _ \ / _ \| |_____ / / 
    | | (_) | (_) | |_____/ /_ 
    |_|\___/ \___/|_|    /____|

"""

def UnHasher_download():
    try:
        os.system('cls')
        os.system('title Tool-Z')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.GREEN + " * " + Fore.RESET + "Installation de UnHasher")
        try:
            os.system('git clone https://github.com/KanekiX2/UnHasher.git')
            print(Fore.GREEN + " * " + Fore.RESET + "UnHasher installer avec succès !")
            input("")
        except:
            print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue lors de du clone de UnHasher...")
            input("")
    except:
        print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue lors du clone de UnHasher")
        input("")
