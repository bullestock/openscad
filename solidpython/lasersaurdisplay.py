#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re
import math

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *
from utils import *

esp = import_scad('ESP8266Models.scad')

SEGMENTS = 16#32

e = 0.001

# Corner radius
cr = 2

# Angle of display
tilt = 30
# Width
width = 50
disp_height = 48

def wemos(x, y, z):
    return trans(x, y, z, rot(90, 0, 0, esp.WemosD1M()))

def oled(x, y, z, a, negative = False):
    extra = 5 if negative else 0
    bezel_w = 30
    bezel_h = 17
    bezel_d = 0
    bezel_c1 = ccube(bezel_w, bezel_h, e)
    bezel_slant = 1 * (bezel_d + extra - e)
    bezel_c2 = ccube(bezel_w + bezel_slant, bezel_h + bezel_slant, e)
    bezel = hull()(bezel_c2 + trans(0, 0, bezel_d + extra - e, bezel_c1))
    return color(c = 'blue')(trans(x, y, z,
                                   rot(90 + a, 0, 0, ccube(38, 36, 4 + extra) +
                                       trans(0, 15.5, 4, ccube(10, 2.5, 10)) +
                                       trans(0, 2, -4 if negative else -1, bezel))))

def front_cuts(x, y, z, a, print = True):
    c = None
    if not print:
        c = trans(0, 2, -2, ccube(32, 18, 2*cr+2))
        c = trans(x, y, z,
                  rot(90 + a, 0, 0, c))                  
    return c

def front_s(x, y, z, a):
    #def roundcube_s(length, width, height, radius):
    #return translate([length/2, width/2, 0])(roundccube_s(length, width, height, radius))
    ss = roundccube_s(width, disp_height, 2*cr+1, cr)
    for i in range(0, 8):
        c = trans(0, 0, -cr, ss[i])
        f = trans(x, y, z,
                  rot(90 + a, 0, 0, c))
        ss[i] = f
    return ss

def top_s(x, y, z, depth):
    return trans(x, y + depth/2, z, roundccube_s(width, depth, 2*cr+1, cr))
    
def back_s(x, y, z, height):
    ss = roundccube_s(width, 2*cr+1, height, cr)
    for i in range(0, 8):
        ss[i] = trans(x, y, z, ss[i])
    return ss
    
def assembly():
    print = True  # Print
    #print = False # Visualize
    d1 = wemos(0, -10, -2)
    wemos_holder = up(4)(trans(0, -10, 9, roundccube(32, 6, 8, 1) - ccube(20.5, 8, 10)) - d1)
    disp_y = 12
    disp_z = 3
    o = oled(0, disp_y, disp_z, tilt, print)
    #f = front_s(
    f_s = front_s(0, disp_y + 1, disp_z, tilt)
    f = hull()(f_s)
    if not print:
        f = f - front_cuts(0, disp_y - 1, disp_z, tilt, print)
    top_depth = 25
    top_y = disp_y - top_depth - disp_height/2*math.sin(90 + tilt)
    top_z = disp_z + disp_height/2*math.cos(90+tilt)
    t_s = top_s(0, top_y + 1.5*cr, top_z - 1.5*cr, top_depth + 1.2*cr)
    t = hull()(t_s)
    back_h = disp_height*math.cos(90+tilt)
    b_s = back_s(0, top_y + 2.8*cr, top_z - back_h, back_h)
    b = hull()(b_s)
    side1 = hull()(f_s[0] + f_s[6] + b_s[0] + b_s[4])
    side2 = hull()(f_s[1] + f_s[7] + b_s[1] + b_s[5])
    a = wemos_holder
    # Visualization
    if not print:
        a = a + d1 + f + o
    else:
        a = a + f - o
    # With cutout for OLED
    #a = d1 + f - o
    a = a + t + b + side1 + side2
    cutoff = trans(-width, -width, -65, cube([2*width, 2*width, width]))
    cw = width - 4
    cd = disp_height - 2
    ch = 10
    cth = 3
    chimney = trans(0, 1, -25, roundxycube(cw, cd, ch, 2) - down(1)(roundxycube(cw - 2*cth, cd - 2*cth, ch+2, 2)))
    return a - cutoff + chimney

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python lasersaurdisplay.py"
# End:
