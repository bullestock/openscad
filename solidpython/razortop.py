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

SEGMENTS = 64#128

eps = 0.001
rr = 2

# Brush
bhd = 34

# Razor
rhd = 12

bridge_l = 15

def sph(dia, radius, angle):
    rads = angle/360*2*math.pi
    return trans((dia/2+radius)*math.cos(rads), (dia/2+radius)*math.sin(rads), 0, sphere(r = radius))

def sfork(dia, th, angle):
    s1 = sph(dia, th/2, angle)
    s2 = sph(dia, th/2, 0)
    return rot(0, 0, (360-angle)/2, s1 + s2 + rotate_extrude(angle=angle)(translate([dia/2+th/2, 0])(circle(d=th))))

def vsfork(dia, th, angle):
    s1 = sphere(r = th/2)
    return up(dia)(trans(-dia, 0, 0, s1) + rot(90, 0, 180, rotate_extrude(angle=-angle)(translate([dia/2+th/2, 0])(circle(d=th)))))

def fork(dia, th, angle):
    return rot(0, 0, (360-angle)/2, rotate_extrude(angle=angle)(translate([dia/2+th/2, 0])(circle(d=th))))

def stand():
    bridge_w = 10
    fork_th = 5
    bfork = trans(bhd/2 + fork_th/2 + bridge_l/2, 0, 0, sfork(bhd, fork_th, 240))
    rfork_arc = trans(-(rhd/2 + fork_th/4 + bridge_l/2 - 0.5), 0, 0, rot(0, 0, 180, fork(rhd, fork_th, 180)))
    r_l = 12
    rcyl = rot(90, 0, 90, cylinder(d = fork_th, h = r_l))
    rc_x = (bridge_l/2 + rhd + fork_th + 1)
    rc_y = (rhd + fork_th)/2
    rcyls = trans(-rc_x, rc_y, 0, rcyl) + trans(-rc_x, -rc_y, 0, rcyl)
    hooks = trans(-rc_x, rc_y, 0, vsfork(5, fork_th, 90)) + trans(-rc_x, -rc_y, 0, vsfork(5, fork_th, 90))
    rfork = rfork_arc + rcyls + hooks
    c = trans(-bridge_l/2, 0, 0, rot(90, 0, 90, cylinder(d = fork_th, h = bridge_l)))
    bridge = hull()(trans(0, -bridge_w/2, 0, c) + trans(0, bridge_w/2, 0, c))
    hole = down(fork_th)(cylinder(d=5, h=3*fork_th))
    return bfork + rfork + bridge - hole

def brush():
    return color(c = 'white')(down(10)(cylinder(d = 30, h = 10) + up(10-eps)(cylinder(d1 = 30, d2 = 38, h = 20))))

def razor():
    return color(c = 'silver')(down(5)(cylinder(d = 9, h = 10) + down(15-eps)(cylinder(d1 = 14, d2 = 9, h = 20))))

def assembly():
    return stand() #+ trans(bhd/2 + bridge_l/2, 0, 0, brush()) + trans(-(rhd/2 + bridge_l/2), 0, 0, razor())

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python razortop.py"
# End:
