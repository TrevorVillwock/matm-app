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
from pyo import EventInstrument, SmoothDelay, Sig, Selector, Freeverb, Phasor, Expseg, ButLP, SfPlayer, Server, Events, EventSeq

s = Server().boot()

# class Instrument(EventInstrument):
#     def __init__(self, **args):
#         EventInstrument.__init__(self, **args)
#         self.delay = SmoothDelay(self.osc, delay=0.333, feedback=0.7)
#         self.delay_is_on = Sig(1)
#         self.delay_selector = Selector([self.osc, self.delay], self.delay_is_on) 
#         self.reverb_is_on = Sig(1)
#         self.reverb = Freeverb(self.delay_selector)
#         self.reverb_selector = Selector([self.delay_selector, self.reverb], self.reverb_is_on)

class HiHat(EventInstrument):
    def __init__(self, **args):
        # Instrument.__init__(self, **args)
        EventInstrument.__init__(self, **args)

        # self.freq is derived from the 'degree' argument.
        
        self.phase = Phasor([self.freq, self.freq * 1.003])

        # self.dur is derived from the 'beat' argument.
        
        self.duty = Expseg([(0, 0.05), (self.dur, 0.5)], exp=4).play()

        self.osc = SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav")

        # EventInstrument created the amplitude envelope as self.env.
        self.filt = ButLP(self.osc, freq=5000, mul=self.env).out()
        
class Snare(EventInstrument):
    def __init__(self, **args):
        # Instrument.__init__(self, **args)
        EventInstrument.__init__(self, **args)

        # self.freq is derived from the 'degree' argument.
        
        self.phase = Phasor([self.freq, self.freq * 1.003])

        # self.dur is derived from the 'beat' argument.
        
        self.duty = Expseg([(0, 0.05), (self.dur, 0.5)], exp=4).play()

        self.osc = SfPlayer("./samples/snare/rhh_snare_one_shot_mid_short_old.wav")

        # EventInstrument created the amplitude envelope as self.env.
        self.filt = ButLP(self.osc, freq=5000, mul=self.env).out()

class Kick(EventInstrument):
    def __init__(self, **args):
        EventInstrument.__init__(self, **args)

        # self.freq is derived from the 'degree' argument.
        
        self.phase = Phasor([self.freq, self.freq * 1.003])

        # self.dur is derived from the 'beat' argument.
        
        self.duty = Expseg([(0, 0.05), (self.dur, 0.5)], exp=4).play()

        self.osc = SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav")

        # EventInstrument created the amplitude envelope as self.env.
        self.filt = ButLP(self.osc, freq=5000, mul=self.env).out()       

    
# We tell the Events object which instrument to use with the 'instr' argument.
hihat = Events(
    instr=HiHat,
    beat=1 / 5,
    db=-12,
    attack=0.001,
    decay=0.05,
    sustain=0.5,
    release=0.005,
).play()

snare = Events(
    instr=Snare,
    beat=1,
    amp=EventSeq([0., 1., 0., 1.]),
    attack=0.001,
    decay=0.05,
    sustain=0.5,
    release=0.005,
).play()

kick = Events(
    instr=Kick,
    beat=1,
    amp=EventSeq([0., 1., 0., 1.]),
    db=-12,
    attack=0.001,
    decay=0.05,
    sustain=0.5,
    release=0.005,
).play()

s.gui(locals())
