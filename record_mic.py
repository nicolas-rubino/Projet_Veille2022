from multiprocessing.connection import wait
import pyaudio
import wave
import time
import threading

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
global recording

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


if __name__ == "__main__":
    recording = True
    myThread = threading.Thread(target = record)
    myThread.start()
    recording = False
    time.sleep(4)
    myThread.join()
    end_record()
