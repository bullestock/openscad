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
gap = 0.9
lever_h = 2.5
extra_h = gap + lever_h
plate_th = 2.7
holes_dist = 6.35
hole_inset = 2

def block():
    return cube([sw_w, sw_h + extra_h, plate_th])

def cyl():
    return cylinder(d = 1.8, h = 6)

def assembly():
    c = cyl()
    dy = 1.6
    return block() + \
        trans(sw_w/2 - holes_dist/2, dy, plate_th - eps, c) + \
        trans(sw_w/2 + holes_dist/2, dy, plate_th - eps, c) + \
        trans(sw_w - hole_inset, sw_h + gap + lever_h/2, plate_th - eps, c)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python frontdoorswitch.py"
# End:
