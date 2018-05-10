import gizeh
from moviepy.editor import VideoClip

WIDTH = 512
HEIGHT = 512

SPEED = 0
ACCEL = 4
DISP = 0

def make_frame(t):
    global SPEED, ACCEL, DISP
    bouncefactor = 0.9
    r = 50
    startheight = 51
    SPEED += ACCEL
    DISP += SPEED
    if (startheight + DISP + r) > 512:
        DISP = 511 - (startheight + r)
        SPEED = -SPEED * bouncefactor
    surface = gizeh.Surface(width=WIDTH, height=HEIGHT)
    circle = gizeh.circle (r = r, 
            xy = [WIDTH//2,startheight + DISP], fill= (0,1,0))
    circle.draw(surface)
    print(t)
    return surface.get_npimage()

clip = VideoClip(make_frame, duration = 10)
#clip.write_videofile("my_animation.mp4",fps=60)
clip.write_gif("my_animation.gif",fps=24,program='ffmpeg')

