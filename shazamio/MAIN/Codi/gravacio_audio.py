import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
duracio = 10
archivo = "gravacio.wav"

#   Inici Pyaudio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

#   Inici gravació
print('gravant...')
frames = []

for i in range(0, int(RATE/CHUNK*duracio)):
    data = stream.read(CHUNK)
    frames.append(data)
print('gravació acabada')

#   Detenim gravació
stream.stop_stream()
stream.close()
audio.terminate()

#   Creació i es desa l'arxiu d'àudio
waveFile = wave.open(archivo, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()