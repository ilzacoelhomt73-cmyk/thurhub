
import hashlib
import textwrap
import os
from getpass import getpass
import time
import sys
import subprocess
import platform

sistema = 0

HASH_ESPERADO = "3669e7add5d311474d0dd3c6e6020163d99c610af9519ad0194158e96d1f7f10"

comando_vscode_debian = (
    "sudo apt update -y && "
    "sudo apt install gnome-keyring -y && "
    "sudo apt install -y wget gpg && "
    "wget -qO- https://packages.microsoft.com/keys/microsoft.asc "
    "| gpg --dearmor "
    "| sudo tee /usr/share/keyrings/microsoft.gpg > /dev/null && "
    "echo 'deb [arch=amd64,arm64,armhf "
    "signed-by=/usr/share/keyrings/microsoft.gpg] "
    "https://packages.microsoft.com/repos/code stable main' "
    "| sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null && "
    "sudo apt update -y && "
    "sudo apt install -y code && "
    "code"
)

comando_zphisher_debian = (
    "sudo apt update -y && "
    "sudo apt upgrade -y && "
    "sudo apt install git -y && "
    "git clone https://github.com/htr-tech/zphisher.git && "
    "cd zphisher && bash zphisher.sh"
)

comando_zphisher_termux = (
    "pkg update -y && "
    "pkg upgrade -y && "
    "pkg install git -y && "
    "git clone https://github.com/htr-tech/zphisher.git && "
    "cd zphisher && bash zphisher.sh"
)

comando_kahoot_termux = (
    "pkg update -y && "
    "pkg upgrade -y && "
    "pkg install -y git python python-pip nodejs npm && "
    "python -m pip install pystyle colorama && "
    "git clone https://github.com/CPScript/Kitty-Tools && "
    "cd Kitty-Tools && "
    "python main.py"
)

comando_kahoot_debian = (
    "sudo apt update -y && "
    "sudo apt upgrade -y && "
    "sudo apt install -y git python3-pip nodejs npm && "
    "python3 -m pip install --break-system-packages pystyle colorama && "
    "git clone https://github.com/CPScript/Kitty-Tools && "
    "cd Kitty-Tools && python3 main.py"
)

AZUL = "\033[34m"
AZUL_FORTE = "\033[1;34m"
CIANO = "\033[36m"
CIANO_MERDA = "\033[96m"
CIANO_FORTE = "\033[1;36m"
MAGENTA = "\033[35m"
MAGENTA_FORTE = "\033[1;35m"
AMARELO = "\033[33m"
AMARELO_FORTE = "\033[1;33m"
BRANCO_FORTE = "\033[1;37m"
BRANCO = "\033[37m"
VERDE_FORTE = "\033[1;32m"
VERMELHO_FORTE = "\033[1;31m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
RESET = "\033[0m"


def clear():
    os.system("clear")


def banner():
    print(VERMELHO_FORTE, end="")
    print(textwrap.dedent(fr"""
     _____ _                _           _
    |_   _| |__  _   _ _ __| |__  _   _| |__
      | | | '_ \| | | | '__| '_ \| | | | '_ \
      | | | | | | |_| | |  | | | | |_| | |_) |
      |_| |_| |_|\__,_|_|  |_| |_|\__,_|_.__/ {RESET}{MAGENTA}V2{RESET}
    """).strip("\n"))
    print(RESET, end="")


def menu():
    senha = getpass(f"{RESET}{BRANCO_FORTE}\ndigite a senha: {RESET}")
    hash_recebido = hashlib.sha256(senha.encode()).hexdigest()

    if hash_recebido == HASH_ESPERADO:
        print("\n\033[1;32mAcesso liberado\033[0m")
        time.sleep(1)
    else:
        print(f"\n{VERMELHO_FORTE}Acesso negado{RESET}")
        sys.exit()


def mostrar_jogos():
    clear()
    banner()

    print(f"{AMARELO_FORTE}\n!ALGUNS LINKS PODEM NÃO FUNCIONAR!{RESET}\n")

    print(f"{CIANO_FORTE}1 - Minecraft{RESET} ({VERDE_FORTE}https://quenq.com/apps/minecraft/{RESET})")
    print(f"{CIANO_FORTE}2 - Gta vice city{RESET} ({VERDE_FORTE}https://quenq.com/apps/vice-city/{RESET})")
    print(f"{CIANO_FORTE}3 - Gta 3{RESET} ({VERDE_FORTE}https://quenq.com/apps/iii-online/{RESET})")
    print(f"{CIANO_FORTE}4 - Veck.io{RESET} ({VERDE_FORTE}https://zapgames.io/veck-io{RESET})")

    escolha_de_jogo = input(f"\n{BRANCO_FORTE}digite sua escolha: {RESET}")

    if escolha_de_jogo == "1":
        print("abrindo Minecraft...")
        os.system("xdg-open https://quenq.com/apps/minecraft/")
    elif escolha_de_jogo == "2":
        print("abrindo gta vice city...")
        os.system("xdg-open https://quenq.com/apps/vice-city/")
    elif escolha_de_jogo == "3":
        print("abrindo gta 3...")
        os.system("xdg-open https://quenq.com/apps/iii-online/")
    elif escolha_de_jogo == "4":
        print("abrindo veck.io...")
        os.system("xdg-open https://zapgames.io/veck-io")
    else:
        print("escolha invalida")


def mostrar_pra_debian():
    clear()
    banner()

    print(f"\n{AMARELO_FORTE}1 - hack para kahoot{RESET}")
    print(f"{AMARELO_FORTE}2 - zphisher{RESET}")
    print(f"{AMARELO_FORTE}3 - jogos{RESET}")
    print(f"{AMARELO_FORTE}4 - vs code{RESET}")

    escolha = input(f"{CIANO_FORTE}\nEscolha: {RESET}")

    if escolha == "1":
        if os.path.isdir("Kitty-Tools"):
            print(f"{AMARELO_FORTE}=== hack para kahoot ja esta instalado ==={RESET}")
        else:
            print(f"{CIANO_MERDA}=== Instalando hack para kahoot ==={RESET}")
            subprocess.run(comando_kahoot_debian, shell=True)

    elif escolha == "2":
        if os.path.isdir("zphisher"):
            print(f"{AMARELO_FORTE}=== zphisher ja esta instalado ==={RESET}")
        else:
            print(f"{CIANO_MERDA}=== Instalando zphisher ==={RESET}")
            subprocess.run(comando_zphisher_debian, shell=True)

    elif escolha == "3":
        mostrar_jogos()

    elif escolha == "4":
        print(f"{CIANO_FORTE}=== Instalando vs code ==={RESET}")
        subprocess.run(comando_vscode_debian, shell=True)

    else:
        print("escolha invalida")


def mostrar_pra_termux():
    clear()
    banner()

    print(f"\n{AMARELO_FORTE}1 - hack para kahoot{RESET}")
    print(f"{AMARELO_FORTE}2 - zphisher{RESET}")
    print(f"{AMARELO_FORTE}3 - jogos{RESET}")

    escolha = input(f"{CIANO_FORTE}\nEscolha: {RESET}")

    if escolha == "1":
        if os.path.isdir("Kitty-Tools"):
            print(f"{AMARELO_FORTE}=== hack para kahoot ja esta instalado ==={RESET}")
        else:
            print(f"{CIANO_MERDA}=== Instalando hack para kahoot ==={RESET}")
            subprocess.run(comando_kahoot_termux, shell=True)

    elif escolha == "2":
        if os.path.isdir("zphisher"):
            print(f"{AMARELO_FORTE}=== zphisher ja esta instalado ==={RESET}")
        else:
            print(f"{CIANO_MERDA}=== Instalando zphisher ==={RESET}")
            subprocess.run(comando_zphisher_termux, shell=True)

    elif escolha == "3":
        mostrar_jogos()

    else:
        print("escolha invalida")


clear()
banner()
menu()

clear()
banner()

try:
    detectado = platform.freedesktop_os_release()

    if detectado["ID"] == "debian":
        print(f"{AZUL_FORTE}\nsistema detectado: {RESET}{AMARELO_FORTE}debian{RESET}")
        time.sleep(1)
        sistema = 2

except (OSError, AttributeError):
    pass

if "TERMUX_VERSION" in os.environ:
    print(f"{AZUL_FORTE}\nsistema detectado: {RESET}{AMARELO_FORTE}termux{RESET}")
    time.sleep(1)
    sistema = 1

if sistema == 1:
    mostrar_pra_termux()
elif sistema == 2:
    mostrar_pra_debian()
else:
    print(f"{VERMELHO_FORTE}Sistema operacional não reconhecido.{RESET}")

