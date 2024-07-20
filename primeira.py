import pyo

# Inicializa o servidor de áudio
s = Server().boot()

# Dicionário que mapeia as notas para suas frequências em Hz
notas = {
    'do': 261.63,
    'do#': 277.18,
    're': 293.66,
    're#': 311.13,
    'mi': 329.63,
    'fa': 349.23,
    'fa#': 369.99,
    'sol': 392.00,
    'sol#': 415.30,
    'la': 440.00,
    'la#': 466.16,
    'si': 493.88
}

def tocar_nota(nota):
    if nota in notas:
        freq = notas[nota]
        # Cria um objeto de onda senoidal com a frequência da nota
        sine = Sine(freq, mul=0.5).out()
        # Inicia o servidor
        s.start()
        # Toca a nota por 1 segundo
        s.sleep(1)
        # Para o servidor
        s.stop()
    else:
        print("Nota não reconhecida!")

while True:
    entrada = input("Digite a nota musical (ou 'sair' para encerrar): ").strip().lower()
    if entrada == 'sair':
        break
    tocar_nota(entrada)

s.shutdown()

