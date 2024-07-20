import sounddevice as sd
import numpy as np

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
        sample_rate = 44100
        duration = 1  # seconds
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        note = np.sin(freq * t * 2 * np.pi)
        audio = note * (2**15 - 1) / np.max(np.abs(note))
        audio = audio.astype(np.int16)
        sd.play(audio, sample_rate)
        status = sd.wait()
    else:
        print("Nota não reconhecida!")

while True:
    entrada = input("Digite a nota musical (ou 'sair' para encerrar): ").strip().lower()
    if entrada == 'sair':
        break
    tocar_nota(entrada)