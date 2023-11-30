from pyo import *
from random import uniform
import wx

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

class Score:
    def __init__(self):
        self.part1 = Adsr(2, 1, 0.5, 1, 0.5)
        self.part2 = Adsr(2, 1, 0.5, 1, 0.5)
        self.part3 = Adsr(1, 1, 0.5, 1, 1)
        self.part4 = Adsr(1, 1, 0.5, 1, 1)
        self.part1.ctrl()
        self.part2.ctrl()
        self.part3.ctrl()
        self.part4.ctrl()
        
    def add(self, instrument, part):
        instrument.mul = getattr(self, "part" + str(part))
        
    def play(self):
        self.part1.play()
        self.part2.play()
        self.part3.play()
        self.part4.play()
        
    def stop(self):
        self.part1.stop()
        self.part2.stop()
        self.part3.stop()
        self.part4.stop()

class Step_seq:
    def __init__(self, scale):
        self.filter_lfo = Sine(random.uniform(0.5, 20)).range(500, 2000)
        self.speed_lfo = Sine(random.uniform(0.5, 20)).range(1, 20)
        self.notes = scale
        self.random_note = Choice(self.notes, self.speed_lfo)
        self.synth = SuperSaw([self.random_note, self.random_note])
        self.filter = MoogLP(self.synth, self.filter_lfo)
        # self.filter.ctrl()

class Seq_manager:
    def __init__(self):
        self.step_sequencers = []
        self.active_voices = 0
    
    def set_num_voices(self, num):
        i = self.active_voices - 1
        if num < self.active_voices - 1:  
            # print("if") 
            while i >= num:
                synth_mixer.setAmp(i, 0, 0)
                i -= 1
                self.active_voices -= 1    
        elif num > self.active_voices and num < 10:
            # print("elif")
            while i <= 9:
                # print("while")
                synth_mixer.setAmp(i, 0, 0.01)
                self.active_voices += 1
                i += 1

#voices_slider = PyoGuiControlSlider()
#voices_slider.enable()   
score = Score()        
sm = Seq_manager()

synth_mixer = Mixer(outs=3, chnls=2, time=0.5).out()

score.add(synth_mixer, 1)  

audio_file = SfPlayer("./bamboo_chimes.wav", speed=-0.5, loop=True, mul=0.3)
audio_file.ctrl()

sfdelay = Delay(audio_file, delay=[1, 2], feedback=.5).out()
score.add(sfdelay, 2)
sfdelay.ctrl()

for i in range(0, 10):
    new_step_seq = Step_seq(natural_minor)
    sm.step_sequencers.append(new_step_seq)
    synth_mixer.addInput(i, new_step_seq.filter)
    synth_mixer.setAmp(i, 0, 0.05)
    sm.active_voices += 1

score.play()
s.gui(locals())

app =wx.App(False)
control_window = wx.Frame(None, wx.ID_ANY, "Hello")
control_window.Show(True)
#app.MainLoop()