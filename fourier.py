import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# a4_octave = ['DO', 'do', 'RE', 're', 'MI', 'mi', 'FA', 'fa', 'SOL', 'sol', 'LA', 'la', 'SI']
a4_octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']


def set_freqs(notes_scale, octave):
    output = {}
    for i in range(len(notes_scale)):
        freq = 440 * np.exp((octave - 4) + (i + 1 - 10) / 12 * np.log(2))
        output[notes_scale[i]] = freq
    return output


def get_sine_wave(freq, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave


notes = set_freqs(a4_octave, 4)
wave_fa = get_sine_wave(notes['A'], 1)
wave_sol = get_sine_wave(notes['G'], 1)

harmonic = np.add(wave_fa, wave_sol)
plt.plot(harmonic[0:2500])
plt.show()


#for note in notes:
#    plt.plot(get_sine_wave(notes[note], 1)[0:2500])
#plt.xlabel('Time')
#plt.ylabel('Amplitude')
#plt.show()


wavfile.write('harmonic_A_G.wav', rate=44100, data=harmonic.astype(np.int16))
