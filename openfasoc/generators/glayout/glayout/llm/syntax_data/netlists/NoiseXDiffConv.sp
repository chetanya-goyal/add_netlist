let width_m1 = 2.5
let width_m2 = 2.5
let length_m1 = 2.5
let length_m2  = 2.5
let m1_multiplier = 2
let m2_multiplier = 2
let m1_fingers = 2
let m2_fingers = 2

.subckt NoiseXDiffConv
X0 out1 bias in gnd sky130_fd_pr__nfet_01v8 l={length_m1} w={width_m1} m={m1_fingers * m1_multiplier}
X1 out2 in gnd gnd sky130_fd_pr__nfet_01v8 l={length_m2} w={width_m2} m={m2_fingers * m2_multiplier}
.ends