# from pyo import Metro, Counter, Score, TrigFunc
import pyo
import wx

s = pyo.Server().boot()
s.start()

num_beats = 4
subdivision = 4
tempo = pyo.Sig(0.25) # in milliseconds

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

# Create a signal to represent the count that we can pass to other places 
hihat_counter = pyo.Sig(pyo.Counter(hihat_click, min=1, max=num_beats * subdivision + 1))
snare_counter = pyo.Sig(pyo.Counter(snare_click, min=1, max=num_beats * subdivision + 1))
kick_counter = pyo.Sig(pyo.Counter(kick_click, min=1, max=num_beats * subdivision + 1))

def seconds_to_bpm(time):
    bpm = time * 60
    return bpm

# def create_tuplets(click, subdivision):
#     click.setTime(tempo * 4/subdivision)
#     print("creating tuplets")
    
# create_tuplets(hihat_click, 5)

# hihat_click.setTime(tempo * 4/5)

def set_hihat_tuplet(e):
    # e.GetEventObject().GetValue()
    hihat_click.setTime(1.0 / e.GetEventObject().GetValue())
    
# et_hihat_tuplet(7)

# TODO: wrap this in Events or something similar to use a list to populate match statements
def play_hihat():
    count = int(hihat_counter.get())
    hihat_sample.mul = pyo.RandInt(100) / 100
    
    rhythm = [1, 1, 0, 1,
              1, 0, 0, 1,
              0, 1, 1, 1, 
              0, 1, 0, 1]
    
    if rhythm[count - 1] == 1:
        hihat_sample.out()

def play_snare():
    count = snare_counter.get()
    snare_sample.mul = 0.75 + pyo.RandInt(100) / 100 * 0.25
    
    match count:
        case (1):
            # print(f"count {int(count)}")
            pass
        case (2):
            pass
            # print(f"count {int(count)}")
        case (3):
            pass
            # print(f"count {int(count)}")
        case (4):
            pass
            # print(f"count {int(count)}")
        case (5):
            snare_sample.out()
            pass
            # print(f"count {int(count)}")
        case (6):
            pass
            # print(f"count {int(count)}")
        case (7):
            pass
            # print(f"count {int(count)}")
        case (8):
            pass
            # print(f"count {int(count)}")
        case (9):
            pass
            # print(f"count {int(count)}")
        case (10):
            pass
            # print(f"count {int(count)}")
        case (11):
            pass
            # print(f"count {int(count)}")
        case (12):
            pass
            # print(f"count {int(count)}")
        case (13):
            snare_sample.out()
            pass
            # print(f"count {int(count)}")
        case (14):
            pass
            # print(f"count {int(count)}")
        case (15):
            pass
            # print(f"count {int(count)}")
        case (16):
            pass
            # print(f"count {int(count)}")
            
def play_kick():
    count = kick_counter.get()
    snare_sample.mul = 0.75 + pyo.RandInt(100) / 100 * 0.25
    
    match count:
        case (1):
            # print(f"count {int(count)}")
            kick_sample.out()
        case (2):
            pass
            # print(f"count {int(count)}")
        case (3):
            pass
            # print(f"count {int(count)}")
        case (4):
            pass
            # print(f"count {int(count)}")
        case (5):
            pass
            # print(f"count {int(count)}")
        case (6):
            pass
            # print(f"count {int(count)}")
        case (7):
            pass
            # print(f"count {int(count)}")
        case (8):
            pass
            # print(f"count {int(count)}")
        case (9):
            kick_sample.out()
            pass
            # print(f"count {int(count)}")
        case (10):
            pass
            # print(f"count {int(count)}")
        case (11):
            pass
            # print(f"count {int(count)}")
        case (12):
            pass
            # print(f"count {int(count)}")
        case (13):
            pass
            # print(f"count {int(count)}")
        case (14):
            pass
            # print(f"count {int(count)}")
        case (15):
            pass
            # print(f"count {int(count)}")
        case (16):
            pass
            # print(f"count {int(count)}")
    
hihat = pyo.TrigFunc(hihat_click, play_hihat)
snare = pyo.TrigFunc(snare_click, play_snare)
kick = pyo.TrigFunc(kick_click, play_kick)

app = wx.App(False)

control_window = wx.Frame(None, wx.ID_ANY, "Soundscape 1")
control_window.Show(True)

hihat_tuplet_slider = wx.Slider(control_window, pos=wx.Point(0, 30), minValue=2, maxValue=10)
hihat_tuplet_slider.Bind(wx.EVT_SLIDER, set_hihat_tuplet)
hihat_tuplet_slider_label = wx.StaticText(control_window, label="hihat tuplet", pos=(10, 10))

app.MainLoop()

s.gui(locals)