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
    return trans(x, y, z,
                 rot(90 + a, 0, 0, ccube(36, 34.3, 4 + extra) +
                     trans(0, 15.5, 4, ccube(10, 2.5, 10)) +
                     trans(0, 2, -4 if negative else -1, ccube(32, 18, 4 + extra))))

def front(x, y, z, a):
    s = sphere(r = cr)
    xo = width/2 - cr/2
    yo = disp_height/2 - cr/2
    s1 = trans(xo, yo, 0, s)
    s2 = trans(-xo, yo, 0, s)
    s3 = trans(xo, -yo, 0, s)
    s4 = trans(-xo, -yo, 0, s)
    return trans(x, y, z,
                 rot(90 + a, 0, 0,
                     hull()(s1 + s2 + s3 + s4) -
                     trans(0, 2, -2, ccube(32, 18, 2*cr+2))))
    
def assembly():
    w = wemos(0, 0)
    disp_y = 12
    disp_z = 10
    o = oled(0, disp_y, disp_z, tilt, True)
    f = front(0, disp_y - 1, disp_z, tilt)
    # Visualization
    a = w + f + o
    # With cutout for OLED
    a = w + f - o
    # Test of OLED fit
    a = f - o
    return a

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python lasersaurdisplay.py"
# End:
