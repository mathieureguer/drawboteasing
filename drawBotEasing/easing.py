import math
import functools


'''
frame is the current time (or position) of the timeline.
origin is the start value of the property.
change is the change between the start and end value of the property.
duration is the total length of the timeline.
'''


# ----------------------------------------
# decorators
# ----------------------------------------

def delay(start=10, end=10):
    def decorator_delay(func):
        @functools.wraps(func)
        def wrapper_delay(frame, origin, change, duration):
            if frame <= start:
                delayed_frame = origin
                return origin
            elif frame > duration-end:
                delayed_frame = duration-end
            else:
                delayed_frame = frame-start
            return func(delayed_frame, origin, change, duration-end)
        return wrapper_delay
    return decorator_delay
    
def frequencer(frequency=2):
    def decorator_frequencer(func):
        @functools.wraps(func)
        def wrapper_frequencer(frame, origin, change, duration):
            frequenced_tween = abs(abs(frame/duration*frequency*2%4-2)/2*duration - duration)
            return func(frequenced_tween, origin, change, duration)
        return wrapper_frequencer
    return decorator_frequencer
    

# ----------------------------------------
# easing
# ----------------------------------------

def linearTween(frame, origin, change, duration):
    return change*frame/duration + origin
    
def easeInQuad(frame, origin, change, duration):
    frame /= duration
    return change*frame*frame + origin

def easeOutQuad(frame, origin, change, duration):
    frame /= duration
    return -change * frame*(frame-2) + origin

def easeInOutQuad(frame, origin, change, duration):
    frame /= duration/2
    if frame < 1:
       return change/2*frame*frame + origin
    frame-=1
    return -change/2 * (frame*(frame-2) - 1) + origin

def easeInOutCubic(frame, origin, change, duration):
    frame /= duration/2
    if frame < 1:
       return change/2*frame*frame*frame + origin
    frame -= 2
    return change/2*(frame*frame*frame + 2) + origin

def easeInQuart(frame, origin, change, duration):
    frame /= duration
    return change*frame*frame*frame*frame + origin

def easeOutQuart(frame, origin, change, duration):
    frame /= duration
    frame -= 1
    return -change * (frame*frame*frame*frame - 1) + origin

def easeInOutQuart(frame, origin, change, duration):
    frame /= duration/2
    if frame < 1:
       return change/2*frame*frame*frame*frame + origin
    frame -= 2
    return -change/2 * (frame*frame*frame*frame - 2) + origin

def easeInQuint(frame, origin, change, duration):
    frame /= duration
    return change*frame*frame*frame*frame*frame + origin

def easeOutQuint(frame, origin, change, duration):
    frame /= duration
    frame -= 1
    return change*(frame*frame*frame*frame*frame + 1) + origin

def easeInOutQuint(frame, origin, change, duration):
    frame /= duration/2
    if frame < 1:
       return change/2*frame*frame*frame*frame*frame + origin
    frame -= 2
    return change/2*(frame*frame*frame*frame*frame + 2) + origin

def easeInSine(frame, origin, change, duration):
    return -change * math.cos(frame/duration * (math.pi/2)) + change + origin

def easeOutSine(frame, origin, change, duration):
    return change * math.sin(frame/duration * (math.pi/2)) + origin


def easeInOutSine(frame, origin, change, duration):
    return -change/2 * (math.cos(math.pi*frame/duration) - 1) + origin

def easeInExpo(frame, origin, change, duration):
    return change * math.pow( 2, 10 * (frame/duration - 1) ) + origin

def easeOutExpo(frame, origin, change, duration):
    return change * ( -math.pow( 2, -10 * frame/duration ) + 1 ) + origin

def easeInOutExpo(frame, origin, change, duration):
    frame /= duration/2
    if frame < 1: 
       return change/2 * math.pow( 2, 10 * (frame - 1) ) + origin
    frame -= 1
    return change/2 * ( -math.pow( 2, -10 * frame) + 2 ) + origin

def easeInCirc(frame, origin, change, duration):
    # this one does not work so well
    # change cannot be higher than duration (?)
    frame /= duration
    return -change * (math.sqrt(1 - frame*frame) - 1) + origin

def easeOutCirc(frame, origin, change, duration):
    frame /= duration
    frame -= 1
    return change * math.sqrt(1 - frame*frame) + origin

def easeInOutCirc(frame, origin, change, duration):
    frame /= duration/2
    if frame < 1:
       return -change/2 * (math.sqrt(1 - frame*frame) - 1) + origin
    frame -= 2
    return change/2 * (math.sqrt(1 - frame*frame) + 1) + origin