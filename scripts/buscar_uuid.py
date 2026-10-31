import requests

preto = "\033[30m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
magenta = "\033[35m"
ciano = "\033[36m"
branco = "\033[37m"

preto_forte = "\033[90m"
vermelho_forte = "\033[91m"
verde_forte = "\033[92m"
amarelo_forte = "\033[93m"
azul_forte = "\033[94m"
magenta_forte = "\033[95m"
ciano_forte = "\033[96m"
branco_forte = "\033[97m"

reset = "\033[0m"

URL = "https://create.kahoot.it/rest/kahoots/"

def buscar_quizzes(termo, limite=20):

    parametros = {
        "query": termo,
        "limit": limite,
        "cursor": 0,
        "orderBy": "relevance"
    }
    
    try:
        resposta = requests.get(
            URL,
            params=parametros,
            timeout=15
        )

        resposta.raise_for_status()
        dados = resposta.json()
        
        quizzes = dados.get("entities", [])
        
        if not quizzes:
            print("nenhum quiz encontrado")
            return

        print(f"{amarelo_forte}{len(quizzes)} resultados encontrados{reset}")
       

        for numero, quiz in enumerate(quizzes, 1):
            card = quiz.get("card", quiz)

            titulo = card.get("title", "sem titulo")
            quizid = card.get("uuid", "sem uuid")
            
            print( f"{numero}. {titulo}")
            print(f"quizId: {verde_forte}{quizid}{reset}")
            print("-" * 40)

    except requests.exceptions.RequestException:
        print(f"{vermelho_forte}ERRO NA REQUISIÇÃO{reset}")

def main():
    termo = input("pesquise no kahoot: ")

    if not termo:
        print("digite alguma coisa")

    buscar_quizzes(termo)


if __name__ == "__main__":
    main()

        
        


