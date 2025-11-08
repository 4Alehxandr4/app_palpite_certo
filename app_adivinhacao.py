import random
import time

def jogo_busca_binaria ():
    
    a = 0 
    b = 128 
    t = 0 
    acertou = False
    
    print("Pense em um número inteiro entre 0 e 128")

    while True: 
        t += 1 
        
        if (t == 7): 
            print("Desculpa, não consegui adivinhar após 6 tentativas.")
            break

        m = (a+b)// 2
        
        resposta_acerto = " "
        while resposta_acerto not in ["sim", "nao"]: 
            resposta_acerto = input (f"O número que você pensou é {m}? (sim/nao) ").strip().lower()
            
            if resposta_acerto  not in ["sim", "nao"]: 
                print("Resposta inválida. Por favor, digite 'sim' ou 'nao'.")
    
        if (resposta_acerto == "sim"):
            print(f"\nEba! O número é {m} e eu adivinhei em {t} tentativas! ")
            acertou = True
            break
        else: 
        # --- Validação da resposta 'maior' ---
           resposta_maior = ""
           while resposta_maior not in ["sim", "nao"]: 
               resposta_maior = input(f"O número {m} é MAIOR que o seu? (sim/nao) ").strip().lower()
               if resposta_maior not in  ["sim", "nao"]: 
                   print("Resposta inválida. Por favor, digite 'sim' ou 'nao'.")
                
        if(resposta_maior == "sim"):
            b = m - 1 
        else: 
            a = m - 1  
            
    if not acertou:
        print("\nAh, parece que não consegui adivinhar em 7 tentativas.")
        print("Vamos jogar de novo?")

    print("----------------------------------------------")
    input("Pressione Enter para voltar ao menu...")
             
                
                
                
                
def jogo_numero_secreto ():

    numero_secreto = random.randint(1,100) 

    chute = 0 
    acertou = 0 
    pontos = 100 


    nivel = int(input(f"Qual o nível de dificuldade?\nEscolha: (1) Fácil (2) Médio (3) Difícil\n"))


    if(nivel == 1):
        num_tentativa = 20
    if(nivel == 2): 
        num_tentativa = 15 
    if(nivel == 3): 
        num_tentativa = 6
        
    tentativa = 1 


    while tentativa <= num_tentativa: 
        print(f"Tentativa {tentativa} de {num_tentativa}")
        chute = int(input("Qual o seu chute: "))
        print(f"Seu chute foi {chute}")
        
        if(chute < 0 or chute > 100): 
            print("Você deve chutar um número entre 1 e 100. Tente novamente.")
            continue 
        
        tentativa += 1 
        
        acertou = chute == numero_secreto
        
        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos
        
        if(acertou):
            break 
        elif(chute > numero_secreto):
            print("Você errou!\n Dica: o número secreto é MENOR")
        elif(chute < numero_secreto):
            print("Você errou!\n Dica: o número secreto é MAIOR")
        
    if(acertou): 
        print(f"Você acertou na tentativa {tentativa - 1}°\n")
        print(f"Total de pontos: {pontos}") 

    else: 
        print("Você perdeu! tente novamente \n")
        print(f"O número secreto era {numero_secreto}")
        
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
            jogo_numero_secreto
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
            
         
        
    
    
        
    
   
