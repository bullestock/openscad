from solid import *
from solid.utils import *

# Cube, rounded in x/y, at (0, 0)
def roundxycube(length, width, height, radius):
    rh = radius
    ch = 0.1
    return translate([rh, rh, 0])(minkowski()(cube([length - 2*radius, width - 2*radius, height - ch]),
                                               cylinder(r = radius, h = ch)))
# Cube, rounded in x/y/z, at (0, 0)
def roundcube(length, width, height, radius):
    rh = radius
    ch = 0.1
    return translate([rh, rh, rh])(minkowski()(cube([length - 2*radius, width - 2*radius, height - ch]),
                                               sphere(r = radius)))
# Cube, rounded in x/y/z, centered in x/y
def roundccube(length, width, height, radius):
    return translate([-length/2, -width/2, 0])(roundcube(length, width, height, radius))

# Cube centered around origin
def ccube(w, l, h):
    return translate([-w/2, -l/2, 0])(cube([w, l, h]))

# Shortcut for translate()
def trans(x, y, z, s):
    return translate([x, y, z])(s)

# Shortcut for rotate()
def rot(x, y, z, s):
    return rotate([x, y, z])(s)

def tslotfoot(length, height):
    width = 20
    inset = 8
    body = roundxycube(length, width, height, 2)
    screwhole = hole()(translate([0, width/2, 0])(down(1)(cylinder(d = 4, h = height + 2))))
    return body + right(inset)(screwhole) + right(length - inset)(screwhole)
