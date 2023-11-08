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
# scale choices
harmonic_series = [100, 200, 300, 400, 500, 600, 700, 800]
whole_tone = midiToHz([60, 62, 64, 66, 68, 70, 72])
major = midiToHz([60, 62, 64, 65, 67, 69, 71, 72])
natural_minor = midiToHz([60, 62, 63, 65, 67, 68, 70, 72])
major_pent = midiToHz([60, 62, 64, 67, 69, 72])
minor_pent = midiToHz([60, 63, 65, 67, 70, 72])

class step_sequencer:
    
filter_lfo_1 = Sine(freq=1, mul=1000, add=1000)
speed_lfo_1 = Sine(freq=0.1, mul=20, add=1)
random_note_1 = Choice(major, speed_lfo_1)
w1 = SuperSaw([random_note_1, random_note_1])
f1 = Tone(w1, filter_lfo_1).out()

filter_lfo_2 = Sine(freq=0.3, mul=1000, add=1000)
speed_lfo_2 = Sine(freq=0.1, mul=20, add=2)
random_note_2 = Choice(major, speed_lfo_2)
w2 = SuperSaw([random_note_2, random_note_2])
f2 = Tone(w2, filter_lfo_2).out()

s.gui(locals())

