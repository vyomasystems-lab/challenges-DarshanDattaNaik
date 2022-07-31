                                                             //vedic8x8
module vedic8x8(a,b,p);
input [7:0] a,b;
output [15:0] p;
wire [7:0] m,n,o,q,s0;
wire [11:0] s1,s2;
wire carry1,carry2,carry3;
vedic4x4 A(a[3:0],b[3:0],m);
vedic4x4 B(a[7:4],b[3:0],n);
vedic4x4 C(a[3:0],b[7:4],o);
vedic4x4 D(a[7:4],b[7:4],q);
assign p[3:0]=m[3:0];
rip_adder_8bit M(n,{4'b0,m[7:4]},1'b0,s0,carry1);
rip_adder_12bit N({q,4'b0},{4'b0,o},1'b0,s1,carry2);
rip_adder_12bit L(s1,{4'b0,s0},1'b0,p[15:4],carry3);
endmodule
                                                         //12bit riplle adder
module rip_adder_12bit(a,b,c,s,co);
input [11:0] a,b;
input c;
output [11:0] s;
output co;
wire [10:0] w;
full_adder A(a[0],b[0],c,s[0],w[0]);
full_adder B(a[1],b[1],w[0],s[1],w[1]);
full_adder C(a[2],b[2],w[1],s[2],w[2]);
full_adder D(a[3],b[3],w[2],s[3],w[3]);
full_adder E(a[4],b[4],w[3],s[4],w[4]);
full_adder F(a[5],b[5],w[4],s[5],w[5]);
full_adder G(a[6],b[6],w[5],s[6],w[6]);
full_adder H(a[7],b[7],w[6],s[7],w[7]);
full_adder I(a[8],b[8],w[7],s[8],w[8]);
full_adder J(a[9],b[9],w[8],s[9],w[9]);
full_adder K(a[10],b[10],w[9],s[10],w[10]);
full_adder L(a[11],b[11],w[10],s[11],co);
endmodule  

                                                         //8bit riplle adder
module rip_adder_8bit(a,b,c,s,co);
input [7:0] a,b;
input c;
output [7:0] s;
output co;
wire [6:0] w;
full_adder A(a[0],b[0],c,s[0],w[0]);
full_adder B(a[1],b[1],w[0],s[1],w[1]);
full_adder C(a[2],b[2],w[1],s[2],w[2]);
full_adder D(a[3],b[3],w[2],s[3],w[3]);
full_adder E(a[4],b[4],w[3],s[4],w[4]);
full_adder F(a[5],b[5],w[4],s[5],w[5]);
full_adder G(a[6],b[6],w[5],s[6],w[6]);
full_adder H(a[7],b[7],w[6],s[7],co);
endmodule 

                                                            //vedic4x4
module vedic4x4(a,b,p);
input [3:0] a,b;
output [7:0] p;
wire [3:0] m,n,o,q,s0;
wire [5:0] s1,s2;
wire carry1,carry2,carry3;
vedic2x2 A(a[1:0],b[1:0],m);
vedic2x2 B(a[3:2],b[1:0],n);
vedic2x2 C(a[1:0],b[3:2],o);
vedic2x2 D(a[3:2],b[3:2],q);
assign p[1:0]=m[1:0];
rip_adder_4bit M(n,{2'b0,m[3:2]},1'b0,s0,carry1);
rip_adder_6bit N({q,2'b0},{2'b0,o},1'b0,s1,carry2);
rip_adder_6bit L(s1,{2'b0,s0},1'b0,p[7:2],carry3);
endmodule


                                                         //6-bit riplle adder
module rip_adder_6bit(a,b,c,s,co);
input [5:0] a,b;
input c;
output [5:0] s;
output co;
wire [4:0] w;
full_adder A(a[0],b[0],c,s[0],w[0]);
full_adder B(a[1],b[1],w[0],s[1],w[1]);
full_adder C(a[2],b[2],w[1],s[2],w[2]);
full_adder D(a[3],b[3],w[2],s[3],w[3]);
full_adder E(a[4],b[4],w[3],s[4],w[4]);
full_adder F(a[5],b[5],w[4],s[5],co);
endmodule 

                                                           //4-bit riplle adder

module rip_adder_4bit(a,b,c,s,co);
input [3:0] a,b;
input c;
output [3:0] s;
output co;
wire [2:0] w;
full_adder A(a[0],b[0],c,s[0],w[0]);
full_adder B(a[1],b[1],w[0],s[1],w[1]);
full_adder C(a[2],b[2],w[1],s[2],w[2]);
full_adder D(a[3],b[3],w[2],s[3],co);
endmodule 

                                                                //Vedic2x2
module vedic2x2(a,b,p);
input [1:0] a,b;
output [3:0] p;
wire [3:0] w;
assign p[0]=a[0]&b[0]; 
assign w[0]=a[1]&b[0];
assign w[1]=a[0]&b[1];
assign w[2]=a[1]&b[1];
half_adder A(w[0],w[1],p[1],w[3]);
half_adder B(w[2],w[3],p[2],p[3]);
endmodule

                                                                //full adder module
module full_adder(a,b,c,s,co);
input a,b,c;
output s,co;
wire [2:0] w;
half_adder A(a,b,w[0],w[1]);
half_adder B(w[0],c,s,w[2]);
or D(co,w[2],w[1]);
endmodule

                                                                //Half adder module
module half_adder(a,b,s,c);
input a,b;
output s,c;
xor A(s,a,b);
and B(c,a,b);
endmodule