#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re
import math

# Assumes SolidPython is in site-packages or elsewhere in sys.path
from solid import *
from solid.utils import *
from utils import *

SEGMENTS = 128

e = 0.01

tube_od = 160
tube_id = 156
tube_height = 20
plate_w = 190
plate_h = 3.5
dh = 155/2

def mhole(x, y):
    return trans(x*dh, y*dh, 1, cylinder(d = 15.5, h = 4))

def assembly():
    tube = cylinder(d = tube_od, h = tube_height) - hole()(down(1)(cylinder(d = tube_id, h = tube_height+2)))
    plate = ccube(plate_w, plate_w, plate_h)
    mholes = mhole(1, 1) + mhole(-1, 1) + mhole(1, -1) + mhole(-1, -1)
    return tube + plate - mholes

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python ventplate.py"
# End:
