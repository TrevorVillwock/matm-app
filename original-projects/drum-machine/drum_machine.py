# from pyo import Metro, Counter, Score, TrigFunc
import pyo

s = pyo.Server().boot()
s.start()

num_beats = 4
subdivision = 4
tempo = 0.25 # in milliseconds

# samples
kick_sample = pyo.SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav")
snare_sample = pyo.SfPlayer("./samples/snare/rhh_snare_one_shot_mid_short_old.wav")
hihat_sample = pyo.SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav")

hihat_click = pyo.Metro(tempo / 3).play()
hihat_click.ctrl()
snare_click = pyo.Metro(tempo).play()
snare_click.ctrl()
kick_click = pyo.Metro(tempo).play()
kick_click.ctrl()

# Create a signal to represent the count that we can pass to other places 
hihat_counter = pyo.Sig(pyo.Counter(hihat_click, min=1, max=num_beats * subdivision + 1))
snare_counter = pyo.Sig(pyo.Counter(snare_click, min=1, max=num_beats * subdivision + 1))
kick_counter = pyo.Sig(pyo.Counter(kick_click, min=1, max=num_beats * subdivision + 1))

# TODO: wrap this in Events or something similar to use a list to populate match statements
def play_hihat():
    count = hihat_counter.get()
    hihat_sample.mul = pyo.RandInt(100) / 100
    
    match count:
        case (1):
            # print(f"count {int(count)}")
            hihat_sample.out()
        case (2):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (3):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (4):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (5):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (6):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (7):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (8):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (9):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (10):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (11):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (12):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (13):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (14):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (15):
            hihat_sample.out()
            # print(f"count {int(count)}")
        case (16):
            hihat_sample.out()
            # print(f"count {int(count)}")

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

s.gui(locals)