#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *

SEGMENTS = 32

D = 26
th = 3
lw = 5
H = 16 + lw - th

def cc(w, l, h):
    return translate([-w/2, -l/2, 0])(cube([w, l, H]))

def top():
    outer = cylinder(d = D + 2*th, h = lw)
    iw = 10
    inner = down(1)(cylinder(d = D - th, h = lw))
    return outer - inner

def leg():
    return cc(lw, th, H)

def assembly():
    t = top()
    ld = D/2 + th/2 - 0.2
    a = t
    for i in range(0, 6):
        a = a + rotate([0, 0, i*60])(translate([0, -ld, th])(leg()))
    h = up(th)(cylinder(d = D, h = H))
    return a - h

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)

