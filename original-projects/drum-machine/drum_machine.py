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
kick_sample = pyo.SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav").out()
# kick_sample.ctrl()
#kick_sample.play()
kick_sample.stop()

def test():
    kick_sample.out()
    print("test")
    # print(kick_sample.isOutputting())

click = pyo.Metro(1).play()
#subdivision_counter = pyo.Counter(click, min=1, max=num_beats * subdivision)

beats = pyo.TrigFunc(click, test)
# control = pyo.Score(subdivision_counter, fname="event_")
s.gui(locals)


