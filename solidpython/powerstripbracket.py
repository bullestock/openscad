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
    bd = 2
    ball = sphere(d = bd)
    cut_w = 56
    cut_h = 7
    bh = 15
    w = 15
    bw = cut_w + 2*w
    # Screw hole radius
    rs = 2
    # Screw head radius
    rsh = 4
    cutout = down(e)(ccube(cut_w, w + 2, cut_h))
    outer = minkowski()(ccube(bw, w, bh - bd), ball)
    negative = trans(-(bw+2)/2, -(w+2)/2, -bd, cube([bw + 2, w + 2, bd]))
    screwhole = down(1)(cylinder(r = rs, h = bh + 2)) + translate([0, 0, bh - rsh])(cylinder(r1 = rs, r2 = rsh, h = rsh))
    mid = (bw + cut_w)/4
    h1 = trans(-mid, 0, 0, screwhole)
    h2 = trans(mid, 0, 0, screwhole)
    return outer - cutout - negative - h1 - h2

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python powerstripbracket.py"
# End:
