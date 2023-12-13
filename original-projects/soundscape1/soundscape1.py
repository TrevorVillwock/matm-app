from pyo import *
from random import uniform
import wx

s = Server().boot()

# This tells pyo to place the recording in the same directory as the file and name it test.wav

s.recordOptions(filename = "./soudscape1.wav")
s.recstart()

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

class StepSeq:
    def __init__(self, scale):
        self.filter_lfo = Sine(random.uniform(0.5, 20)).range(500, 2000)
        self.speed_lfo = Sine(random.uniform(0.5, 20)).range(1, 20)
        self.notes = scale
        self.random_note = Choice(self.notes, self.speed_lfo)
        self.synth = SuperSaw([self.random_note, self.random_note])
        self.filter = MoogLP(self.synth, self.filter_lfo)
        # self.filter.ctrl()

class SeqManager:
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
                synth_mixer.setAmp(i, 0, 0.07)
                self.active_voices += 1
                i += 1
       
sm = SeqManager()

synth_mixer = Mixer(outs=3, chnls=2, time=0.5).out()

audio_file = SfPlayer("./bamboo_chimes.wav", speed=-0.5, loop=True, mul=0.3)
audio_file.ctrl()

sfdelay = Delay(audio_file, delay=[1, 2], feedback=.5).out()
sfdelay.ctrl()

for i in range(0, 10):
    new_step_seq = StepSeq(natural_minor)
    sm.step_sequencers.append(new_step_seq)
    synth_mixer.addInput(i, new_step_seq.filter)
    synth_mixer.setAmp(i, 0, 0.07)
    sm.active_voices += 1

def event_0():
    print("event_0")
    
def event_1():
    print("event_1")
    sm.set_num_voices(1)
    
def event_2():
    print("event_2")
    sm.set_num_voices(3)
    
def event_3():
    print("event_3")
    audio_file.speed = 1.0
    
def num_synths_slider_move(e):
    sm.set_num_voices(e.GetEventObject().GetValue())

def sf_speed_slider_move(e):
    audio_file.speed = e.GetEventObject().GetValue() / 200
    
def delay_time_slider_move(e):
    delay_time = e.GetEventObject().GetValue() / 2000
    sfdelay.delay = [delay_time, delay_time]

metro = Metro(4).play()
count = Counter(metro, min=0, max=8)
score = Score(count, fname="event_")

app = wx.App(False)
control_window = wx.Frame(None, wx.ID_ANY, "Soundscape 1")
control_window.Show(True)

num_synths_slider = wx.Slider(control_window, pos=wx.Point(0, 30), minValue=1, maxValue=10)
num_synths_slider.Bind(wx.EVT_SLIDER, num_synths_slider_move)
num_synths_slider_label = wx.StaticText(control_window, label="synth voices", pos=(10, 10))

sf_speed_slider = wx.Slider(control_window, pos=wx.Point(0, 70), minValue=-200, maxValue=200)
sf_speed_slider.Bind(wx.EVT_SLIDER, sf_speed_slider_move)
sf_speed_slider_label = wx.StaticText(control_window, label="soundfile speed", pos=(10, 50))

delay_time_slider = wx.Slider(control_window, pos=(0, 110), minValue=1, maxValue=2000)
delay_time_slider.Bind(wx.EVT_SLIDER, delay_time_slider_move)
delay_time_slider_label = wx.StaticText(control_window, label="delay time", pos=(10, 90))

s.start()
app.MainLoop()

s.recstop()