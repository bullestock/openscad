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

d1 = 7
d2 = 8.6
d3 = 5
h1 = 6.7
h2 = 1.2

def flange():
    s = sphere(d = h2)
    d = down(0)(cylinder(d = d2 - h2, h = h2))
    return minkowski()(s, d) - down(0)(cylinder(d = d2 + 2, h = h2+1))

def body():
    rr = 1
    s = sphere(r = rr)
    c = cylinder(d = d1 - 2*rr, h = h1 - rr)
    return minkowski()(s, c) - down(2)(cylinder(d = d2 + 2, h = 2))

def slit():
    return translate([-5, 0, h1 - 0.3])(rotate([0, 90, 0])(cylinder(d = 0.8, h = 10)))

def separator():
    return translate([-0.9, -2.5, h1-2])(cube([1.8, 5, 1]))

def assembly():
    f = flange()
    b = body()
    return b + f - down(1)(cylinder(d = d3, h = h1 + h2 + 2)) - slit() + separator()

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)

