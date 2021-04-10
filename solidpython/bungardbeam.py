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

SEGMENTS = 32

e = 0.001

def assembly():
    bw = 12
    bl = 127
    bh = 20
    hi = 8
    beam = cube([bl, bw, bh])
    ch = 20
    cutout = trans(15, -1, -ch + 10, cube([81, bw+2, ch]))
    mh1 = trans(hi, bw/2, -1, cylinder(d = 6, h = 8))
    mh2 = trans(bl - hi, bw/2, -1, cylinder(d = 6, h = 8))
    sh = bh - 1
    sw = 5
    si = 5 + sw/2
    brush_z = 11
    c1 = trans(si, bw/2, brush_z, cylinder(d = sw, h = sh+1))
    c2 = trans(bl - si, bw/2, brush_z, cylinder(d = sw, h = sh+1))
    return beam - cutout - mh1 - mh2 - hull()(c1 + c2)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python bungardbeam.py"
# End:
