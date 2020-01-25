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

d1 = 6.9
d2 = 8.6
d3 = 5.4
h1 = 6.7
h2 = 1.2

def flange():
    d = down(0)(cylinder(d = d2, h = h2))
    return cylinder(d = d2, h = h2)

def body():
    c = cylinder(d = d1, h = h1)
    return c

def slit():
    sd = 1
    return translate([-5, 0, h1 - 0.3])(rotate([0, 90, 0])(cylinder(d = sd, h = 10)))

def separator():
    w = 3
    h = 1.5
    l = 5.5
    return translate([-w/2, -l/2, h1-h])(cube([w, l, h]))

def assembly():
    f = flange()
    b = body()
    return b + f - down(1)(cylinder(d = d3, h = h1 + h2 + 2)) - slit() + separator()

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)

