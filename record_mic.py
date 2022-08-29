import pyaudio
import wave
# import time

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels= CHANNELS,
    rate= RATE, 
    input= True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

# def display_seconds(x):
#     sec = time.strftime('%S',x)
#     sec = int(sec)
#     print(sec)

print("recording started")

seconds = 5 
frames = []
# t = time.gmtime()

for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.start_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav","wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()
