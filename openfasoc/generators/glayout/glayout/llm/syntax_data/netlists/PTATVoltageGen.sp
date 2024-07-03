let bias_width = 2.5
let mirror_width = 2.5
let bias_length = 2.5
let mirror_length = 2.5
let bias_multiplier = 2
let mirror_multiplier = 2
let bias_fingers = 2
let mirror_fingers = 2

.subckt PTATVoltageGen
X0 out vdd gnd gnd sky130_fd_pr__nfet_01v8 l={mirror_length} w={mirror_width} m={mirror_fingers * mirror_multiplier}
X1 vdd vdd out gnd sky130_fd_pr__nfet_01v8 l={bias_length} w={bias_width} m={bias_fingers * bias_multiplier}
.ends