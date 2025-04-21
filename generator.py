from midiutil import MIDIFile

midi = MIDIFile(4)
channel = [0, 1, 2, 3]
volume = [70, 60, 80, 65]
tempo = 60
time = 0

for i in range(4):
    midi.addTempo(i, time, tempo)

# Cello (track 0)
cello_notes = [48, 51, 55, 53, 56, 55, 51, 50, 53, 48, 51, 55, 56, 58, 55]
for i, pitch in enumerate(cello_notes):
    midi.addNote(0, channel[0], pitch, time + i, 1, volume[0])

# Piano (track 1)
piano_chords = [
    [60, 55, 63], [], [53, 60, 57], [],
    [63, 58, 55], [], [53, 60, 57], []
]
piano_time = 0
for triad in piano_chords:
    if triad:
        for note_pitch in triad:
            midi.addNote(1, channel[1], note_pitch, piano_time, 4, volume[1])
    piano_time += 4

# Violin I (track 2)
violin_melody = [67, 70, 68, 65, 67, 67, 65, 63]
for i, pitch in enumerate(violin_melody):
    midi.addNote(2, channel[2], pitch, time + 16 + i, 1, volume[2])

# Viola (track 3)
viola_harmony = [63, 69, 65, 67]
for i, pitch in enumerate(viola_harmony):
    midi.addNote(3, channel[3], pitch, time + 16 + i * 4, 4, volume[3])

with open("ashes_of_the_crown_mockup.mid", "wb") as output_file:
    midi.writeFile(output_file)
print("MIDI file created successfully.")