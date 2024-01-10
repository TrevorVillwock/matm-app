import pyo
import wx
import numpy as np

# base class (also called a superclass or parent class)
#
# has variables and methods shared between all instruments 
# variables and methods are called "class members"
class Instrument():
    def __init__(self, tempo, num_beats, subdivision):
        self.click = pyo.Metro(tempo).play()
        self.trigger = pyo.TrigFunc(self.click, self.play)
        # we need to store the speed change here first so the Metro object can be updated by play_main()
        # on the next beat
        self.speed = tempo         
        self.counter = pyo.Sig(pyo.Counter(self.click, min=1, max=num_beats * subdivision + 1))
        self.rhythm = [1, 1, 1, 1,
                       1, 1, 1, 1,
                       1, 1, 1, 1, 
                       1, 1, 1, 1]

    def play(self):
        count = int(self.counter.get())
        self.sample.mul = pyo.RandInt(100) / 100
        
        if self.rhythm[count - 1]:
            self.sample.out()

# derived classes (also called a subclass or child class)
# these have class members that differ between instruments
class Hihat(Instrument):
    def __init__(self, tempo, num_beats, subdivision, control_window): 
        super().__init__(tempo, num_beats, subdivision)
        self.sample = pyo.SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav")  
        self.tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 30), minValue=2, maxValue=10)
        self.tuplet_slider.Bind(wx.EVT_SLIDER, self.set_tuplet)
        self.tuplet_slider_label = wx.StaticText(control_window, label="hihat tuplet", pos=(10, 10))
        self.rhythm = [1, 1, 1, 1,
                       1, 1, 1, 1,
                       1, 1, 1, 1, 
                       1, 1, 1, 1]
        
        
        # self.rhythm = np.repeat(1, 16)

    def set_tuplet(self, e):
        self.speed = 1.0 / e.GetEventObject().GetValue()
        print(f"hihat: {1 / self.speed}")

class Snare(Instrument):
    def __init__(self, tempo, num_beats, subdivision, control_window):
        super().__init__(tempo, num_beats, subdivision)
        self.sample = pyo.SfPlayer("./samples/snare/rhh_snare_one_shot_mid_short_old.wav")
        self.tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 70), minValue=2, maxValue=10)
        self.tuplet_slider.Bind(wx.EVT_SLIDER, self.set_tuplet)
        self.tuplet_slider_label = wx.StaticText(control_window, label="snare tuplet", pos=(10, 50))
        self.rhythm = [0, 0, 0, 0,
                       1, 0, 0, 0,
                       0, 0, 0, 0, 
                       1, 0, 0, 0]
        
        # self.rhythm = np.repeat(1, 16)

    
    def set_tuplet(self, e):
        self.speed = 1.0 / e.GetEventObject().GetValue()
        print(f"snare: {1 / self.speed}")

class Kick(Instrument):
    def __init__(self, tempo, num_beats, subdivision, control_window):
        super().__init__(tempo, num_beats, subdivision)
        self.sample = pyo.SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav")
        self.tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 110), minValue=2, maxValue=10)
        self.tuplet_slider.Bind(wx.EVT_SLIDER, self.set_tuplet)
        self.tuplet_slider_label = wx.StaticText(control_window, label="kick tuplet", pos=(10, 90))
        self.rhythm = [1, 0, 0, 0,
                       0, 0, 0, 0,
                       1, 0, 0, 0, 
                       0, 0, 0, 0]
        
        # self.rhythm = np.repeat(1, 16)
            
    def set_tuplet(self, e):
        self.speed = 1.0 / e.GetEventObject().GetValue()
        print(f"kick: {1 / self.speed}")
        
        