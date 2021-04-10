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

SEGMENTS = 16

e = 0.001

fan_wh = 120
fanh_d = 5
fan_bottom = 13

shroud_w = 134.5
shroud_l = 147
overhang_h = 10.5
overhang_d = 12.6
overhang_cutout_w = 6.5
overhang_cutout_h = 3
hole_cc = 112
hole_bot = 4
th = 3

v_size = 8.5
v_dist = 10
v_n_x = 13
v_n_y = 12

def vents():
    v = down(1)(roundxycube(v_size, v_size, 10, 2))
    vents = None
    for x in range(0, v_n_x):
        for y in range(0, v_n_y):
            vent = trans(x*v_dist, y*v_dist, 0, v)
            if vents:
                vents = vents + vent
            else:
                vents = vent
    return vents

def assembly():
    fanhole = trans((shroud_w - fan_wh)/2, fan_bottom, -1, cube([fan_wh, fan_wh, fanh_d + 1]))
    cover = trans(0, 0, 0, cube([shroud_w, shroud_l, fanh_d + th]))
    overhang = trans(0, 0, -overhang_d, cube([shroud_w, overhang_h, overhang_d]))
    overhang_cutout = trans(-1, overhang_h - overhang_cutout_h, -(0*6.8 + overhang_cutout_w), cube([shroud_w+2, overhang_cutout_h, overhang_cutout_w]))
    vent_width = (v_n_x - 1) * v_dist + v_size
    vent_length = (v_n_y - 1) * v_dist + v_size
    vent_offset_x = (shroud_w - vent_width)/2
    vent_offset_y = (shroud_l - vent_length)/2
    cutter = trans(-10, 20, -20, cube([200, 200, 200]))
    hole = cylinder(d = 3, h = 20)
    holes = trans(-hole_cc/2, 0, 0, hole) + trans(hole_cc/2, 0, 0, hole)
    holes = trans(shroud_w/2, shroud_l - hole_bot, 0, holes)
    return cover + overhang - overhang_cutout - fanhole - trans(vent_offset_x, vent_offset_y, 0, vents()) - holes

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python sfcover.py"
# End:
