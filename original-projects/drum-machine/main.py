# TODO:
# make Instrument superclass
# Sync tempo changes
# Add effects
# Add controls for density and variation to each instrument
# Add multiple layers of hihat
# Add drag and drop for samples
# Create number boxes to display tuplets
# Create grid to visualize polyrhythms
# switch to tkinter?
# resolve dependency issues

import pyo
import wx
import numpy as np
from instruments import Hihat, Snare, Kick

s = pyo.Server().boot()
s.start()

app = wx.App(False)

control_window = wx.Frame(None, wx.ID_ANY, "Drum Machine")
control_window.Show(True)

num_beats = 4
subdivision = 4
tempo = 0.25

main_click = pyo.Metro(tempo).play()

hihat = Hihat(tempo, num_beats, subdivision, control_window)
snare = Snare(tempo, num_beats, subdivision, control_window)
kick = Kick(tempo, num_beats, subdivision, control_window)
      
def play_main():
    # update instrument speeds on downbeat to keep rhythmic alignment
    hihat.click.setTime(hihat.speed)
    snare.click.setTime(snare.speed)
    kick.click.setTime(kick.speed)

main = pyo.TrigFunc(main_click, play_main)

app.MainLoop()