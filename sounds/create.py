import numpy as np
from scipy.io.wavfile import write

def key(frequency, duration = 1, sampling_rate = 44100 , amplitude = 10000):
    """ Returns a Numpy array for a given frequency """
    times = np.linspace(0,duration,sampling_rate*duration)
    note = amplitude * np.sin(2*np.pi*frequency*times)
    return note.astype(np.int16)

notes = {}
notes_config = open("notes.config","r").read().split("\n")
for line in notes_config:
	l = line.split(" ")
	k = l[0]
	v = l[1]
	notes[k] = v
print(notes)
for i in notes:
	print("Generating for "+i+" ...")
	write(i+'.wav', 44100, key(int(notes[i])))
	print("Done..")


#Create notes for the lower octave

for i in notes:
	print("Generating for "+i+"lower ...")
	write(i+'l.wav', 44100, key(int(notes[i])/2))
	print("Done..")

