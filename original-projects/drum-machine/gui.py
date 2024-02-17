import tkinter as tk
import customtkinter as ctk
from pyo import Server, Events, EventSeq

root = ctk.CTk()

class DrumMachineGUI():
    def __init__(self, root):
        print("GUI INIT")
        self.bpm_label = ctk.CTkLabel(root, text='BPM')
        self.bpm_label.pack(pady=10)
        self.bpm_slider = ctk.CTkSlider(root, from_=60, to=200)
        self.bpm_slider.pack(pady=10)

        self.hihat1_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuplet')
        self.hihat1_tuplet_slider_label.pack(pady=10)
        self.hihat1_tuplet_slider = ctk.CTkSlider(root, from_=1, to=12)
        self.hihat1_tuplet_slider.pack(pady=10)

        self.hihat1_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuning')
        self.hihat1_tuning_slider_label.pack(pady=10)
        self.hihat1_tuning_slider = ctk.CTkSlider(root, from_=1, to=12)
        self.hihat1_tuning_slider.pack(pady=10)

        self.hihat2_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuplet')
        self.hihat2_tuplet_slider_label.pack(pady=10)
        self.hihat2_tuplet_slider = ctk.CTkSlider(root, from_=1, to=12)
        self.hihat2_tuplet_slider.pack(pady=10)

        self.hihat2_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuning')
        self.hihat2_tuning_slider_label.pack(pady=10)
        self.hihat2_tuning_slider = ctk.CTkSlider(root, from_=1, to=12)
        self.hihat2_tuning_slider.pack(pady=10)

        self.hihat3_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuplet')
        self.hihat3_tuplet_slider_label.pack(pady=10)
        self.hihat3_tuplet_slider = ctk.CTkSlider(root, from_=1, to=12)
        self.hihat3_tuplet_slider.pack(pady=10)

        self.hihat3_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuning')
        self.hihat3_tuning_slider_label.pack(pady=10)
        self.hihat3_tuning_slider = ctk.CTkSlider(root, from_=1, to=12)
        self.hihat3_tuning_slider.pack(pady=10)
        
        root.mainloop()

# GPT-4:
# Define the GUI class
# class MusicApp(ctk.CTk):

#     def __init__(self):
#         super().__init__()

#         self.title('Music Instrument GUI')
#         self.geometry('800x600')

#         # HiHat Controls
#         self.create_instrument_controls('HiHat', row=0)

#         # Snare Controls
#         self.create_instrument_controls('Snare', row=1)

#         # Kick Controls
#         self.create_instrument_controls('Kick', row=2)

#         # BPM Control
#         self.bpm_label = ctk.CTkLabel(root, text='BPM')
#         self.bpm_label.grid(row=3, column=0, pady=10)
#         self.bpm_slider = ctk.CTkSlider(root, from_=60, to_=200)
#         self.bpm_slider.grid(row=3, column=1, pady=10)

#         # Play Button
#         self.play_button = ctk.CTkButton(root, text='Play', command=self.play_music)
#         self.play_button.grid(row=4, column=0, columnspan=2, pady=10)

#         # Stop Button
#         self.stop_button = ctk.CTkButton(root, text='Stop', command=self.stop_music)
#         self.stop_button.grid(row=4, column=2, columnspan=2, pady=10)

#     def create_instrument_controls(self, instrument, row):
#         label = ctk.CTkLabel(root, text=instrument)
#         label.grid(row=row, column=0, pady=10)

#         beat_label = ctk.CTkLabel(root, text='Beat')
#         beat_label.grid(row=row, column=1, pady=10)
#         beat_entry = ctk.CTkEntry(root)
#         beat_entry.grid(row=row, column=2, pady=10)

#         amp_label = ctk.CTkLabel(root, text='Amp')
#         amp_label.grid(row=row, column=3, pady=10)
#         amp_entry = ctk.CTkEntry(root)
#         amp_entry.grid(row=row, column=4, pady=10)

#         speed_label = ctk.CTkLabel(root, text='Speed')
#         speed_label.grid(row=row, column=5, pady=10)
#         speed_slider = ctk.CTkSlider(root, from_=0.5, to_=2.0)
#         speed_slider.grid(row=row, column=6, pady=10)

#     def play_music(self):
#         # Implement playing logic here
#         pass

#     def stop_music(self):
#         # Implement stop logic here
#         s.stop()

# app = MusicApp()

# Create and run the application
# root.mainloop()