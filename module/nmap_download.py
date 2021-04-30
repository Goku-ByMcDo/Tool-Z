banner = """
   _____           _      _____
  |_   _|__   ___ | |    |__  /
    | |/ _ \ / _ \| |_____ / / 
    | | (_) | (_) | |_____/ /_ 
    |_|\___/ \___/|_|    /____|

"""

def nmap_download():
    os.system('cls')
    os.system('title Tool-Z')
    print(Fore.BLUE + banner + Fore.RESET)
    print(Fore.GREEN + " * "+ Fore.RESET + "Installation de nmap")
    try:
        os.system('git clone https://github.com/nmap/nmap.git >nul')
        os.system('cls')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.GREEN + " * " + Fore.RESET + "nmap installer avec succès")
        input("")
    except:
            print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue à l'installation de nmap")
            input("")