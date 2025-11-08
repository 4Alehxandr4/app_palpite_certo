import random

a = 0 
b = 128 
t = 0 

print("Pense em um número inteiro entre 0 e 128")

while True: 
    t += 1 
    
    if (t == 7): 
        print("Desculpa, não consegui adivinhar após 6 tentativas.")
        break

    m = (a+b)// 2
    resposta = input(f"O número que você pensou é {m}? (responda 'sim' ou 'nao') ")

    if (resposta == "sim"): 
        print(f"O número é {m} e eu adivinhei em {t} tentativas! ")
        break

    else: 
        resposta = input(f"O número {m} é MAIOR que o seu? (responda 'sim' ou 'nao') ")
        
        if(resposta == "sim"):
            b = m 
        else: 
            a = m 

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
    
        
    
   
