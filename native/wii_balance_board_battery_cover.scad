$fn=60;
main();
translate([2,40,1]) clipsu();


module clipsu() {
rotate([90,0,0]){
	difference () {
		union(){
			hull () {
				translate([0,0,0]) cylinder(r=1,h=15);
				translate([5,0,0]) cylinder(r=1,h=14.5);
				translate([3.6,10.4,1]) cylinder(r=2,h=12.7);
				}
				translate([-2,-1,0]) cube([2,1,15]);

			}
		union(){
			hull() { 
				translate([3.6,10.4,-1]) cylinder(r=1,h=16);
				translate([3.5,-2,-1]) cylinder(r=1,h=16);
				translate([2.9,-2,-1]) cylinder(r=1,h=16);
				}
			translate([-3,0,-0.5]) cube([3,5,16]);
			translate([-2,-2,-0.5]) cube([5,7,2.6]);
			translate([-2,-2,12.6]) cube([5,7,2.6]);
			}
		}
	}
}

module main() {
difference(){
union(){
//cube([6.2,24,2]);
//translate([0,42,0]) cube([6.2,24,2]);
translate([4,4,0])
minkowski(){
cube([69.5,58,1]);
cylinder(r=4,h=1,$fn=60);
}
translate([8.1,0,0]) cube([54.8,1.6,4.5]);
translate([8.1,64.4,0]) cube([54.8,1.6,4.5]);
translate([73.8,8.8,0]) cube([5.8,8.8,5.3]);
translate([73.8,48.2,0]) cube([5.8,8.8,5.3]);
}
union(){
translate([0,24,0]) cube([6.2,17.8,2]);
translate([77.5,8.3,0]) cube([3,10,3.9]);
translate([77.5,47.7,0]) cube([3,10,3.9]);
}
}
}