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

SEGMENTS = 128

e = 0.01

tube_od = 160
tube_id = 156
tube_height = 20
ring_od = 190
ring_h = 3

def hole(angle):
    return rot(0, 0, angle, trans((ring_od + tube_id)/4, 0, -1, cylinder(d = 10, h = 10)))

def assembly():
    tube = cylinder(d = tube_od, h = tube_height) - down(1)(cylinder(d = tube_id, h = tube_height+2))
    ring = cylinder(d = ring_od, h = ring_h) - down(1)(cylinder(d = tube_id, h = ring_h+2))
    holes = hole(0)
    for a in range(1, 18):
        holes = holes + hole(a*20)
    return tube + ring - holes

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python ventring.py"
# End:
