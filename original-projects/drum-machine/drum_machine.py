# TODO:
# Sync tempo changes
# Create sliders for kick and snare
# Add effects
# Create number boxes to display tuplets
# switch to tkinter?
# resolve dependency issues

# from pyo import Metro, Counter, Score, TrigFunc
import pyo
import wx
import numpy as np
import sys

s = pyo.Server().boot()
s.start()

num_beats = 4
subdivision = 4
tempo = 0.25
# tempo = pyo.Sig(0.25) # in milliseconds
# tempo.ctrl()

# samples
kick_sample = pyo.SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav")
snare_sample = pyo.SfPlayer("./samples/snare/rhh_snare_one_shot_mid_short_old.wav")
hihat_sample = pyo.SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav")

hihat_click = pyo.Metro(tempo).play()
hihat_click.ctrl()
snare_click = pyo.Metro(tempo).play()
snare_click.ctrl()
kick_click = pyo.Metro(tempo).play()
kick_click.ctrl()
main_click = pyo.Metro(tempo).play()
main_click.ctrl()

hihat_tempo = 0.25

# Create a signal to represent the count that we can pass to other places 
hihat_counter = pyo.Sig(pyo.Counter(hihat_click, min=1, max=num_beats * subdivision + 1))
snare_counter = pyo.Sig(pyo.Counter(snare_click, min=1, max=num_beats * subdivision + 1))
kick_counter = pyo.Sig(pyo.Counter(kick_click, min=1, max=num_beats * subdivision + 1))

def seconds_to_bpm(time):
    bpm = time * 60
    return bpm

def set_hihat_tuplet(e):
    hihat_tempo = 1.0 / e.GetEventObject().GetValue()
    print(hihat_tempo)
    # hihat_click.setTime(1.0 / e.GetEventObject().GetValue())

# TODO: wrap this in Events or something similar to use a list to populate match statements
def play_hihat():
    count = int(hihat_counter.get())
    hihat_sample.mul = pyo.RandInt(100) / 100
    
    rhythm = [1, 1, 0, 1,
              1, 0, 0, 1,
              0, 1, 1, 1, 
              0, 1, 0, 1]
    
    rhythm = np.repeat(1, 16)
    
    if rhythm[count - 1] == 1:
        hihat_sample.out()

def play_snare():
    count = int(snare_counter.get())
    snare_sample.mul = 0.75 + pyo.RandInt(100) / 100 * 0.25
    
    rhythm = [0, 0, 0, 0,
              1, 0, 0, 0,
              0, 0, 0, 0, 
              1, 0, 0, 0]
    
    if rhythm[count - 1] == 1:
        snare_sample.out()
            
def play_kick():
    count = int(kick_counter.get())
    snare_sample.mul = 0.75 + pyo.RandInt(100) / 100 * 0.25
    
    rhythm = [1, 0, 0, 0,
              0, 0, 0, 0,
              0, 1, 0, 0, 
              0, 0, 0, 0]
    
    if rhythm[count - 1] == 1:
        kick_sample.out()
        
def play_main():
    hihat_click.setTime(hihat_tempo)
    print(hihat_tempo)
    
hihat = pyo.TrigFunc(hihat_click, play_hihat)
snare = pyo.TrigFunc(snare_click, play_snare)
kick = pyo.TrigFunc(kick_click, play_kick)
main = pyo.TrigFunc(main_click, play_main)

app = wx.App(False)

control_window = wx.Frame(None, wx.ID_ANY, "Soundscape 1")
control_window.Show(True)

hihat_tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 30), minValue=2, maxValue=10)
hihat_tuplet_slider.Bind(wx.EVT_SLIDER, set_hihat_tuplet)
hihat_tuplet_slider_label = wx.StaticText(control_window, label="hihat tuplet", pos=(10, 10))

print(sys.__dict__.keys())

app.MainLoop()

s.gui(locals)