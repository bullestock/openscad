module rounded_box(x=10,y=20,z=10,r=0.25,wall=2,
		   has_lid=false, has_ridge=false, lid_thick=2,lid_ledge_width=2,lid_ledge_depth=2)
{
	/*
		Purpose:  Create a hollow enclosure with rounded corners and an optional lid
		Inputs:
			x,y,z = box inside dimensions (see note 1 below)
			r = radius of sphere used for rounding the corners. 
			wall = wall thickness
			has_lid = true to generate internal ledge and companion lid, false otherwise
			lid_thick = lid thickness
			lid_ledge_width = width of internal lid ledge
			lid_ledge_depth = depth of internal lid ledge
		Usage: 'rounded_box();' to generate a box with default parameters and a lid
		Note 1:
			The generated box will have outside x & y dimensions larger than the 
			specified parameters by twice the radius parameter selected.  The total
			height will be the specified z parameter plus the specified radius
		Note 2:
			Successful prints require a reasonably high quality 3D printer, capable
			of 0.2mm or better layer heights. 0.3mm 'draft' setting on my Prusa MK3S
			printer wouldn't resolve the inner lid ledge on a 30x20x10mm box with a
			1mm wide ledge.
	*/	
	
	
	difference()
	{
		minkowski()
		{
			cube([x,y,z],center = true);
			sphere(r);
		}
	  
		//cut off the top (need to do this to have flat lid mating surface)
		color("red")
		translate([0,0,z]) cube([x+3+r,y+3+r,z],center = true);

		//Hollow out the box
		color("green")
		minkowski()
		{
			translate([0,0,wall]) cube([x-wall,y-wall,z],center = true);
			sphere(r);
		}

		//optionally, create a ledge for a lid
		if(has_lid || has_ridge)
		{
		  //generate the ledge
		  translate([0,0,(z/2)-lid_ledge_depth])
		  {
				linear_extrude(10)
				{
					 minkowski()
					 {
						  square([x-wall+lid_ledge_width,y-wall+lid_ledge_width], 
						 center = true);
						  circle(r);
					 }
				}
		  }			  
		}//if(has_lid == true)
	}//difference
	 
	//optionally generate a lid
	if(has_lid)
	{
		//bottom plate
		translate([0,1.1*y+r,-z/2-r])//align lid bottom and box bottom 
		{
			color("red") 
			linear_extrude(lid_thick-lid_ledge_depth)
			{
				minkowski()
				{
				  square([x,y], center = true);
				  circle(r);
				}
			}
			
			//upper plate
			translate([0,0,lid_ledge_depth])//relative inside prev block 
			{
				color("violet") 
				linear_extrude(lid_ledge_depth)
				{
					minkowski()
					{
					  square([x-lid_ledge_width,y-lid_ledge_width], center = true);
					  circle(r);
					}
				}
			}//inner translate
		}//outer translate
	} //end 'if(has_lid == true)'
}//rounded_box()


module set_cutout(x,y,z,w,l,h) {
    translate(v = [x, y, z]) cube([w+0.4, l+0.2, h+0.2], center = true);
}

module set_cyl_cutout(x, y, z, d) {
    translate(v = [x, y + 5, z]) rotate([90]) cylinder(d = d, h = 10);
}

box_w = 75;
box_l = 125;
box_l_extra = 50;
box_h = 22;
pcb_z = 5;

