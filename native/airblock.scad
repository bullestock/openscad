F = 50; // Circle accuracy
Ws = 0.8; // Wall thickness
Hg = 10;// High over all
Rib = 0.1; // High of the Rib
Rf = 2; // Rib proportion
Dr = 6; // Dia Hose Outside

module part(Da, Ws, taper = 0.5)
{
    union()
    {
        //
        cylinder(h=Hg, d1=Da, d2 = Da-taper, $fn=F);
        // Disc
        translate([0,0,-Ws/2]) cylinder(h=Ws,d=Dr,$fn=F);
        // Top cone
        translate([0,0,0.5*Ws]) cylinder(h=Ws,d1=Dr,d2=Da,$fn=F);
        //
        //
        for(i=[Rf*Ws:Rf*Ws:Hg-Ws])
        {
            translate([0,0,i])
            rotate_extrude (angle = 360, $fn=F) 
            {
                translate([Da/2 - Ws+Rib + .1 - i/60, 0])
                circle(Ws,$fn=6); 
            }// ende rotate_extrude
        }// ende for
    } // ende union
}

module part_hole(Da, Ws)
{
    union()
    {
        translate([0, 0, -0.5*Hg]) cylinder(h=2*Hg,d=Da-2*Ws,$fn=F);
        translate([0, 0, -0.5*Hg]) cylinder(h=4,d=Dr - 2*Ws,$fn=F);
    }
}

Da = 5;
Da1 = 3.5;
Dd = 10;

difference()
{
    union()
    {
        part(Da1, Ws, 0.3);
        translate([Dd, 0, 0]) part(Da, Ws);
        translate([2*Dd, 0, 0]) part(Da, Ws);
        translate([-Dd/2, -Dd/2, -Dd]) cube([3*Dd, Dd, Dd]);
    }
    union()
    {
        part_hole(Da1, Ws*.8);
        translate([Dd, 0, 0]) part_hole(Da, Ws);
        translate([2*Dd, 0, 0]) part_hole(Da, Ws);
        translate([-0.25*Dd, 0, -Dd/2]) rotate([90, 0, 90]) cylinder(d = 0.8*Dd, h = 2.5*Dd, $fn=F);
    }
}
