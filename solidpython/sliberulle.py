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

def rulle():
    return rotate_extrude(angle=360)(translate([0, 0])(square(size=[18, 18])) - \
                                     translate([17, 9])(hull()(circle(d=8) + \
                                                               translate([2, 0])(circle(d=6)))))

def assembly():
    return rulle() - \
        down(0.1)(cylinder(d = 22.5, h = 10)) - \
        cylinder(d = 17, h = 20)

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)
