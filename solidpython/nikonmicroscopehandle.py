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

rod_dia = 7
rod_length = 50
handle_dia = 20
handle_h = rod_dia

def rod():
    return rotate([0, 90, 0])(cylinder(d = rod_dia, h = rod_length))

def hole():
    return rotate([0, 90, 0])(cylinder(d = 3.5, h = 10))

def handle():
    return down(handle_h/2)(cylinder(d = handle_dia, h = handle_h))

def handle_indents():
    s_d = 70
    s = sphere(d = s_d)
    dip = 1.5
    return up(handle_h/2 + s_d/2 - dip)(s) + down(handle_h/2 + s_d/2 - dip)(s)

def assembly():
    r = rod()
    h = handle()
    hi = handle_indents()
    return r + h - hi - translate([rod_length - 9.9, 0, 0])(hole())

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)

