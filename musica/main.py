
from sound.sound_device import play_sound
from notas.note_device import Note 

def main():
    notas = {
        'do': Note('do', 261.63),
        'do#': Note('do#', 277.18),
        're': Note('re', 293.66),
        're#': Note('re#', 311.13),
        'mi': Note('mi', 329.63),
        'fa': Note('fa', 349.23),
        'fa#': Note('fa#', 369.99),
        'sol': Note('sol', 392.00),
        'sol#': Note('sol#', 415.30),
        'la': Note('la', 440.00),
        'la#': Note('la#', 466.16),
        'si': Note('si', 493.88)
    }

    while True:
        entrada = input("Digite a nota musical (ou 'sair' para encerrar): ").strip().lower()
        if entrada == 'sair':
            break
        octave_shift = int(input("Digite o deslocamento de oitava (0 para padrão, -1 para uma oitava abaixo, 1 para uma oitava acima): "))
        if entrada in notas:
            freq = notas[entrada].play(octave_shift)
            play_sound(freq, 1)  # Play the sound for 1 second
        else:
            print("Nota não reconhecida!")

if __name__ == "__main__":
    main()