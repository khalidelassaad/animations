import gizeh
from moviepy.editor import VideoClip
import random

WIDTH = 512
HEIGHT = 512
DURATION = 10
FPS = 32
FRAMES = DURATION*FPS
POSITIONS = []
CURR = (256,400)
GROUND = 400
INAIR = 0
RABBITSIZE = 10
VELOCITY = (0,0)
ACCELERATION = (0,10)
JUMPCHANCE = 0.05
JUMPWEIGHT = 20
INDEX = 0
for x in range(FRAMES):
    if INAIR:
        VELOCITY = tuple(map(sum, zip(VELOCITY,ACCELERATION)))
    else:
        VELOCITY = (0,0)
        if random.random() < JUMPCHANCE:
            vx = round((random.random()-0.5)*JUMPWEIGHT)*2
            vy = -round(random.random()*JUMPWEIGHT)
            VELOCITY = (vx, vy)
            INAIR = 1
    CURR = tuple(map(sum, zip(CURR,VELOCITY)))
    if CURR[1] > GROUND - RABBITSIZE//2:
        CURR = (CURR[0],GROUND-RABBITSIZE//2)
        INAIR = 0
    if CURR[0] > WIDTH - RABBITSIZE//2:
        CURR = (WIDTH - RABBITSIZE//2,CURR[1])
        VELOCITY = (-VELOCITY[0], VELOCITY[1])
    if CURR[0] < RABBITSIZE//2:
        CURR = (RABBITSIZE//2, CURR[1])
        VELOCITY = (-VELOCITY[0], VELOCITY[1])
    POSITIONS.append(CURR)

for pos in POSITIONS:
    print(pos)
print(len(POSITIONS))

def make_frame(t):
    global DURATION, WIDTH, HEIGHT, POSITIONS, FRAMES, INDEX
    surface = gizeh.Surface(width=WIDTH, height=HEIGHT)
    rabbit = gizeh.square(l=RABBITSIZE,fill=(1,1,1),
            xy=POSITIONS[min(len(POSITIONS)-1,INDEX)])
    rabbit.draw(surface)
    INDEX += 1
    return surface.get_npimage()

clip = VideoClip(make_frame, duration = DURATION)
#clip.write_videofile("my_animation.mp4",fps=FPS)
clip.write_gif("my_animation.gif",fps=FPS,program='ffmpeg')

