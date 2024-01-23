import pyaudio
import wave

FRAMES_PER_BUFFER = 6400

FORMAT = pyaudio.paInt16
CHANNELS =1
RATE = 100000

p=pyaudio.PyAudio()


stream=p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER    
)

print("Start Recording")

seconds = 6
frames =[]
for i in range (0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obje = wave.open("op.wav", "wb")
obje.setnchannels(CHANNELS)
obje.setsampwidth(p.get_sample_size(FORMAT))
obje.setframerate(RATE)
obje.writeframes(b"".join(frames))
obje.close()

print("Recorded")





