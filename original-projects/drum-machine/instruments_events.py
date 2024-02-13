"""
03-instruments.py - Using custom instrument with events.

The default instrument ( DefaultInstrument ) is a basic stereo RC oscillator
passing through reverberation unit. For the events framework to be really
useful, it has to give the user the opportunity to use their own instruments.
Composing an instrument is very simple.

An Events's instrument must be derived from the EventInstrument class. Its
signature must be::

    class InstrumentName(EventInstrument):
        def __init__(self, **args):
            EventInstrument.__init__(self, **args)

The EventInstrument is responsible for the creation of the envelope, accessible
through the variable self.env, and also for clearing its resources when it's done
playing. 

All arguments given to the Events object can be retrieved in our instrument with 
the syntax self.argument_name (ex.: self.freq).

"""
from pyo import EventInstrument, SmoothDelay, Sig, Selector, Freeverb, Phasor, Expseg, ButLP, SfPlayer, Server, Events, EventSeq, EventChoice
from effects import EffectsUnit

s = Server().boot()

class Instrument(EventInstrument):
    def __init__(self, **args):
        # print("Instrument Constructor")
        super().__init__(**args)
        self.osc = SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav", mul=self.env)
        # print("self.env: " + self.env)

class HiHat(EventInstrument):
    def __init__(self, **args):
        EventInstrument.__init__(self, **args)
        self.osc = SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav", mul=self.env, speed=self.sample_speed)
        self.effects = EffectsUnit(self.osc)
        
class Snare(Instrument):
    def __init__(self, **args):
        super().__init__(**args)
        self.sample_speed = 1.0
        self.osc = SfPlayer("./samples/snare/rhh_snare_one_shot_mid_short_old.wav", mul=self.env, speed=self.sample_speed)
        self.effects = EffectsUnit(self.osc)

class Kick(Instrument):
    def __init__(self, **args):
        super().__init__(**args)
        self.sample_speed = 1.0
        self.osc = SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav", mul=self.env, speed=self.sample_speed)
        self.effects = EffectsUnit(self.osc)   

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

hihat = Events(
    instr=HiHat,
    beat=0.333,
    amp=EventSeq([1, 0, 1, 0, 1]),
    bpm=BPM
).play()

snare = Events(
    instr=Snare,
    beat=1,
    amp=EventSeq([0, 1]), # amp = amplitude = volume
    bpm=BPM
).play()

kick = Events(
    instr=Kick,
    beat=1,
    amp=EventSeq([1, 0]),
    bpm=BPM
).play()

s.gui(locals())
