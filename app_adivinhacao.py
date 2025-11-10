import random
import time

def jogo_busca_binaria ():
    # Jogo onde o computador tenta adivinhar o númer que o usuário pensou, usando busca binária.
    
    print("\n==============================================")
    print("  JOGO 1: O COMPUTADOR TENTA ADIVINHAR")
    print("==============================================")
    print("Pense em um número inteiro entre 0 e 128.")
    print("Eu terei 7 tentativas para adivinhar.")
    print("Responda com 'sim' ou 'nao'.")
    print("----------------------------------------------")
    
    # Pausa para o usuário pensar
    time.sleep(2)
    
    limite_inferior = 0 
    limite_superior = 128 
    tentativa_atual = 0 
    max_tentativas = 7 # log2(128) é 7, então 7 tentativas são suficientes
    acertou = False  # Flag para saber se o loop terminou com acerto

    
    print("Pense em um número inteiro entre 0 e 128")

    while tentativa_atual < max_tentativas: 
        tentativa_atual += 1 
        print(f"\nTentativa {tentativa_atual} de {max_tentativas}...")
        
        # Evita que os limites se cruzem
        if limite_inferior > limite_superior: 
            print("\nOpa! Parece que suas respostas foram inconsistentes.")
            acertou = True 
            break

        palpite = (limite_inferior+limite_superior)// 2
        
        # --- Validação da resposta 'sim' ou 'nao' ---
        resposta_acerto = " "
        while resposta_acerto not in ["sim", "nao"]: 
            resposta_acerto = input (f"O número que você pensou é {palpite}? (sim/nao) ").strip().lower()
            
            if resposta_acerto  not in ["sim", "nao"]: 
                print("Resposta inválida. Por favor, digite 'sim' ou 'nao'.")
    
        if (resposta_acerto == "sim"):
            print(f"\nEba! O número é {palpite} e eu adivinhei em {tentativa_atual} tentativas! ")
            acertou = True
            break
        else: 
        # --- Validação da resposta 'maior' ---
           resposta_maior = ""
           while resposta_maior not in ["sim", "nao"]: 
               # Pergunta se o palpite foi maior que o número pensado
               resposta_maior = input(f"O número {palpite} é MAIOR que o seu? (sim/nao) ").strip().lower()
               
               if resposta_maior not in  ["sim", "nao"]: 
                   print("Resposta inválida. Por favor, digite 'sim' ou 'nao'.")
                
        if(resposta_maior == "sim"):
            # Se o palpite é MAIOR, o número real é MENOR.
            # Então, o novo teto (limite_superior) vira palpite - 1
            limite_superior = palpite - 1 
        else: 
            # Se o palpite é MENOR, o número real é MAIOR.
            # Então, o novo piso (limite_inferior) vira palpite + 1
            limite_inferior = palpite - 1 
             
     # Verifica se saiu do loop sem acertar    
    if not acertou:
        print("\nAh, parece que não consegui adivinhar em 7 tentativas.")
        print("Vamos jogar de novo?")

    print("----------------------------------------------")
    input("Pressione Enter para voltar ao menu...")                    
                
                
def jogo_numero_secreto ():
    #Jogo onde o usuário tenta adivinhar o número sorteado pelo computador (1 a 100).

    numero_secreto = random.randint(1,100) 
    numero_tentativa = 0
    pontos = 1000 
    nivel = 0 

    # --- Validação da escolha do nível ---
    while nivel not in [1, 2, 3]: 
        try: 
            nivel = int(input(f"Qual o nível de dificuldade?\n(1) Fácil (20 tent.) (2) Médio (15 tent.) (3) Difícil (6 tent.)\nEscolha: "))
            if nivel not in [1, 2, 3]:
                print("Opção inválida. Digite 1, 3 ou 3.")
        except ValueError: 
            print("Entrada inválida. Por favor, digite um NÚMERO (1, 2 ou 3)")

    if(nivel == 1):
        numero_tentativa = 20
    if(nivel == 2): 
        numero_tentativa = 15 
    if(nivel == 3): 
        numero_tentativa = 6
        
    tentativa = 1 
    acertou = False 
    
    print(f"\nCerto! Você tem {numero_tentativa} tentativas. Valendo {pontos} pontos!")
    print("----------------------------------------------")
    
    
    while tentativa <= numero_tentativa: 
        print(f"Tentativa {tentativa} de {numero_tentativa}")
        
        # --- Validação do chute ---
        chute = 0 
        try: 
            chute = int(input("Qual o seu chute (entre 1 e 100): "))
        except ValueError: 
             print("Entrada inválida. Você deve digitar um NÚMERO.")
             continue # Pula para a próxima iteração do loop, sem contar a tentativa
        
        print(f"Seu chute foi {chute}")
        
        if(chute < 0 or chute > 100): 
            print("Você deve chutar um número entre 1 e 100. Tente novamente.")
            # Não incrementa a tentativa se o chute for inválido
            continue 
        
        acertou = (chute == numero_secreto)
        
        if(acertou):
            break 
        
        else: 
            # Calcula pontos perdidos apenas se errar
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos
            
            if(chute > numero_secreto):
                print("Você errou!\n Dica: o número secreto é MENOR")
            if(chute < numero_secreto):
                print("Você errou!\n Dica: o número secreto é MAIOR")
                
        # Incrementa a tentativa apenas após um chute válido
        tentativa += 1
    
    # --- Mensagem Final ---  
    if(acertou): 
        print(f"\nParabéns! Você acertou na {tentativa}ª tentativa!")
        print(f"Total de pontos: {pontos}")
    else:
        print("\nVocê perdeu! Suas tentativas acabaram.")
        print(f"O número secreto era {numero_secreto}")
    
    print("----------------------------------------------")
    input("Pressione Enter para voltar ao menu...")
        
def main():
   #Função principal que exibe o menu e gerencia a escolha do jogo.
   
    while True: 
        print("\n======================================")
        print(" BEM-VINDO AO MENU DE JOGOS ")
        print("======================================")
        print("Escolha seu jogo:")
        print("(1) Eu adivinho seu número (Busca Binária)")
        print("(2) Você adivinha meu número (Número Secreto)")
        print("(0) Sair do programa")
        print("--------------------------------------")
        
        escolha = input("Digite sua opção (1, 2 ou 0): " ).strip()
        
        if escolha == "1": 
            jogo_busca_binaria()
        elif escolha == "2":
            jogo_numero_secreto()
        elif escolha == "0":
            print("\nObrigado por jogar! Até a próxima. ")
            break
        else:
            print("\nOpção inválida! Por favor, escolha 1, 2 ou 0.")
            time.sleep(1.5)
            
# --- Ponto de entrada do programa ---
# Verifica se este script está sendo executado diretamente
if __name__ == "__main__":
    main()
            
         
        
    
    
        
    
   
