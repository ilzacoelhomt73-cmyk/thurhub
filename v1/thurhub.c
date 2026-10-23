#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <termios.h>
#include <openssl/evp.h>

#define HASH_ESPERADO "3669e7add5d311474d0dd3c6e6020163d99c610af9519ad0194158e96d1f7f10"

char comando[100];
int executou = 0;
int escolha = 0;
int sistema = 0;
int numero = 0;
int primeira_vez = 1;
int escolha_de_jogo = 0;



void mostrar_banner(void) {
    printf("\033[1;31m");
    printf(" _____ _                _           _     \n");
    printf("|_   _| |__  _   _ _ __| |__  _   _| |__  \n");
    printf("  | | | '_ \\| | | | '__| '_ \\| | | | '_ \\ \n");
    printf("  | | | | | | |_| | |  | | | | |_| | |_) |\n");
    printf("  |_| |_| |_|\\__,_|_|  |_| |_|\\__,_|_.__/ \n");
    printf("                                          \n");
    printf("\033[0m");
}

void mostrar_jogo(const char *jogo, const char *link) {



    
if (primeira_vez) {
    mostrar_banner();
    printf("\n\033[1;33m!ALGUMS LINKS PODEM NÃO FUNCIONAR!\n\n");
    primeira_vez = 0;
}
 

printf("\033[1;36m%d - %s \033[0m(\033[1;32m%s\033[0m)\n", ++numero, jogo, link);


}

void instalar_para_debian(const char *ferramenta) {

if (strcmp(ferramenta, "kahoot") == 0) {

  

  system(
        "sudo apt update -y && "
        "sudo apt upgrade -y && "
        "sudo apt install -y git python3-pip nodejs npm && "
        "python3 -m pip install --break-system-packages pystyle colorama && "
        "git clone https://github.com/CPScript/Kitty-Tools && "
        "cd Kitty-Tools && python3 main.py"
    );
}

else if (strcmp(ferramenta, "zphisher") == 0) {
    system(
      "sudo apt update -y &&"
      "sudo apt upgrade -y &&"
      "sudo apt install git -y &&"
      "git clone https://github.com/htr-tech/zphisher.git &&"
      "cd zphisher && bash zphisher.sh"
    );
  }



else if (strcmp(ferramenta, "jogos") == 0) {
    system("clear");

    numero = 0;
    primeira_vez = 1;

    mostrar_jogo("minecraft", "https://quenq.com/apps/minecraft/");
    mostrar_jogo("Gta vice city", "https://quenq.com/apps/vice-city/");
    mostrar_jogo("Gta 3", "https://quenq.com/apps/iii-online/");
    mostrar_jogo("Veck.io", "https://zapgames.io/veck-io");
    printf("\n\033[1;37mdigite sua escolha: \033[0m");
    scanf("%d", &escolha_de_jogo);

    switch (escolha_de_jogo) {
        case 1:
            system("xdg-open https://quenq.com/apps/minecraft/");
            break;        
        case 2:
            system("xdg-open https://quenq.com/apps/vice-city/");
            break;
        case 3:
            system("xdg-open https://quenq.com/apps/iii-online/");
            break;
        case 4:
            system("xdg-open https://zapgames.io/veck-io");
            break;        

        default:
            printf("jogo invalido\n");


}


}

}


void instalar_para_termux(const char *ferramenta) {

if (strcmp(ferramenta, "kahoot") == 0) {

  system(
        "pkg update -y && "
        "pkg upgrade -y && "
        "pkg install -y git python python-pip nodejs npm && "
        "python -m pip install pystyle colorama && "
        "git clone https://github.com/CPScript/Kitty-Tools && "
        "cd Kitty-Tools && python main.py"
    );
  }

  

else if (strcmp(ferramenta, "zphisher") == 0) {
    system(
      "pkg update -y &&"
      "pkg upgrade -y &&"
      "pkg install git -y &&"
      "git clone https://github.com/htr-tech/zphisher.git &&"
      "cd zphisher && bash zphisher.sh"
    );
  }

else if (strcmp(ferramenta, "jogos") == 0) {
    system("clear");
    
    numero = 0;
    primeira_vez = 1; 
  
    mostrar_jogo("minecraft", "https://quenq.com/apps/minecraft/");
    mostrar_jogo("Gta vice city", "https://quenq.com/apps/vice-city/");
    mostrar_jogo("Gta 3", "https://quenq.com/apps/iii-online/");
    mostrar_jogo("Veck.io", "https://zapgames.io/veck-io");
    printf("\n\033[1;37mdigite sua escolha: \033[0m");
    scanf("%d", &escolha_de_jogo);

    switch (escolha_de_jogo) {
        case 1:
            printf("%d\n", system("xdg-open https://quenq.com/apps/minecraft/"));
            break;        
        case 2:
            system("xdg-open https://quenq.com/apps/vice-city/");
            break;
        case 3:
            system("xdg-open https://quenq.com/apps/iii-online/");
            break;
        case 4:
            system("xdg-open https://zapgames.io/veck-io");
            break;        

        default:
            printf("jogo invalido\n");




    }
}

}





void executar_opcao(const char *tool) {
    if (sistema == 1) {
        instalar_para_termux(tool);
    } else if (sistema == 2) {
        instalar_para_debian(tool);
    }
}

void menu(void) {
    while (1) {
        system("clear");
        mostrar_banner();

        printf("\033[1;33m1 - hack para kahoot\033[0m\n");
        printf("\033[1;33m2 - zphisher\033[0m\n");
        printf("\033[1;33m3 - jogos\033[0m\n");
        printf("\n\033[36mEscolha: \033[0m");
        fflush(stdout);

        if (scanf("%d", &escolha) != 1) {
            while (getchar() != '\n');
            continue;
        }

        switch (escolha) {
            case 1:
                executar_opcao("kahoot");
                break;


            case 2:
                executar_opcao("zphisher");
                break;

            case 3:
                executar_opcao("jogos");
                break;


            default:
                printf("Opcao invalida.\n");
                sleep(1);
                break;
        }
    }
}

int main(void) {
    int tentativas = 3;
    char senha[100];
    unsigned char hash[EVP_MAX_MD_SIZE];
    unsigned int tamanho = 0;
    char hash_hex[65] = {0};

    struct termios original, novo;

    while (tentativas > 0) {
        system("clear");
        mostrar_banner();
        
        printf("\033[1;37mdigite a senha: \033[0m");
        fflush(stdout);

        int eco_desativado =
            tcgetattr(STDIN_FILENO, &original) == 0;

        if (eco_desativado) {
            novo = original;
            novo.c_lflag &= ~ECHO;
            tcsetattr(STDIN_FILENO, TCSANOW, &novo);
        }

        if (fgets(senha, sizeof(senha), stdin) == NULL) {
            if (eco_desativado) {
                tcsetattr(STDIN_FILENO, TCSANOW, &original);
            }
            printf("\nErro ao ler a senha.\n");
            return 1;
        }

        if (eco_desativado) {
            tcsetattr(STDIN_FILENO, TCSANOW, &original);
        }

        printf("\n");
        senha[strcspn(senha, "\n")] = '\0';

        if (EVP_Digest(
                senha,
                strlen(senha),
                hash,
                &tamanho,
                EVP_sha256(),
                NULL) != 1) {
            printf("Erro ao calcular o hash.\n");
            return 1;
        }

        for (unsigned int i = 0; i < tamanho; i++) {
            snprintf(&hash_hex[i * 2], 3, "%02x", hash[i]);
        }

        if (strcmp(hash_hex, HASH_ESPERADO) == 0) {
            printf("\n\033[1;32mAcesso liberado!\033[0m\n");
            sleep(1);
            break;
        }

        tentativas--;
        printf("\033[1;31mAcesso negado. Tentativas restantes: %d\033[0m\n",
               tentativas);
        sleep(1);
    }

    if (tentativas == 0) {
        printf("Numero maximo de tentativas atingido.\n");
        return 1;
    } 

    system("clear");
    mostrar_banner();

    printf("\033[33m1 - Termux\033[0m\n");
    printf("\033[33m2 - Debian\033[0m\n");
    printf("\n\033[1;37mEscolha o sistema: \033[0m");
    fflush(stdout);

    if (scanf("%d", &sistema) != 1 ||
        (sistema != 1 && sistema != 2)) {
        printf("Sistema invalido.\n");
        return 1;
    }

    menu();

    return 0;
}
