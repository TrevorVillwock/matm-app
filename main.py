# This module creates the starting window for the application
#
# Built following tutorial at https://www.youtube.com/watch?v=1itG8q-sCGY
# Creating a virtual environment: https://docs.python.org/3/tutorial/venv.html
# 
# customtkinter documentation: https://customtkinter.tomschimansky.com/documentation/
import customtkinter as ctk

# widgets are nested inside eachother in a hierarchy
# widgets are labels, buttons, etc.
root = ctk.CTk()
root.geometry("800x400")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.title("Music and the Macrocosmos")
root.attributes("-fullscreen", True)

# first argument is parent widget
title_label = ctk.CTkLabel(root, text="Welcome! Select A Project:", font=ctk.CTkFont(size=30, weight="bold"))
# position label
title_label.pack(padx=10, pady=(40, 20))

# Layout options: pack, grid, place

# https://tkdocs.com/tutorial/canvas.html

main_menu_frame = ctk.CTkFrame(root, fg_color="black")
main_menu_frame.grid(column=0, row=0, sticky="nsew")

# TODO: make icons for each of these
square_sounds_button = ctk.CTkButton(root, text="Square Sounds", width=500, font=("Arial", 18))
synth_sandbox_button = ctk.CTkButton(root, text="Synth Sandbox", width=500, font=("Arial", 18))
conway_button = ctk.CTkButton(root, text="Conway's Game of Sound", width=500, font=("Arial", 18))

square_sounds_button.pack(pady=10)
synth_sandbox_button.pack(pady=10)
conway_button.pack(pady=10)

# square_sounds_canvas = ctk.CTkCanvas(main_canvas, width=400, height=200, background="blue")
# square_sounds_canvas.pack()

# runs infinite event loop, anything below this line won't run
root.mainloop()