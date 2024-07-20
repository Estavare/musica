from sound.sound_device import play_sound
from notas.note_device import Note
import re

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
        entrada = str(input("Digite a nota musical (ou 'sair' para encerrar): ")).strip().lower()
        if entrada == 'sair':
            break

        match = re.match(r'([a-z]+#?)\s*(\d+)?', entrada)
        if match:
            note_name = match.group(1)
            octave_shift = match.group(2)
            if octave_shift:
                octave_shift = int(octave_shift)
            else:
                octave_shift = 5  # Oitava padrão como a central (5)
        else:
            print("Nota não reconhecida!")
            continue

        if note_name in notas:
            freq = notas[note_name].play(octave_shift - 5)  # Considerando a oitava 5 como a oitava central
            play_sound(freq, 1)  # Play the sound for 1 second
        else:
            print("Nota não reconhecida!")

if __name__ == "__main__":
    main()
