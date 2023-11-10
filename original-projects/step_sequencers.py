from pyo import *

s = Server().boot()

"""
harmonic_series = [100, 200, 300, 400, 500, 600, 700, 800]
whole_tone = Choice(midiToHz([60, 62, 64, 66, 68, 70, 72]))
major = Choice(midiToHz([60, 62, 64, 65, 67, 69, 71, 72]))
natural_minor = Choice(midiToHz([60, 62, 63, 65, 67, 68, 70, 72]))
major_pent = Choice(midiToHz([60, 62, 64, 67, 69, 72]))
minor_pent = Choice(midiToHz([60, 63, 65, 67, 70, 72]))
"""
# note choices
harmonic_series = [100, 200, 300, 400, 500, 600, 700, 800]
whole_tone = midiToHz([60, 62, 64, 66, 68, 70, 72])
major = midiToHz([60, 62, 64, 65, 67, 69, 71, 72])
natural_minor = midiToHz([60, 62, 63, 65, 67, 68, 70, 72])
major_pent = midiToHz([60, 62, 64, 67, 69, 72])
minor_pent = midiToHz([60, 63, 65, 67, 70, 72])

class Step_seq:
    def __init__(self):
        self.filter_lfo = Sine(freq=1).range(500, 2000)
        self.speed_lfo = Sine(freq=1).range(1, 20)
        self.notes = harmonic_series
        self.random_note = Choice(self.notes, self.speed_lfo)
        self.synth = SuperSaw([self.random_note, self.random_note])
        self.filter = MoogLP(self.synth, self.filter_lfo)
        
        self.filter.ctrl()

step_sequencers = []

mixer = Mixer(outs=3, chnls=2, time=0.5)

for i in range(0, 10):
    new_step_seq = Step_seq()
    step_sequencers.append(new_step_seq)
    mixer.addInput(i, new_step_seq.filter)
    mixer.setAmp(i, 0, 0.1)
print(type(mixer))

lf1 = Sine(freq=[0.1, 0.15], mul=100, add=250)
lf2 = Sine(freq=[0.18, 0.13], mul=0.4, add=1.5)
lf3 = Sine(freq=[0.07, 0.09], mul=5, add=6)

# Apply the phasing effect with 20 notches.
b = Phaser(mixer[0], freq=lf1, spread=lf2, q=lf3, num=20, mul=0.5).out()

# filter_lfo_1 = Sine(freq=1, mul=1000, add=1000)
# speed_lfo_1 = Sine(freq=0.1, mul=20, add=1)
# random_note_1 = Choice(major, speed_lfo_1)
# w1 = SuperSaw([random_note_1, random_note_1])
# f1 = Tone(w1, filter_lfo_1).out()

# filter_lfo_2 = Sine(freq=0.3, mul=1000, add=1000)
# speed_lfo_2 = Sine(freq=0.1, mul=20, add=2)
# random_note_2 = Choice(major, speed_lfo_2)
# w2 = SuperSaw([random_note_2, random_note_2])
# f2 = Tone(w2, filter_lfo_2).out()

s.gui(locals())

