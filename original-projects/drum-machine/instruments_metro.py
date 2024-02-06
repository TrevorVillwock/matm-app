import pyo
import wx
import numpy as np

# base class (also called a superclass or parent class)
#
# has variables and methods shared between all instruments 
# variables and methods are called "class members"
# 
class Instrument():
    def __init__(self, tempo, num_beats, subdivision):
        self.click = pyo.Metro(tempo).play()
        self.trigger = pyo.TrigFunc(self.click, self.play)
        # we need to store the speed change here first so the Metro object can be updated by play_main()
        # on the next beat
        self.speed = tempo         
        self.counter = pyo.Sig(pyo.Counter(self.click, min=1, max=num_beats * subdivision + 1))
        # 1 = note, 0 = rest
        
        self.sample = pyo.SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav")
        self.delay = pyo.SmoothDelay(self.sample, delay=0.333, feedback=0.7)
        self.delay_is_on = pyo.Sig(1)
        self.delay_selector = pyo.Selector([self.sample, self.delay], self.delay_is_on) 
        self.reverb_is_on = pyo.Sig(1)
        self.reverb = pyo.Freeverb(self.delay_selector)
        self.reverb_selector = pyo.Selector([self.delay_selector, self.reverb], self.reverb_is_on)
        
        self.rhythm = [1, 1, 1, 1,
                       1, 1, 1, 1,
                       1, 1, 1, 1, 
                       1, 1, 1, 1]
        
    def play(self):
        count = int(self.counter.get())
        # mul = volume
        self.sample.mul = pyo.RandInt(100) / 100
        
        if self.rhythm[count - 1]:
            self.sample.out()
            
    def toggleDelay(self, command):
        print(command)
        if self.delay_is_on.value:
            self.delay_is_on.setValue(0)
        else:
            self.delay_is_on.setValue(1)
        print(f"delay: {self.delay_is_on._value}")  
        
    def toggleReverb(self, command):
        print(command)
        if self.reverb_is_on.value:
            self.reverb_is_on.setValue(0)
        else:
            self.reverb_is_on.setValue(1)
        print(f"reverb: {self.reverb_is_on._value}")

# derived classes (also called a subclass or child class)
# these have class members that differ between instruments
class Hihat(Instrument):
    def __init__(self, tempo, num_beats, subdivision, control_window): 
        super().__init__(tempo, num_beats, subdivision)
        self.sample = pyo.SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav")
        self.delay.input = self.sample
        
        # TODO: add increment for slider and label positions  
        self.tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 30), minValue=2, maxValue=10)
        self.tuplet_slider.Bind(wx.EVT_SLIDER, self.set_tuplet)
        self.tuplet_slider_label = wx.StaticText(control_window, label="hihat tuplet", pos=(10, 10))
        
        self.delay_button = wx.Button(control_window, label="toggle delay", pos=wx.Point(160, 30))
        self.delay_button.Bind(wx.EVT_BUTTON, self.toggleDelay)
        self.reverb_button = wx.Button(control_window, label="toggle reverb", pos=wx.Point(260, 30))
        self.reverb_button.Bind(wx.EVT_BUTTON, self.toggleReverb)
        
        self.rhythm = [0, 1, 1, 1,
                       1, 1, 0, 1,
                       1, 1, 1, 0, 
                       0, 1, 0, 1]
        
        # self.rhythm = np.repeat(1, 16)

    def set_tuplet(self, e):
        self.speed = 1.0 / e.GetEventObject().GetValue()
        print(f"hihat: {1 / self.speed}")

class Snare(Instrument):
    def __init__(self, tempo, num_beats, subdivision, control_window):
        super().__init__(tempo, num_beats, subdivision)
        self.sample = pyo.SfPlayer("./samples/snare/rhh_snare_one_shot_mid_short_old.wav")
        self.delay.input = self.sample
        
        self.tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 70), minValue=2, maxValue=10)
        self.tuplet_slider.Bind(wx.EVT_SLIDER, self.set_tuplet)
        self.tuplet_slider_label = wx.StaticText(control_window, label="snare tuplet", pos=(10, 50))
        
        self.delay_button = wx.Button(control_window, label="toggle delay", pos=wx.Point(160, 70))
        self.delay_button.Bind(wx.EVT_BUTTON, self.toggleDelay)
        self.reverb_button = wx.Button(control_window, label="toggle reverb", pos=wx.Point(260, 70))
        self.reverb_button.Bind(wx.EVT_BUTTON, self.toggleReverb)
        
        self.rhythm = [0, 0, 0, 0,
                       1, 0, 0, 0,
                       0, 0, 0, 0, 
                       0, 1, 0, 1]        
        
        # self.rhythm = np.repeat(1, 16)
    
    def set_tuplet(self, e):
        self.speed = 1.0 / e.GetEventObject().GetValue()
        print(f"snare: {1 / self.speed}")

class Kick(Instrument):
    def __init__(self, tempo, num_beats, subdivision, control_window):
        super().__init__(tempo, num_beats, subdivision)
        self.sample = pyo.SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav")
        self.delay.input = self.sample
        
        self.tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 110), minValue=2, maxValue=10)
        self.tuplet_slider.Bind(wx.EVT_SLIDER, self.set_tuplet)
        self.tuplet_slider_label = wx.StaticText(control_window, label="kick tuplet", pos=(10, 90))
        
        self.delay_button = wx.Button(control_window, label="toggle delay", pos=wx.Point(160, 110))
        self.delay_button.Bind(wx.EVT_BUTTON, self.toggleDelay)
        self.reverb_button = wx.Button(control_window, label="toggle reverb", pos=wx.Point(260, 110))
        self.reverb_button.Bind(wx.EVT_BUTTON, self.toggleReverb)
        
        self.rhythm = [1, 0, 0, 0,
                       0, 0, 1, 0,
                       0, 1, 0, 1, 
                       0, 0, 1, 0]

        # self.rhythm = np.repeat(1, 16)
            
    def set_tuplet(self, e):
        self.speed = 1.0 / e.GetEventObject().GetValue()
        print(f"kick: {1 / self.speed}")
        
        