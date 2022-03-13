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

SEGMENTS = 16#64

eps = 0.01
width = 12
sw_h = 3
sw_w = 6
gap = 0.9
lever_h = 2.5
extra_h = gap + lever_h
plate_th = 1.3
holes_dist = 6.35
hole_inset = 2
rod_dia = 1.4

def block():
    return cube([width, sw_h + extra_h + lever_h/2, plate_th])

def cyl():
    return 

def part(flip):
    c = cylinder(d = rod_dia, h = plate_th + 2)
    horiz_gap = 1
    return block() + \
        trans(width - sw_w + horiz_gap if flip else 0,
              0,
              plate_th - eps,
              cube([width - sw_w - horiz_gap, sw_h, sw_w])) + \
        trans(0 if flip else width - sw_w,
              0,
              plate_th - eps,
              cube([sw_w, 1, sw_w])) - \
        trans(width - hole_inset if flip else hole_inset,
              sw_h + extra_h, -1, c)

def lever():
    return cube([width, lever_h, sw_w]) - \
        trans(hole_inset, lever_h/2, -1, cylinder(d = rod_dia, h = sw_w + 2))
    
def assembly():
    return part(False) + trans(width+1, 0, 0, part(True)) + \
        trans(0, sw_h + extra_h + lever_h, 0, lever())

if __name__ == '__main__':
    a = assembly()
    p1 = part(False)
    p2 = part(True)
    p3 = lever()
    scad_render_to_file(a, 'frontdoorswitch.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)
    scad_render_to_file(p1, 'part1.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)
    scad_render_to_file(p2, 'part2.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)
    scad_render_to_file(p3, 'part3.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python frontdoorswitch.py"
# End:
