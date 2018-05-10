import gizeh
from moviepy.editor import VideoClip

WIDTH = 512
HEIGHT = 512
DURATION = 2
SW = 2.5 

def make_frame(t):
    global DURATION, WIDTH, HEIGHT, SW
    diagspeed = 256/DURATION

    surface = gizeh.Surface(width=WIDTH, height=HEIGHT)
    polygon = gizeh.square(l=max(100,300 -(200/DURATION)*t), 
            fill = (0,1,0), stroke_width = SW,
            xy = [256,256]) 
    polygon.draw(surface)

    l = 100

    ns1 = gizeh.square(l=100, 
            fill = (0,1,0), stroke_width = SW,
            xy = [-l+diagspeed*t,-l+diagspeed*t]) 
    ns1.draw(surface)

    ns2 = gizeh.square(l=100, 
            fill = (0,1,0), stroke_width = SW,
            xy = [512+l-diagspeed*t,-l+diagspeed*t]) 
    ns2.draw(surface)

    ns3 = gizeh.square(l=100, 
            fill = (0,1,0), stroke_width = SW,
            xy = [-l+diagspeed*t,512+l-diagspeed*t]) 
    ns3.draw(surface)

    ns4 = gizeh.square(l=100, 
            fill = (0,1,0), stroke_width = SW,
            xy = [512+l-diagspeed*t,512+l-diagspeed*t]) 
    ns4.draw(surface)

    ns5 = gizeh.square(l=100, 
            fill = (0,1,0), stroke_width = SW,
            xy = [256,512+l-diagspeed*t]) 
    ns5.draw(surface)

    ns6 = gizeh.square(l=100, 
            fill = (0,1,0), stroke_width = SW,
            xy = [256,-l+diagspeed*t]) 
    ns6.draw(surface)

    ns7 = gizeh.square(l=100, 
            fill = (0,1,0), stroke_width = SW,
            xy = [512+l-diagspeed*t,256]) 
    ns7.draw(surface)

    ns8 = gizeh.square(l=100, 
            fill = (0,1,0), stroke_width = SW,
            xy = [-l+diagspeed*t,256]) 
    ns8.draw(surface)

    print(t)
    return surface.get_npimage()

clip = VideoClip(make_frame, duration = DURATION)
clip.write_videofile("my_animation.mp4",fps=60)
clip.write_gif("my_animation.gif",fps=24,program='ffmpeg')

