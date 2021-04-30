banner = """
   _____           _      _____
  |_   _|__   ___ | |    |__  /
    | |/ _ \ / _ \| |_____ / / 
    | | (_) | (_) | |_____/ /_ 
    |_|\___/ \___/|_|    /____|

"""

def EmailOsint_download():
    os.system('cls')
    os.system('title Tool-Z')
    print(Fore.BLUE + banner + Fore.RESET)
    print(Fore.GREEN + " * "+ Fore.RESET + "Installation de Email-Osint")
    try:
        os.system('git clone https://github.com/KanekiX2/Email-Osint.git >nul')
        os.system('cls')
        print(Fore.BLUE + banner + Fore.RESET)
        print(Fore.GREEN + " * " + Fore.RESET + "Email-Osint installer avec succès")
        input("")
    except:
            print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue à l'installation de Email-Osint")
            input("")