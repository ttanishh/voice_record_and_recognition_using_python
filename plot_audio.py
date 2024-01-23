# import wave
# import matplotlib.pyplot as plt 
# import numpy as np 

# ob = wave.open("sample.wav", "rb")
# sampleFreq = ob.getframerate()
# n_samples = ob.getnframes()
# signal_wave = ob.readframes(-1)
# ob.close()

# t_audio =(n_samples / sampleFreq)
# print(t_audio)

# signal_array = np.frombuffer(signal_wave, dtype=np.int16)
# times = np.linspace(0, t_audio, num=n_samples)

# plt.figure(figsize=(8, 4))
# plt.plot(times, signal_array)
# plt.title("Audio Signal")
# plt.ylabel("Signal Wave")
# plt.xlabel("Time(in sec)")
# plt.xlim(0, t_audio)
# plt.show()

import wave
import matplotlib.pyplot as plt
import numpy as np


ob = wave.open("sample.wav", "rb")
sampleFreq = ob.getframerate()
n_samples = ob.getnframes()
signal_wave = ob.readframes(-1)
ob.close()


t_audio = n_samples / sampleFreq

signal_array = np.frombuffer(signal_wave, dtype=np.int16)


times = np.linspace(0, t_audio, num=len(signal_array))  # Use len(signal_array)

plt.figure(figsize=(8, 4))
plt.plot(times, signal_array, label="Audio Signal")
plt.title("Audio Signal Waveform")
plt.xlabel("Time (in seconds)")
plt.ylabel("Amplitude")
plt.show()

