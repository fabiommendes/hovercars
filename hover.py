from FGAme import *

hover = world.add.rectangle(shape=(120, 50), pos=pos.middle, damping=0.1)

@listen('long-press', 'up')
def accel():
	hover.vel += 3 * hover.orientation()

run()
