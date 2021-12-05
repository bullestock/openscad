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

SEGMENTS = 32#64#128

eps = 0.001
rr = 2

# Brush
bhd = 30

# Razor
rhd = 10

def sph(dia, radius, angle):
    rads = angle/360*2*math.pi
    return trans((dia+2*radius)*math.cos(rads), (dia+2*radius)*math.sin(rads), 0, sphere(r = radius))

def fork(dia, th, angle):
    s1 = sph(dia, th/2, angle)
    s2 = sph(dia, th/2, 0)
    return rot(0, 0, (360-angle)/2, s1 + s2 + rotate_extrude(angle=angle)(translate([dia+th, 0])(circle(d=th))))

def assembly():
    bridge_l = 15
    bridge_w = 10
    fork_th = 5
    bfork = trans(bhd + fork_th + bridge_l/2, 0, 0, fork(bhd, fork_th, 250))
    rfork = trans(-(rhd + fork_th + bridge_l/2), 0, 0, rot(0, 0, 180, fork(rhd, fork_th, 250)))
    c = trans(-bridge_l/2, 0, 0, rot(90, 0, 90, cylinder(d = fork_th, h = bridge_l)))
    bridge = hull()(trans(0, -bridge_w/2, 0, c) + trans(0, bridge_w/2, 0, c))
    hole = down(fork_th)(cylinder(d=5, h=3*fork_th))
    return bfork + rfork + bridge - hole

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python razortop.py"
# End:
