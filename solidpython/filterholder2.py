#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Lasersaur filter holder, with holes

from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *
from utils import *

SEGMENTS = 64

eps = 0.001
iw = 215
ow = 235
rr = 2
th = 3
pd = 3

def peghole():
    return hole()(down(1)(cylinder(d = pd, h = 2*th)))

def cutout():
    return roundccube(20, 10, 3, 1)

def assembly():
    outer = roundxycube(ow, ow, th, rr)
    inner = roundxycube(iw, iw, th + 2, rr)
    mw = (ow + iw)/4
    for i in range(-2, 3):
        outer = outer + trans(mw, i/2*mw, 0, peghole())
        outer = outer + trans(-mw, i/2*mw, 0, peghole())
    for i in range(-1, 2):
        outer = outer + trans(i/2*mw, mw, 0, peghole())
        outer = outer + trans(i/2*mw, -mw, 0, peghole())
    cutouts = None
    cz = 2
    for i in range(-2, 2):
        c = trans((i/2 + 0.25)*mw, -ow/2, cz, cutout())
        if cutouts:
            cutouts = cutouts + c
        else:
            cutouts = c
    for i in range(-2, 2):
        c = trans((i/2 + 0.25)*mw, ow/2, cz, cutout())
        cutouts = cutouts + c
    for i in range(-2, 2):
        c = trans(ow/2, (i/2 + 0.25)*mw, cz, rot(0, 0, 90, cutout()))
        cutouts = cutouts + c
    for i in range(-2, 2):
        c = trans(-ow/2, (i/2 + 0.25)*mw, cz, rot(0, 0, 90, cutout()))
        cutouts = cutouts + c
    return outer - down(1)(inner) - cutouts

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python filterholder2.py"
# End:
