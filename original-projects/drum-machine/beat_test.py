from pyo import *

s = Server().boot()
s.start()
t = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
beat = Beat(time=.125, taps=16, w1=[90,80], w2=50, w3=35, poly=1).play()
trmid = TrigXnoiseMidi(beat, dist=12, mrange=(60, 96))
trhz = Snap(trmid, choice=[0,2,3,5,7,8,10], scale=1)
tr2 = TrigEnv(beat, table=t, dur=beat['dur'], mul=beat['amp'])
a = Sine(freq=trhz, mul=tr2*0.3).out()