import pyo
import wx
import numpy as np

class Hihat():
    def __init__(self, tempo, num_beats, subdivision, control_window):
        self.sample = pyo.SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav")
        self.click = pyo.Metro(tempo).play()
        self.trigger = pyo.TrigFunc(self.click, self.play)
        # we need to store the speed change here first so it can be updated by play_main()
        # on the next beat
        self.speed = tempo         
        self.counter = pyo.Sig(pyo.Counter(self.click, min=1, max=num_beats * subdivision + 1))
        self.tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 30), minValue=2, maxValue=10)
        self.tuplet_slider.Bind(wx.EVT_SLIDER, self.set_tuplet)
        self.hihat_tuplet_slider_label = wx.StaticText(control_window, label="hihat tuplet", pos=(10, 10))

    def set_tuplet(self, e):
        self.speed = 1.0 / e.GetEventObject().GetValue()

    def play(self):
        count = int(self.counter.get())
        self.sample.mul = pyo.RandInt(100) / 100
        
        rhythm = [1, 1, 0, 1,
                1, 0, 0, 1,
                0, 1, 1, 1, 
                0, 1, 0, 1]
        
        # rhythm = np.repeat(1, 16)
        
        if rhythm[count - 1]:
            self.sample.out()

class Snare():
    def __init__(self, tempo, num_beats, subdivision, control_window):
        self.sample = pyo.SfPlayer("./samples/snare/rhh_snare_one_shot_mid_short_old.wav")
        self.click = pyo.Metro(tempo).play()
        self.speed = tempo
        self.trigger = pyo.TrigFunc(self.click, self.play)
        self.counter = pyo.Sig(pyo.Counter(self.click, min=1, max=num_beats * subdivision + 1))
        self.tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 70), minValue=2, maxValue=10)
        self.tuplet_slider.Bind(wx.EVT_SLIDER, self.set_tuplet)
        self.hihat_tuplet_slider_label = wx.StaticText(control_window, label="snare tuplet", pos=(10, 50))
        
    def play(self):
        count = int(self.counter.get())
        self.sample.mul = 0.75 + pyo.RandInt(100) / 100 * 0.25
        
        rhythm = [0, 0, 0, 0,
                1, 0, 0, 0,
                0, 0, 0, 0, 
                1, 0, 0, 0]
        
        if rhythm[count - 1]:
            self.sample.out()
            
    def set_tuplet(self, e):
        self.speed = 1.0 / e.GetEventObject().GetValue()
        

class Kick():
    def __init__(self, tempo, num_beats, subdivision, control_window):
        self.sample = pyo.SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav")
        self.click = pyo.Metro(tempo).play()
        self.speed = tempo
        self.trigger = pyo.TrigFunc(self.click, self.play)
        self.counter = pyo.Sig(pyo.Counter(self.click, min=1, max=num_beats * subdivision + 1))
        self.tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 110), minValue=2, maxValue=10)
        self.tuplet_slider.Bind(wx.EVT_SLIDER, self.set_tuplet)
        self.hihat_tuplet_slider_label = wx.StaticText(control_window, label="kick tuplet", pos=(10, 90))
                
    def play(self):
        count = int(self.counter.get())
        self.sample.mul = 0.75 + pyo.RandInt(100) / 100 * 0.25
        
        rhythm = [1, 0, 0, 0,
                0, 0, 0, 0,
                0, 1, 0, 0, 
                0, 0, 0, 0]
        
        if rhythm[count - 1]:
            self.sample.out()
            
    def set_tuplet(self, e):
        self.speed = 1.0 / e.GetEventObject().GetValue()