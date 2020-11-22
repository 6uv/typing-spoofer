import requests
from colorama import Fore, init
import os
init(convert=True)

intro = """
                    Made by REZIZT. I already know your skidding this just admit it
                            Discord : https://discord.gg/XgpXMWk2bG
                ▄▄▄█████▓▓██   ██▓ ██▓███  ▓█████   ██████  ██▓███   ▒█████   ▒█████    █████▒
                ▓  ██▒ ▓▒ ▒██  ██▒▓██░  ██▒▓█   ▀ ▒██    ▒ ▓██░  ██▒▒██▒  ██▒▒██▒  ██▒▓██   ▒ 
                ▒ ▓██░ ▒░  ▒██ ██░▓██░ ██▓▒▒███   ░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒██░  ██▒▒████ ░ 
                ░ ▓██▓ ░   ░ ▐██▓░▒██▄█▓▒ ▒▒▓█  ▄   ▒   ██▒▒██▄█▓▒ ▒▒██   ██░▒██   ██░░▓█▒  ░ 
                  ▒██▒ ░   ░ ██▒▓░▒██▒ ░  ░░▒████▒▒██████▒▒▒██▒ ░  ░░ ████▓▒░░ ████▓▒░░▒█░    
                  ▒ ░░      ██▒▒▒ ▒▓▒░ ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ░    
                    ░     ▓██ ░▒░ ░▒ ░      ░ ░  ░░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░   ░ ▒ ▒░  ░      
                  ░       ▒ ▒ ░░  ░░          ░   ░  ░  ░  ░░       ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░    
                          ░ ░                 ░  ░      ░               ░ ░      ░ ░          
                          ░ ░                                                                


                                            [+]1 Typing spoof
                                            
"""

def type():
    print(f'[{Fore.RED}>{Fore.RESET}] Your token', end=''); token = str(input('  :  '))
    print(f'[{Fore.RED}>{Fore.RESET}] Channel id', end=''); channel = str(input('  :  '))
    headers = {'Authorization': token}
    print('starting typing...')
    while True:    
        requests.post(f'https://discordapp.com/api/v6/channels/{channel}/typing', headers=headers)




def startMenu():
    print(intro)
    print(f'[{Fore.RED}>{Fore.RESET}] Your choice', end=''); choice = str(input('  :  '))
    if choice == '1':
       os.system('cls')
       type()

if __name__ == '__main__':
    startMenu()