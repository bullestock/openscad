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

SEGMENTS = 64

eps = 0.01
width = 12
sw_h = 3
sw_w = 6.5
button_h = 1.35
lever_h = 2.5
sw_plate_th = 0.5
extra_h = sw_plate_th + button_h + lever_h
plate_th = 1.25
holes_dist = 6.35
hole_inset = 2
rod_dia = 1.4

def block():
    return cube([width, sw_h + extra_h, plate_th])

def cyl():
    return 

def part1():
    c = cylinder(d = rod_dia, h = plate_th + 2)
    horiz_gap = 2
    return block() + \
        trans(0,
              0,
              plate_th - eps,
              cube([width - sw_w - horiz_gap, sw_plate_th + sw_h, sw_w])) + \
        trans(width - sw_w,
              0,
              plate_th - eps,
              cube([sw_w, sw_plate_th, sw_w])) - \
        trans(hole_inset,
              sw_plate_th + sw_h + button_h + lever_h/2, -1, c) - \
        trans(2 * hole_inset,
              sw_h + extra_h - lever_h + eps,
              -eps, cube([width - 2 * hole_inset + eps, lever_h, 5]))

def part2():
    c = cylinder(d = rod_dia, h = plate_th + 2)
    return block() - \
        trans(width - hole_inset,
              sw_plate_th + sw_h + button_h + lever_h/2, -1, c) - \
        trans(-eps,
              sw_h + extra_h - lever_h + eps,
              -eps, cube([width - 2 * hole_inset + eps, lever_h, 5]))

def lever():
    stopper = cube([hole_inset, button_h, sw_w])
    clearance = 0.25
    return cube([hole_inset*2 + clearance, lever_h, sw_w]) + \
        trans(2 * hole_inset + clearance, 0, -plate_th, cube([width - 2 * hole_inset, lever_h, sw_w + 2 * plate_th])) - \
        trans(hole_inset, lever_h/2, -1, cylinder(d = rod_dia, h = sw_w + 2)) + \
        trans(0, lever_h - eps, 0, stopper)
    
def assembly():
    return part1() + trans(width+1, 0, 0, part2()) + \
        trans(0, sw_h + extra_h + lever_h + sw_w, 0, rot(90, 0, 0, lever()))

if __name__ == '__main__':
    a = assembly()
    p1 = part1()
    p2 = part2()
    p3 = lever()
    scad_render_to_file(a, 'frontdoorswitch.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)
    scad_render_to_file(p1, 'part1.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)
    scad_render_to_file(p2, 'part2.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)
    scad_render_to_file(p3, 'part3.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python frontdoorswitch.py"
# End:
