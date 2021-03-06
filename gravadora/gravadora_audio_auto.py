import pyaudio
import wave
from pydub import AudioSegment

def gravadora_audio_auto():
    #DEFINIMOS PARAMETROS
    FORMAT=pyaudio.paInt16
    CHANNELS=2
    RATE=44100
    CHUNK=1024
    duracion=10
    archivo="gravadora/grabacion.wav"

    #INICIAMOS "pyaudio"
    audio=pyaudio.PyAudio()

    #INICIAMOS GRABACIÓN
    stream=audio.open(format=FORMAT,channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("grabando...")
    frames=[]

    for i in range(0, int(RATE/CHUNK*duracion)):
        data=stream.read(CHUNK)
        frames.append(data)
    print("grabación terminada")

    #DETENEMOS GRABACIÓN
    stream.stop_stream()
    stream.close()
    audio.terminate()

    #CREAMOS/GUARDAMOS EL ARCHIVO DE AUDIO
    waveFile = wave.open(archivo, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    #   Passem arxiu de wav a mp3
    wav_audio = AudioSegment.from_file("gravadora/grabacion.wav", format="wav")
    wav_audio.export("gravadora/grabacion.mp3", format="mp3")

    return "gravadora/grabacion.mp3"

#gravadora_audio_auto()