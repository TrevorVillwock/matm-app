from pyo import *
from random import uniform

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
    def __init__(self, scale):
        self.filter_lfo = Sine(random.uniform(0.5, 20)).range(500, 2000)
        self.speed_lfo = Sine(random.uniform(0.5, 20)).range(1, 20)
        self.notes = scale
        self.random_note = Choice(self.notes, self.speed_lfo)
        self.synth = SuperSaw([self.random_note, self.random_note])
        self.filter = MoogLP(self.synth, self.filter_lfo)
        self.filter.ctrl()

step_sequencers = []

mixer = Mixer(outs=3, chnls=2, time=0.5).out()

audio_file = SfPlayer("./bamboo_chimes.wav", speed=-0.3, loop=True)
audio_file.ctrl()

delay = Delay(audio_file, delay=[1,1], feedback=.5, mul=.4)
delay.ctrl()

# audio_file = SfMarkerShuffler("./oboe_multiphonics.aif")
# audio_file.setRandomType(9, 0.5)
# audio_file.ctrl()

for i in range(0, 10):
    new_step_seq = Step_seq(natural_minor)
    step_sequencers.append(new_step_seq)
    mixer.addInput(i, new_step_seq.filter)
    mixer.setAmp(i, 0, 0.01)
    
mixer.addInput(10, delay)
mixer.setAmp(10, 0, 0.5)

s.gui(locals())

