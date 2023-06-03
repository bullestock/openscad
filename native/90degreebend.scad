use <threadlib/threadlib.scad>

F = 90 ;// Circle accuracy
Ws = 2.0 ;// Wall thickness
Hg = 25 ;// High over all
Rib = 0.3 ;// High of the Rib
Rf = 1.6 ;// Rib proportion
Dr = 25;// Dia Hose Outside

module part(Da)
{
    //
    difference()
    {
        //
        union()
        {
            //
            cylinder(h=Hg, d1=Da, d2=Da-1, $fn=F);
            // Top cone
            translate([0,0,0]) cylinder(h=Ws,d1=Dr,d2=Da,$fn=F);
            //
            //
            for(i=[Rf*Ws:Rf*Ws:Hg-Ws])
            {
                translate([0,0,i])
                rotate_extrude (angle = 360, $fn=F) 
                {
                    translate([Da/2 - Ws+Rib - i/60, 0])
                    circle(Ws,$fn=6); 
                }// ende rotate_extrude
            }// ende for
        } // ende union
        //
        translate([0,0,-1])
        cylinder(h=Hg+2,d=Da-2*Ws,$fn=F);
    }// ende difference
}

// For lille
// Da1 = 12.5;// Dia Hose Inside
// Da2 = 9 ;// Dia Hose Inside
// Close
// Da1 = 13.5;
// Da2 = 10;
Da1 = 13.5;

offset = Dr/2;
cs = Dr;
difference()
{
    union()
    {
        part(Da1);
        translate([offset, 0, -offset]) rotate([0, 90, 0]) part(Da1);
        translate([-cs/2, -cs/2, -cs]) cube([cs, cs, cs]);
    }
    translate([offset, 0, 0]) rotate([90, 180, 0]) rotate_extrude(angle = 90) translate([offset, 0, 0]) circle(r = Da1/2-Ws);
}
