import time

# pede ao usuário o tempo desejado em segundos
tempo_total = int(input("Digite o tempo desejado em segundos: "))

# inicia o cronômetro
inicio = time.time()

# loop enquanto o tempo não se esgota
while True:
    # calcula o tempo decorrido
    tempo_decorrido = time.time() - inicio
    
    # calcula o tempo restante
    tempo_restante = tempo_total - tempo_decorrido
    
    # verifica se o tempo se esgotou
    if tempo_restante <= 0:
        print("O tempo se esgotou!")
        break
    
    # exibe o tempo restante em segundos
    print("Tempo restante:", int(tempo_restante), "segundos")
    
    # espera um segundo antes de verificar novamente
    time.sleep(1)
