from pyo import Server, Events, EventSeq
import json
from instruments_events import HiHat, Snare, Kick
import tkinter as tk
import customtkinter as ctk
from threading import Thread
from functools import partial
# import time
# from gui import DrumMachineGUI

s = Server().boot()
s.start()

with open("settings.json", 'r') as file:
    data = json.load(file)

s.recordOptions(filename = f"./drum_machine_take{data['take_number']}.wav")

new_take_number = data['take_number'] + 1

with open("settings.json", 'w') as file:
    data = json.dump({"take_number": new_take_number}, file)
            
BPM = 124

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
    beat=0.5,
    amp=EventSeq([0, 0, 1, 0, 0, 0, 1, 0]), # amp = amplitude = volume
    bpm=BPM
).play()

kick = Events(
    instr=Kick,
    beat=0.25,
    amp=EventSeq([1, 0, 0, 0, 1, 1, 0, 0]),
    bpm=BPM
).play()

instruments = [hihat1, hihat2, hihat3, snare, kick]

# original code
# def set_bpm(bpm):
#     print(bpm)
#     for i in instruments:
#         # time1 = time.perf_counter_ns()
#         i["bpm"] = bpm
#         # time2 = time.perf_counter_ns()
#         # print(time2-time1)

# GPT-4 conversion to parallel processing using threads an explanation 
# of the muse of multitheading vs multiprocessing 
# In the context of the provided code snippet, using multithreading with threading.Thread seems appropriate because the task of updating the BPM of instruments doesn't involve heavy computation or I/O operations that would benefit significantly from multiprocessing.
# However, if the task performed by change_bpm() involved computationally intensive operations or blocking I/O tasks (such as network or file operations), multiprocessing might be a better choice. Multiprocessing would allow you to take advantage of multiple CPU cores 
# and execute the tasks concurrently in separate processes, potentially providing better performance.

# In summary:

# Use multithreading (threading.Thread) when your tasks involve I/O-bound operations or when you want to run multiple tasks concurrently within the same process.
# Use multiprocessing (multiprocessing.Process) when your tasks involve CPU-bound operations or when you want to take advantage of multiple CPU cores by executing tasks in separate processes.

def set_bpm(bpm):
    def set(instrument):
        instrument["bpm"] = bpm

    threads = [Thread(target=set, args=(instr,)) for instr in instruments]
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(bpm)

# single function set_tuplet that takes an instrument as an argument,
# finds its name, and then acess that object's "beat" attribute

def set_tuplet(time, arg1):
    arg1["beat"] = EventSeq([1 / time])

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

def toggle_color(button):
    print(button)
    # current_color = button.cget("bg")
    # if current_color == "red":
    #     button.config(bg="green")
    # else:
    #     button.config(bg="red")




bpm_label = ctk.CTkLabel(root, text='BPM')
bpm_label.pack(pady=10)
bpm_slider = ctk.CTkSlider(root, command=set_bpm, from_=60, to=200)
bpm_slider.pack(pady=10)

hihat1_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="red", command=toggle_color)
hihat1_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="red", command=toggle_color)
hihat1_reverb_button.pack(pady=20)
hihat1_delay_button.pack(pady=20)

hihat1_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuplet')
hihat1_tuplet_slider = ctk.CTkSlider(root, command=set_hihat1_tuplet, from_=1, to=12)
hihat1_set_tuplet = partial(set_tuplet, arg1=hihat1)
hihat1_tuplet_slider.configure(command=hihat1_set_tuplet)
hihat1_tuplet_slider_label.pack(pady=10)
hihat1_tuplet_slider.pack(pady=10)

hihat1_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuning')
hihat1_tuning_slider = ctk.CTkSlider(root, command=set_hihat1_sample_speed, from_=0.1, to=2.0)
hihat1_tuning_slider_label.pack(pady=10)
hihat1_tuning_slider.pack(pady=10)

hihat2_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="red", command=toggle_color)
hihat2_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="red", command=toggle_color)
hihat2_reverb_button.pack(pady=20)
hihat2_delay_button.pack(pady=20)

hihat2_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuplet')
hihat2_tuplet_slider = ctk.CTkSlider(root, command=set_hihat2_tuplet, from_=1, to=12)
hihat2_tuplet_slider_label.pack(pady=10)
hihat2_tuplet_slider.pack(pady=10)

hihat2_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuning')
hihat2_tuning_slider = ctk.CTkSlider(root, command=set_hihat2_sample_speed, from_=0.1, to=2.0)
hihat2_tuning_slider_label.pack(pady=10)
hihat2_tuning_slider.pack(pady=10)

hihat2_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="red", command=toggle_color)
hihat2_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="red", command=toggle_color)
hihat2_reverb_button.pack(pady=20)
hihat2_delay_button.pack(pady=20)

hihat3_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuplet')
hihat3_tuplet_slider = ctk.CTkSlider(root, command=set_hihat1_tuplet, from_=1, to=12)
hihat3_tuplet_slider_label.pack(pady=10)
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