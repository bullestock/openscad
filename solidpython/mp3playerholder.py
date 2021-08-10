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

hdx = 14.5*2.54
hdy = 7.5*2.54
wx = 42
wy = 24
hd = 2.5
pcb_th = 1.6
base_th = 3

def stud():
    h1 = 3
    h2 = 1.2*pcb_th
    sd = 1.2*hd
    return (cylinder(d = 5, h = h1) +
            up(h1)(cylinder(d = hd, h = h2)) +
            hull()(up(h1+h2)(cylinder(d = hd, h = e)) +
                   up(h1+h2+sd*0.4)(sphere(d = sd))))

def assembly():
    base = roundxycube(wx, wy, base_th, 2.5)
    studs = (trans(hdx/2, hdy/2, 0, stud()) +
             trans(-hdx/2, hdy/2, 0, stud()) +
             trans(hdx/2, -hdy/2, 0, stud()) +
             trans(-hdx/2, -hdy/2, 0, stud()))
    sd = 4
    screwhole = cylinder(d1 = sd, d2 = sd + 2*base_th, h = base_th + 2*e)
    return base + trans(0, 0, base_th, studs) - down(e)(screwhole)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python mp3playerholder.py"
# End:
