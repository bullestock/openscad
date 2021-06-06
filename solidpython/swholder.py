#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhere in sys.path
from solid import *
from solid.utils import *
from utils import *

SEGMENTS = 64

e = 0.001

w = 6
l = 18

sw_l = 12.6
sw_h = 6.5

pins_l = sw_l
pins_w = 3
pins_h = 6

wire_d = 1.5
wire_h = 3

def assembly():
    sw = ccube(sw_l, w, sw_h)
    pins = ccube(pins_l, pins_w, pins_h)
    wire = cylinder(d = wire_d, h = wire_h)
    wires = hull()(trans(-wire_d/2, 0, 0, wire)+trans(wire_d/2, 0, 0, wire))
    inner = sw + up(sw_h - e)(pins) + up(sw_h + pins_h - e)(wires)
    outer = roundccube(l, w-e, sw_h + pins_w + wire_h, 1)
    return outer - inner

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python swholder.py"
# End:
