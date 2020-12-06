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

# Tube dia
td = 16
wt = 1
h1 = 50
h2 = 30
th = 50
d = 10

def bagkanal():
    w = 30
    bottom = ccube(w, d, h1) - up(wt+e)(ccube(w-2*wt, d-2*wt, h1-wt)) - trans(0, 1, 5, ccube(w - 10, 10, 20))
    d2 = 20
    top_outer = hull()(ccube(w, d, e) + trans(0, d/2, h2, ccube(w, d2, e)))
    top_inner = hull()(ccube(w-2*wt, d-2*wt, e) + trans(0, d/2, h2-wt, ccube(w-2*wt, d2-2*wt, e)))
    top = top_outer - top_inner - trans(0, d/2, h2 - 2*wt, cylinder(d = td-wt, h = 5))
    tube = cylinder(d = td, h = th) - cylinder(d = td-wt, h = th+e)
    return bottom + up(h1)(top) + trans(0, d/2, h1+h2, tube)

def tube_bend():
    offset = 20
    return trans(offset, 0, 0, rot(90, -90, 0, rotate_extrude(angle = 90)(trans(offset, 0, 0, circle(d = td) - circle(d = td-wt)))))

def assembly():
    bk = bagkanal()
    bkd = 100
    bend_size = 20
    hor_w = bkd - 2*bend_size
    return left(bkd/2)(bk) + right(bkd/2)(bk) + \
        trans(-bkd/2, d/2, h1+h2+th, tube_bend()) + \
        trans(bkd/2, d/2, h1+h2+th, rot(0, 0, 180, tube_bend())) + \
        trans(-hor_w/2, d/2, h1+h2+th+bend_size, rot(90, 0, 90, cylinder(d = td, h = hor_w))) + \
        trans(0, d/2, h1+h2+th+bend_size, cylinder(d = td, h = 50))

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python ludsugning.py"
# End:
