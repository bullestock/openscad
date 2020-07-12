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

def block(w, l, h, inset):
    c = right(w/2)(ccube(w, l, h))
    corner_side_len = w
    corner_size = corner_side_len*0.707
    corner = rot(0, 0, 45, ccube(corner_side_len, corner_side_len, h+2))
    xc = l + corner_size/2 - inset
    yc = w/2 + corner_size/2
    c1 = trans(xc, yc, -1, corner)
    c2 = trans(xc, -yc, -1, corner)
    return c - (c1 + c2)
    
def assembly():
    inner = trans(-e, 0, -5, block(80, 80-.5, 20, 20)) # sub .5 for tight fit
    shell = 15
    offset = 18
    outer = trans(0, -offset/2, 0, block(80 + shell, 80 + offset + 2*shell, 20 + 5, 35))
    cutout = left(e)(block(75, 70, 30, 17))
    cutout2 = trans(68, -20, 0, cylinder(h = 30, d = 15))
    sh = 20+10
    sw = 5
    c1 = trans(5, -(45+sw/2+offset), 0, cylinder(d = sw, h = sh))
    c2 = trans(5, (45+sw/2), 0, cylinder(d = sw, h = sh))
    c3 = trans(60+sw/2, -(45+sw/2+offset), 0, cylinder(d = sw, h = sh))
    c4 = trans(60+sw/2, (45+sw/2), 0, cylinder(d = sw, h = sh))
    c5 = trans(85+sw/2, -(20+sw/2+offset), 0, cylinder(d = sw, h = sh))
    c6 = trans(85+sw/2, (20+sw/2), 0, cylinder(d = sw, h = sh))
    slits = hull()(c1 + c3) + hull()(c2 + c4) + hull()(c5 + c6) + hull()(c3 + c5) + hull()(c4 + c6) + hull()(c1 + c2)
    exhaust = trans(50, -51, -1, cylinder(h = 30, d = 20))
    return outer - inner - cutout - down(sh-15)(slits) - cutout2 - exhaust

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python bungardshoe.py"
# End:
