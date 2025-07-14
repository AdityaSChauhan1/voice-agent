import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("sample.wav" , "rb")

sample_freq=obj.getframerate()
n_samples= obj.getnframes()
signal_wave = obj.readframes(-1)
n_channels =obj.getnchannels()
obj.close()

t_audio =n_samples / sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave  ,dtype=np.int16)

if n_channels ==2:
    signal_array= signal_array.reshape(-1 , 2)
    signal_array= signal_array[:,0]

times =np.linspace(0 , t_audio , num =n_samples)

plt.figure(figsize=(15 ,5))
plt.plot(times,signal_array)
plt.title("audio signal")
plt.ylabel("signal wave")
plt.xlabel("time")
plt.xlim(0 , t_audio)
plt.grid()
plt.show()