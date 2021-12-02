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

SEGMENTS = 64#128

eps = 0.001
iw = 215
ow = 235
rr = 2
th = 3
pd = 3

def peghole():
    return hole()(down(1)(cylinder(d = pd, h = 2*th)))

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
    return outer - down(1)(inner)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python filterholder2.py"
# End:
