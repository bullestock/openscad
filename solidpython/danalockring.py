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

groove_id = 45
groove_od = 53
groove_depth = 2
ring_id = 42
ring_od = 59
ring_h = 7
slot_r = 24
disc_id = 10
disc_od = ring_id + 1
disc_th = 2

def slot(angle):
    d1 = 4
    d2 = 2.5
    return rot(0, 0, angle,
               trans(slot_r, 0, -2,
                     ccube(d1, 9, 10) + trans(d2-e, 0, 5, ccube(d2, 9, 5))))

def assembly():
    groove = cylinder(d = groove_od, h = groove_depth) - down(1)(cylinder(d = groove_id, h = groove_depth+2))
    ring = cylinder(d = ring_od, h = ring_h) - down(1)(cylinder(d = ring_id, h = ring_h+2))
    disc = up(ring_h - disc_th)(cylinder(d = disc_od, h = disc_th) - down(1)(cylinder(d = disc_id, h = disc_th+2)))
    slots = slot(0)
    for a in range(1, 6):
        slots = slots + slot(a*60)
    body = ring - down(e)(groove)
    return body + disc - slots

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python danalockring.py"
# End:
