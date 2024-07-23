import numpy as np
import pyaudio

def play_sound(frequency, duration):
    # Generate the sound wave
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)

    # Open the audio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, output=True)

    # Write the audio data to the stream
    stream.write(audio.tobytes())

    # Close the audio stream
    stream.stop_stream()
    stream.close()
    p.terminate()
