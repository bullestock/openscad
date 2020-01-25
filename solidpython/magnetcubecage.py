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

w = 20
th = 3
lw = 5

def cc(w, l, h):
    return translate([-w/2, -l/2, 0])(cube([w, l, h]))

def top():
    outer = cc(w + 2*th, w + 2*th, lw)
    iw = w - 2*(lw-th)
    inner = down(1)(cc(iw, iw, lw+2))
    return outer - inner

def leg():
    return cc(lw, lw, w)

def assembly():
    t = top()
    ld = w/2 + 0.5
    l1 = translate([-ld, -ld, th])(leg())
    l2 = translate([ld, ld, th])(leg())
    h = up(th)(cc(w, w, w+1))
    return t + l1 + l2 - h

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)

