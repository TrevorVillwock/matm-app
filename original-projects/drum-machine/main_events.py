from pyo import Server, Events, EventSeq, Freeverb, Sig
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

"""
preset parameters organized by instrument
tuplet
rhythmic pattern
bpm
sample tuning

"""
presets = data["presets"]

with open("settings.json", 'w') as file:
    data = json.dump({"take_number": new_take_number}, file)
            
BPM = 124

# We tell the Events object which instrument to use with the 'instr' argument.
hihat1 = Events(
    instr=HiHat,
    beat=0.333,
    amp=EventSeq([1, 0, 1, 0, 1]),
    bpm=BPM,
    sample_speed=0.7,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

hihat2 = Events(
    instr=HiHat,
    beat=0.5,
    amp=EventSeq([1, 0, 1, 0, 1]),
    bpm=BPM,
    sample_speed=1.0,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

hihat3 = Events(
    instr=HiHat,
    beat=0.2,
    amp=EventSeq([1, 1, 1, 1, 1]),
    bpm=BPM,
    sample_speed=1.0,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()
 
snare = Events(
    instr=Snare,
    beat=0.5,
    amp=EventSeq([0, 0, 1, 0, 0, 0, 1, 0]), # amp = amplitude = volume
    bpm=BPM,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

kick = Events(
    instr=Kick,
    beat=0.5,
    amp=EventSeq([1, 0, 0, 0, 1, 0, 0, 0,
                  1, 0, 0, 0, 1, 0, 0, 1]),
    bpm=BPM,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
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

    # print(bpm)

def set_tuplet(time, instrument):
    instrument["beat"] = EventSeq([1 / time])
    
def set_sample_speed(speed, instrument):
    instrument["sample_speed"] = EventSeq([speed])

### GUI ###

root = ctk.CTk()

def toggle_reverb(button, instrument):
    # print(button)
    current_color = button.cget("fg_color")
    # print(instrument["effects"])
    # print(instrument)
    if current_color == "black":
        instrument["reverb_is_on"].setValue(1)
        button.configure(fg_color="green")
        #instrument.instr.effects.reverb_is_on = 1
    else:
        instrument["reverb_is_on"].setValue(0)
        button.configure(fg_color="black")
        # instrument.instr.effects.reverb_is_on = 0
    
def toggle_delay(button, instrument):
    # print(instrument)
    current_color = button.cget("fg_color")
    if current_color == "black":
        button.configure(fg_color="green")
        instrument["delay_is_on"].setValue(1)
    else:
        button.configure(fg_color="black")
        instrument["delay_is_on"].setValue(0)

bpm_label = ctk.CTkLabel(root, text='BPM')
bpm_slider = ctk.CTkSlider(root, command=set_bpm, from_=60, to=200)
bpm_label.pack(pady=10)
bpm_slider.pack(pady=10)

hihat1_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="black")
hihat1_reverb_toggle = partial(toggle_reverb, button=hihat1_reverb_button, instrument=hihat1)
hihat1_reverb_button.configure(command=hihat1_reverb_toggle)

hihat1_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="black")
hihat1_delay_toggle = partial(toggle_delay, button=hihat1_delay_button, instrument=hihat1)
hihat1_delay_button.configure(command=hihat1_delay_toggle)

hihat1_reverb_button.pack(pady=20)
hihat1_delay_button.pack(pady=20)

hihat1_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuplet')
hihat1_set_tuplet = partial(set_tuplet, instrument=hihat1)
hihat1_tuplet_slider = ctk.CTkSlider(root, command=hihat1_set_tuplet, from_=1, to=12)

hihat1_tuplet_slider_label.pack(pady=10)
hihat1_tuplet_slider.pack(pady=10)

hihat1_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuning')
hihat1_set_sample_speed = partial(set_sample_speed, instrument=hihat1)
hihat1_tuning_slider = ctk.CTkSlider(root, command=hihat1_set_sample_speed, from_=0.1, to=2.0)

hihat1_tuning_slider_label.pack(pady=10)
hihat1_tuning_slider.pack(pady=10)

hihat2_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="black")
hihat2_reverb_toggle = partial(toggle_reverb, button=hihat2_reverb_button, instrument=hihat2)
hihat2_reverb_button.configure(command=hihat2_reverb_toggle)

hihat2_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="black")
hihat2_delay_toggle = partial(toggle_delay, button=hihat2_delay_button, instrument=hihat2)
hihat2_delay_button.configure(command=hihat2_delay_toggle)

hihat2_reverb_button.pack(pady=20)
hihat2_delay_button.pack(pady=20)

hihat2_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuplet')
hihat2_set_tuplet = partial(set_tuplet, instrument=hihat2)
hihat2_tuplet_slider = ctk.CTkSlider(root, command=hihat2_set_tuplet, from_=1, to=12)
hihat2_tuplet_slider.configure(command=hihat2_set_tuplet)

hihat2_tuplet_slider_label.pack(pady=10)
hihat2_tuplet_slider.pack(pady=10)

hihat2_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuning')
hihat2_set_sample_speed = partial(set_sample_speed, instrument=hihat2)
hihat2_tuning_slider = ctk.CTkSlider(root, command=hihat2_set_sample_speed, from_=0.1, to=2.0)

hihat2_tuning_slider_label.pack(pady=10)
hihat2_tuning_slider.pack(pady=10)

hihat3_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="black")
hihat3_reverb_toggle = partial(toggle_reverb, button=hihat3_reverb_button, instrument=hihat3)
hihat3_reverb_button.configure(command=hihat3_reverb_toggle)

hihat3_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="black")
hihat3_delay_toggle = partial(toggle_delay, button=hihat3_delay_button, instrument=hihat3)
hihat3_delay_button.configure(command=hihat3_delay_toggle)

hihat3_reverb_button.pack(pady=20)
hihat3_delay_button.pack(pady=20)

hihat3_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuplet')
hihat3_set_tuplet = partial(set_tuplet, instrument=hihat3)
hihat3_tuplet_slider = ctk.CTkSlider(root, command=hihat3_set_tuplet, from_=1, to=12)
hihat3_tuplet_slider.configure(command=hihat3_set_tuplet)
hihat3_tuplet_slider_label.pack(pady=10)
hihat3_tuplet_slider.pack(pady=10)

hihat3_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuning')
hihat3_tuning_slider_label.pack(pady=10)
hihat3_set_sample_speed = partial(set_sample_speed, instrument=hihat3)
hihat3_tuning_slider = ctk.CTkSlider(root, command=hihat3_set_sample_speed, from_=0.1, to=2.0)
hihat3_tuning_slider.pack(pady=10)

root.mainloop()