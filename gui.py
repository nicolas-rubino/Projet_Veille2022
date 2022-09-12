from re import T
from time import sleep
import  PySimpleGUI as sg
import record_mic
import pyaudio
import wave
import time
import threading
import print_wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

frames = []
past_t = 0
start_time = time.time()
recording = True

layout = [
    [sg.Text("L'enregistrement a commence")],
    [sg.Button("Arret")]],

def record():
    while recording:
        past_t = 0
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)
        current_time = time.time()
        elapsed_time = current_time - start_time
        if str(int(elapsed_time)) > str(int(past_t)):
            print(str(int(elapsed_time)))
        past_t = str(int(elapsed_time))
    return

def end_record():
    stream.start_stream()
    stream.close()
    p.terminate()

    obj = wave.open("output.wav", "wb")
    obj.setnchannels(CHANNELS)
    obj.setsampwidth(p.get_sample_size(FORMAT))
    obj.setframerate(RATE)
    obj.writeframes(b"".join(frames))
    obj.close()

window = sg.Window("Voice Recognition App", layout, margins=(150,100))

myThread = threading.Thread(target = record)
myThread.start()

while True:
    event, values = window.read()
    if event == "Arret" or event == sg.WIN_CLOSED:
        recording = False
        myThread.join()
        end_record()
        break

window.close()
print_wave.show("output.wav")