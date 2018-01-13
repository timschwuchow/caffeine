import win32api
import time
import random 
import math

def jitter():
    x,y = win32api.GetCursorPos()
    dx,dy = tuple([2*math.ceil(random.uniform(-1,1))-1 for x in range(2)])
    win32api.SetCursorPos((x+dx,y+dy))

while True:
    jitter()
    time.sleep(60)
