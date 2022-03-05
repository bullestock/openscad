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
sw_w = 12
sw_h = 5
sw_th = 5.6
gap = 0.9
lever_h = 2.5
extra_h = gap + lever_h
plate_th = 1.5 # 2.7
holes_dist = 6.35
hole_inset = 2

def block():
    return cube([sw_w, sw_h + extra_h + lever_h/2, plate_th])

def cyl():
    # actual diameter 1.85
    return cylinder(d = 1.8, h = sw_th/2 - 0.1)

def part(flip):
    c = cyl()
    dy = 1.6
    return block() + \
        trans(sw_w/2 - holes_dist/2, dy, plate_th - eps, c) + \
        trans(sw_w/2 + holes_dist/2, dy, plate_th - eps, c) + \
        trans(sw_w - hole_inset if flip else hole_inset,
              sw_h + extra_h, plate_th - eps, c)

def lever():
    return cube([sw_w, lever_h, sw_th]) - \
        trans(hole_inset, lever_h/2, -1, cylinder(d = 1.9, h = sw_th + 2))
    
def assembly():
    return part(False) + trans(sw_w+1, 0, 0, part(True)) + \
        trans(0, sw_h + extra_h + lever_h, 0, lever())

if __name__ == '__main__':
    #a = assembly()
    p1 = part(False)
    p2 = part(True)
    p3 = lever()
    scad_render_to_file(p1, 'part1.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)
    scad_render_to_file(p2, 'part2.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)
    scad_render_to_file(p3, 'part3.scad', file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python frontdoorswitch.py"
# End:
