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

SEGMENTS = 32#256

e = 0.001
dia = 59
lid_w = 36
corner_r = 3
lid_th = 2

pod_iw = 28
pod_ow = 32
pod_h = 22
pod_x = 2

cutout_h = 7
cutout_w = 12
cutout_offset = -1 # Offset from center

# Wemos
wm_l = 34.5
wm_w = 25.5
wm_th = 2
wm_usb_offset = 1 # USB connector is not centered

filler_offset = 10

led_y = -5

def pod():
    pod_l = 15
    pod_extra_w = 5
    pod_h = 12
    wt = 2
    pod_outer = roundccube(pod_l, wm_w + pod_extra_w, pod_h, 1.5)
    usb_w = 12
    usb_h = 8
    usb_hole = ccube(pod_l + 5, usb_w, usb_h)
    pod = trans(-(wm_l + 2*wt + pod_l)/2, 0, -pod_h/2, down(1)(pod_outer) - trans(1, wm_usb_offset, (pod_h - usb_h)/2, hole()(usb_hole)))
    plughole = trans(dia/2, led_y, 10, ccube(5, 4.7, 6))
    plugtube = trans(dia/2 - 4, led_y, 10-1.5, ccube(5, 4.7+3, 6+3))
    es = .5
    frame_inner = ccube(wm_l+es, wm_w+es, wm_th+e)
    frame_outer = ccube(wm_l + 2*wt, wm_w + 2*wt, 2*wm_th)
    frame_cut = trans(-wm_l/2, wm_usb_offset, -wm_th, ccube(5, 12, wm_th+2))
    return pod + frame_outer - frame_inner - frame_cut #pod_outer - pod_inner + plugtube - plughole + 

def smps():
    w = 17
    l = 22
    h = 2
    wt = 1
    inner = ccube(w, l, h + e)
    outer = ccube(w + 2*wt, l + 2*wt, h)
    return trans(8, filler_offset - dia/2 - h, lid_w/2, rot(90, 0, 180, outer - hole()(inner)))

def shell():
    outer = cylinder(d = dia, h = lid_w)
    inner = down(1)(cylinder(d = dia - 2*lid_th, h = lid_w+2))
    cutter = trans(0, dia/2, -1, ccube(dia + 2, dia, lid_w + 2))
    rounder_cube = cube([lid_th + 2, corner_r, corner_r])
    rounder_cyl = trans(-1, 0, 0, rot(0, 90, 0, cylinder(r = corner_r, h = lid_th + 4)))
    rounder = rounder_cube - rounder_cyl
    adj = 0
    rounder1 = trans(-dia/2 - 1, -corner_r + adj + 0.5, lid_w - corner_r, rounder)
    rounder2 = trans(dia/2 - lid_th - 1, -corner_r + adj + 0.5, lid_w - corner_r, rounder)
    # Inner slit at edges
    slit1 = trans(dia/2 - 2, adj, -1, ccube(2, 2.5, lid_w + 2))
    slit2 = trans(-(dia/2 - 2), adj, -1, ccube(2, 2.5, lid_w + 2))
    filler_h = wm_w+4
    # Block for screw hole
    filler = up((lid_w - filler_h)/2)(cylinder(d = dia - 2*lid_th, h = filler_h) -
                                      trans(-dia/2, -dia/2 + filler_offset, -2, cube([dia, dia, lid_w+4])))
    screwhole = trans(0, -dia/2 + 4.8, -lid_w/2, cylinder(d = 4.5, h = 2*lid_w))
    led_x = dia/2 - 5
    ledhole = trans(dia/2 - 5, led_y, 30, rot(90, 0, 90, cylinder(d = 5, h = 10)))
    ledtube = trans(dia/2 - 4, led_y, 30, rot(90, 0, 90, cylinder(d = 7, h = 4)))
    return outer - inner - cutter - rounder1 - rounder2 - slit1 - slit2 + filler - screwhole + ledtube - ledhole

def assembly():
    return pod() #shell() + smps() #

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=False)


# Local Variables:
# compile-command: "python lid.py"
# End:
