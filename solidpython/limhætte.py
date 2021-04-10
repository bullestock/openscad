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

e = 0.001

def segment(w, d, h):
    dist = (w-d)/2
    c1 = left(dist)(cylinder(d = d, h = h))
    c2 = right(dist)(cylinder(d = d, h = h))
    return hull()(c1+c2)

def assembly():
    h1 = 10
    s1 = up(0)(segment(13.8, 6.2, h1))
    h2 = 5
    s2 = up(h1)(segment(10, 5, h2))
    h3 = 5
    s3 = up(h1+h2)(segment(7, 5, h2))
    inner = s1 + s2 + s3
    outer = segment(h1+h2+h3, 12, 20+5)
    tab = translate([10, 0, h1+h2+h3])(segment(20, 12, 5)) - right(14)(cylinder(d = 4, h = 100))
    #
    return outer - down(e)(inner) + tab

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)

