# Music and the Macrocosmos App

This will eventually turn into a desktop app that will hold Python versions of all the current Tone.js instrument projects (Square Sounds, Conway's Game of Sound, Synth Sandbox, and HexGrid) as well as allow users to create their own instruments with Python.

We'll be using the `pyo` package for audio; documentation here: http://ajaxsoundstudio.com/pyodoc/

We'll also be using tkinter and customtkinter for the user interface (UI): 

http://tkdocs.com/
https://pypi.org/project/customtkinter/0.3/

To get started with this project, we need to create an "environment," or a setup on our computer where the program can access all the other code it needs in the form of various libraries. The Python command we use for this is called `venv`, which stands for virtual environment. To create a new `venv` Python environment called `matm-app-env`run `venv ./matm-app-env` in your terminal. Then install the necessary Python packages from the `requirements.txt` file using the command `pip3 install -r requirements.txt`.

For an explanation of scripts, modules, packages, and libraries, read here: https://realpython.com/lessons/scripts-modules-packages-and-libraries/#:~:text=04%3A41%20Packages%20are%20a,Python%20scripts%20without%20any%20issues.

The `pyo-examples` folder in this folder contains working examples with `pyo` from the package's github that can be used to expand the project: https://github.com/belangeo/pyo

## Recording

The pyo server has built-in recording ability. By default, the recording is stored in your home directory. To change this to the directory of your Python file or another folder on your computer, use `Server.recordOptions(filename = "./your_file_name.wav")`.