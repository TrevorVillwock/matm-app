import pyo
import wx
import numpy as np
import json
from instruments import Hihat, Snare, Kick

s = pyo.Server().boot()
s.start()


with open("settings.json", 'r') as file:
    data = json.load(file)
    
print(data)

s.recordOptions(filename = f"./drum_machine_take{data['take_number']}.wav")

new_take_number = data['take_number'] + 1

with open("settings.json", 'w') as file:
    data = json.dump({"take_number": new_take_number}, file)

#data.write()
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