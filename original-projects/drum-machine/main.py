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
# main_click.ctrl()

hihat = Hihat(tempo, num_beats, subdivision, control_window)
snare = Snare(tempo, num_beats, subdivision, control_window)
kick = Kick(tempo, num_beats, subdivision, control_window)
print(hihat.rhythm)
      
def play_main():
    # update instrument speeds on downbeat to keep rhythmic alignment
    hihat.click.setTime(hihat.speed)
    hihat.click.play()
    snare.click.setTime(snare.speed)
    kick.click.setTime(kick.speed)
    # print("play_main")

main = pyo.TrigFunc(main_click, play_main)

s.gui(locals)

app.MainLoop()