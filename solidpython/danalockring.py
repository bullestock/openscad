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

SEGMENTS = 32

e = 0.01

cover_id = 47
cover_od = 53
ring_id = 42
ring_od = 58
ring_h = 3
slot_r = 25

def slot(angle):
    return rot(0, 0, angle, trans(slot_r, 0, -2, ccube(3, 9, 10)))

def assembly():
    cover_groove = cylinder(d = cover_od, h = 2) - down(1)(cylinder(d = cover_id, h = 4))
    ring = cylinder(d = ring_od, h = ring_h) - down(1)(cylinder(d = ring_id, h = ring_h+2))
    slots = slot(0)
    for a in range(1, 6):
        slots = slots + slot(a*60)
    body = ring - down(e)(cover_groove)
    return body - slots

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python danalockring.py"
# End:
