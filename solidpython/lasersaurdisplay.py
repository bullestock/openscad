#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *
from utils import *

esp = import_scad('ESP8266Models.scad')

SEGMENTS = 32

e = 0.001

# Corner radius
cr = 2

# Angle of display
tilt = 30
# Width
width = 50
disp_height = 40

def wemos(x, y):
    # 'turns' must match h
    return trans(x, y, 0, rot(90, 0, 0, esp.WemosD1M()))

def oled(x, y, z, a, negative = False):
    extra = 5 if negative else 0
    return color(c = 'blue')(trans(x, y, z,
                                   rot(90 + a, 0, 0, ccube(36, 34.3, 4 + extra) +
                                       trans(0, 15.5, 4, ccube(10, 2.5, 10)) +
                                       trans(0, 2, -4 if negative else -1, ccube(32, 18, 4 + extra)))))

def front(x, y, z, a, print = True):
    c = trans(0, 0, -cr, roundccube(width, disp_height, cr/4, cr));
    if not print:
        c = c - trans(0, 2, -2, ccube(32, 18, 2*cr+2))
    f = trans(x, y, z,
              rot(90 + a, 0, 0, c))                  
    return f
                     
    
def assembly():
    print = True  # Print
    print = False # Visualize
    w = wemos(0, -10)
    disp_y = 12
    disp_z = 3
    o = oled(0, disp_y, disp_z, tilt, print)
    f = front(0, disp_y - 1, disp_z, tilt, print)
    # Visualization
    if not print:
        a = w + f + o
    else:
        a = f - o
    # With cutout for OLED
    #a = w + f - o
    # Test of OLED fit
    #a = f - o
    return a

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python lasersaurdisplay.py"
# End:
