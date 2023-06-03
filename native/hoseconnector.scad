pcInnDia=3.5;
pcInnDiaEnd=5;
pcOutSmallDia=pcInnDia+2;
pcOutBigDia=pcOutSmallDia+0.8;
pcOutEndDia=8;
pcTipH=5;
pcNotchH=6;
pcNotchCnt=1;
pcEndH=pcNotchH;


pcFn=30;
pcH=pcTipH+pcNotchH*pcNotchCnt+pcEndH;

module PipeConnector() difference(){
	union(){
		translate([0,0,pcNotchH*pcNotchCnt+pcEndH])
		cylinder(d2=pcInnDia,d1=pcOutBigDia,h=pcTipH,$fn=pcFn);
		for(i=[0:(pcNotchCnt-1)])
		translate([0,0,pcNotchH*i+pcEndH])
		cylinder(d2=pcOutSmallDia,d1=pcOutBigDia,h=pcNotchH,$fn=pcFn);
		cylinder(d2=pcOutSmallDia,d1=pcOutEndDia,h=pcEndH,$fn=pcFn);
	}
	cylinder(d=pcInnDia,h=pcH,$fn=pcFn);
	cylinder(d2=pcInnDia,d1=pcInnDiaEnd,h=pcEndH,$fn=pcFn);
}

PipeConnector();
rotate([180,0,0])
PipeConnector();