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

e = 0.01

# Small tube dia
std = 10
# Wall thickness
wt = 0.5
# Height of lower straight part
h1 = 50
# Height of upper wedge-shaped part
h2 = 30
# Height of tube above
th = 50
# Depth of straight part
d = 10
# Width
w = 30

def bagkanal():
    bottom = ccube(w, d, h1) - up(wt+e)(ccube(w-2*wt, d-2*wt, h1-wt)) - trans(0, 1, 5, ccube(w - 10, 10, 20))
    # Upper depth of upper part
    d2 = 15
    displacement = (d2-d)/2
    top_outer = hull()(ccube(w, d, e) + trans(0, displacement, h2, ccube(w, d2, e)))
    top_inner = hull()(ccube(w-2*wt, d-2*wt, e) + trans(0, displacement, h2-wt, ccube(w-2*wt, d2-2*wt, e)))
    top = top_outer - top_inner - trans(0, displacement, h2 - 2*wt, cylinder(d = std-wt, h = 5))
    tube = cylinder(d = std, h = th) - cylinder(d = std-wt, h = th+e)
    return bottom + up(h1)(top) + trans(0, displacement, h1+h2, tube)

def assembly():
    bk = bagkanal()
    bkd = 100
    hor_w = bkd + std
    return left(bkd/2)(bk) + right(bkd/2)(bk)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python ludsugning.py"
# End:
