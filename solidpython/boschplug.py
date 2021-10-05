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

SEGMENTS = 128

e = 0.001

def assembly():
    # Hole for one contact
    hole = cylinder(d = 4.7, h = 8)
    dd = 7 # Hole c/c
    # A round tuit to hold the contacts
    tuit = cylinder(d = 25, h = 6)
    tuit_holes =  trans(-dd, 0, -1, hole) + trans(dd, 0, -1, hole)
    # A stick to build the base
    ss = 6  # Stick thickness
    bw = 40 # Base width
    stick = ccube(bw, ss, ss)
    # Upright part
    hh = 23.2 # Hole height above plane
    upright = hull()(trans(0, hh, 0, tuit) + trans(0, 0, 0, stick))
    # Horizontal part
    hl = 20
    rstick = rot(90, 0, 0, trans(0, 0, -ss/2, roundxycube(bw, ss, ss, 2)))
    sd = 4.5
    screwhole = rot(90, 0, 180,
                    cylinder(d1 = sd, d2 = sd + 1.5*ss, h = ss + 2*e) +
                    trans(0, 0, -ss, cylinder(d = sd, h = 2*ss + 2*e)))
    scd = 25
    horiz = (hull()(stick + up(hl)(rstick)) - 
             trans(-scd/2, 0, ss + hl/2, screwhole) -
             trans(scd/2, 0, ss + hl/2, screwhole))
    return horiz + upright - trans(0, hh, 0, tuit_holes)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python boschplug.py"
# End:
