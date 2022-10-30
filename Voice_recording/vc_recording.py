#Libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


#For recording within the frequency
freq = 48000
#For recording within the duration
duration = 5

#Start recording
my_recording = sd.rec(int(duration*freq),samplerate=freq, channels=2)

sd.wait()

write("my_recording0.wav", freq, my_recording)

wv.write("my_recording1.wav", my_recording, freq, sampwidth=2)
