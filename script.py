import keyboard
import time
import os
from colorama import Fore, Back, Style

# ----------------------------------- #

os.system("cls")

keyboard.press('f11')
print("")
print("")
print("")
print('Atualização do Sistema - ATC Informática (62) 3357-3105'.center(150))
print('O Sistema Está Atualizando...'.center(150))
print("")
print("")
print("")
print("")

print("[!] Iniciando Download dos Arquivos Necessários...".center(150))
time.sleep(100)
print("[!] Iniciando Instalação da Atualização...".center(150))
time.sleep(500)
print("[+] Instalação Concluída!".center(150))
print("[!] Sistema será reinicializado em alguns instantes...".center(150))
time.sleep(10)

os.system("reboot now")
os.system("shutdown -t 0 -r -f")
