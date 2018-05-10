import gizeh
from moviepy.editor import VideoClip
import random

class Rabbit:
    def __init__(self, 
            width = 512,
            height = 512,
            ground = 400,
            jumpchance = 0.05,
            jumpweight = 20,
            rabbitsize = 10):
        self.width = width
        self.height = height
        self.ground = ground
        self.jumpchance = jumpchance
        self.jumpweight = jumpweight
        self.inair = 0
        self.velocity = (0,0)
        self.acceleration = (0,10)
        self.positions = []
        self.curr = (width//2, ground)
        self.rabbitsize = rabbitsize

    def get_positions(self, number_of_positions):
        for x in range(number_of_positions):
            if self.inair:
                self.velocity = tuple(map(sum,
                    zip(self.velocity,self.acceleration)))
            else:
                self.velocity = (0,0)
                if random.random() < self.jumpchance:
                    vx = round((random.random()-0.5)*self.jumpweight)*2
                    vy = -round(random.random()*self.jumpweight)
                    self.velocity = (vx, vy)
                    self.inair = 1
            self.curr = tuple(map(sum, zip(self.curr,self.velocity)))
            if self.curr[1] > self.ground - self.rabbitsize//2:
                self.curr = (self.curr[0],self.ground-self.rabbitsize//2)
                self.inair = 0
            if self.curr[0] > self.width - self.rabbitsize//2:
                self.curr = (self.width - self.rabbitsize//2,self.curr[1])
                self.velocity = (-self.velocity[0], self.velocity[1])
            if self.curr[0] < self.rabbitsize//2:
                self.curr = (self.rabbitsize//2, self.curr[1])
                self.velocity = (-self.velocity[0], self.velocity[1])
            self.positions.append(self.curr)
        return self.positions


DURATION = 10
FPS = 32
FRAMES = DURATION*FPS
POSITIONS = []
HEIGHT = 512
WIDTH = 512
INDEX = 0
RABBITSIZE = 10

for i in range(5):
    r = Rabbit()
    r.ground = 400 + int((random.random()-0.5)*40)
    r.curr = (int(512*random.random()),r.ground)
    POSITIONS.append(r.get_positions(FRAMES))
    print(POSITIONS[i][19])

print(len(POSITIONS)) 

def make_frame(t):
    global DURATION, WIDTH, HEIGHT, POSITIONS, INDEX, RABBITSIZE
    surface = gizeh.Surface(width=WIDTH, height=HEIGHT)
    for pos in POSITIONS:
        rabbit = gizeh.square(l=RABBITSIZE,fill=(1,1,1),
                xy=pos[min(len(pos)-1,INDEX)])
        rabbit.draw(surface)
    INDEX += 1
    return surface.get_npimage()

clip = VideoClip(make_frame, duration = DURATION)
clip.write_videofile("my_animation.mp4",fps=FPS)
clip.write_gif("my_animation.gif",fps=FPS,program='ffmpeg')

