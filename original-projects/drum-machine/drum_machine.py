# from pyo import Metro, Counter, Score, TrigFunc
import pyo

"""_summary_
metronome
counter for beats
counter for subdivisions - 2, 3, 4, 5, 6, 7, 8, 9
"""
s = pyo.Server().boot()
s.start()

num_beats = 4
subdivision = 4

# samples
kick_sample = pyo.SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav")
snare_sample = pyo.SfPlayer("./samples/snare/rhh_snare_one_shot_mid_short_old.wav")
hihat_sample = pyo.SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav")
# kick_sample.ctrl()
# kick_sample.play()
# kick_sample.stop()

click = pyo.Metro(0.25).play()
click.ctrl()

# Create a signal to represent the count that we can pass to other places 
subdivision_counter = pyo.Sig(pyo.Counter(click, min=1, max=num_beats * subdivision + 1))

def play_samples():
    count = subdivision_counter.get()
    hihat_sample.mul = pyo.RandInt(100) / 100
    match count:
        case (1):
            print(f"count {int(count)}")
            hihat_sample.out()
            kick_sample.out()
        case (2):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (3):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (4):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (5):
            hihat_sample.out()
            snare_sample.out()
            print(f"count {int(count)}")
        case (6):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (7):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (8):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (9):
            hihat_sample.out()
            kick_sample.out()
            print(f"count {int(count)}")
        case (10):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (11):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (12):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (13):
            hihat_sample.out()
            snare_sample.out()
            print(f"count {int(count)}")
        case (14):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (15):
            hihat_sample.out()
            print(f"count {int(count)}")
        case (16):
            hihat_sample.out()
            print(f"count {int(count)}")
    
beats = pyo.TrigFunc(click, play_samples)

s.gui(locals)