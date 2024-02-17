# import pyo
from pyo import EventInstrument, SmoothDelay, Sig, Selector, Freeverb, Phasor, Expseg, ButLP, SfPlayer, Server, Events, EventSeq, EventChoice
import json
from instruments_events import HiHat, Snare, Kick
# from gui import DrumMachineGUI
import tkinter as tk
import customtkinter as ctk
import time

s = Server().boot()
s.start()

with open("settings.json", 'r') as file:
    data = json.load(file)

# s.recordOptions(filename = f"./drum_machine_take{data['take_number']}.wav")

new_take_number = data['take_number'] + 1

with open("settings.json", 'w') as file:
    data = json.dump({"take_number": new_take_number}, file)
            
BPM = 100

# We tell the Events object which instrument to use with the 'instr' argument.
hihat1 = Events(
    instr=HiHat,
    beat=0.333,
    amp=EventSeq([1, 0, 1, 0, 1]),
    bpm=BPM,
    sample_speed=0.7
).play()

hihat2 = Events(
    instr=HiHat,
    beat=0.5,
    amp=EventSeq([1, 0, 1, 0, 1]),
    bpm=BPM,
    sample_speed=1.0
).play()

hihat3 = Events(
    instr=HiHat,
    beat=0.2,
    amp=EventSeq([1, 1, 1, 1, 1]),
    bpm=BPM,
    sample_speed=1.0
).play()
 
snare = Events(
    instr=Snare,
    beat=1,
    amp=EventSeq([0, 1, 0]), # amp = amplitude = volume
    bpm=BPM
).play()

kick = Events(
    instr=Kick,
    beat=1,
    amp=EventSeq([1, 0]),
    bpm=BPM
).play()

instruments = [hihat1, hihat2, hihat3, snare, kick]

def set_bpm(bpm):
    print(bpm)
    for i in instruments:
        # time1 = time.perf_counter_ns()
        i["bpm"] = bpm
        # time2 = time.perf_counter_ns()
        # print(time2-time1)
        
def set_hihat1_tuplet(time):
    hihat1["beat"] = EventSeq([1 / time])
    
def set_hihat2_tuplet(time):
    hihat2["beat"] = EventSeq([1 / time])

def set_hihat3_tuplet(time):
    hihat3["beat"] = EventSeq([1 / time])
    
def set_hihat1_sample_speed(speed):
    hihat1["sample_speed"] = EventSeq([speed])
    
def set_hihat2_sample_speed(speed):
    hihat2["sample_speed"] = EventSeq([speed])
    
def set_hihat3_sample_speed(speed):
    hihat3["sample_speed"] = EventSeq([speed])

### GUI ###

root = ctk.CTk()

bpm_label = ctk.CTkLabel(root, text='BPM')
bpm_label.pack(pady=10)
bpm_slider = ctk.CTkSlider(root, command=set_bpm, from_=60, to=200)
bpm_slider.pack(pady=10)

hihat1_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuplet')
hihat1_tuplet_slider_label.pack(pady=10)
hihat1_tuplet_slider = ctk.CTkSlider(root, command=set_hihat1_tuplet, from_=1, to=12)
hihat1_tuplet_slider.pack(pady=10)

hihat1_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuning')
hihat1_tuning_slider_label.pack(pady=10)
hihat1_tuning_slider = ctk.CTkSlider(root, command=set_hihat1_sample_speed, from_=0.1, to=2.0)
hihat1_tuning_slider.pack(pady=10)

hihat2_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuplet')
hihat2_tuplet_slider_label.pack(pady=10)
hihat2_tuplet_slider = ctk.CTkSlider(root, command=set_hihat1_tuplet, from_=1, to=12)
hihat2_tuplet_slider.pack(pady=10)

hihat2_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuning')
hihat2_tuning_slider_label.pack(pady=10)
hihat2_tuning_slider = ctk.CTkSlider(root, command=set_hihat2_sample_speed, from_=0.1, to=2.0)
hihat2_tuning_slider.pack(pady=10)

hihat3_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuplet')
hihat3_tuplet_slider_label.pack(pady=10)
hihat3_tuplet_slider = ctk.CTkSlider(root, command=set_hihat1_tuplet, from_=1, to=12)
hihat3_tuplet_slider.pack(pady=10)

hihat3_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuning')
hihat3_tuning_slider_label.pack(pady=10)
hihat3_tuning_slider = ctk.CTkSlider(root, command=set_hihat3_sample_speed, from_=0.1, to=2.0)
hihat3_tuning_slider.pack(pady=10)

print(hihat1["bpm"])
root.mainloop()




#gui = DrumMachineGUI()
#print(gui)

# root.mainloop()

# control_window = wx.Frame(None, wx.ID_ANY, "Drum Machine")
# control_window.Show(True)

# num_beats = 4
# subdivision = 4
# tempo = 0.25

# main_click = pyo.Metro(tempo).play()

# hihat = HiHat(tempo, num_beats, subdivision, control_window)
# snare = Snare(tempo, num_beats, subdivision, control_window)
# kick = Kick(tempo, num_beats, subdivision, control_window)

# mixer = pyo.Mixer(outs=2, chnls=3)
# mixer.addInput(0, hihat.reverb_selector)
# mixer.addInput(1, snare.reverb_selector)
# mixer.addInput(2, kick.reverb_selector)
# mixer.setAmp(0, 0, 0.3)
# mixer.setAmp(1, 0, 0.3)
# mixer.setAmp(2, 0, 0.3)

# recorder = pyo.Record(mixer, "./test.wav")
      
# def play_main():
#     # update instrument speeds on downbeat to keep rhythmic alignment
#     hihat.click.setTime(hihat.speed)
#     hihat.click.play()
#     snare.click.setTime(snare.speed)
#     kick.click.setTime(kick.speed)
#     # print("play_main")

# main = pyo.TrigFunc(main_click, play_main)