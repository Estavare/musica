class Note:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency

    def play(self, octave_shift=0):
        freq = self.frequency
        freq *= 2 ** octave_shift  # adjust frequency by octave shift
        return freq
