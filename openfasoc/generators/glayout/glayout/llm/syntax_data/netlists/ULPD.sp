let forward_width = 2.5
let leakred_width = 2.5
let forward_length = 2.5
let leakred_length = 2.5
let forward_multiplier = 2
let leakred_multiplier = 2
let forward_fingers = 2
let leakred_fingers = 2

.subckt ULPD Vp Vn
X0 Vd Vn Vp Vp sky130_fd_pr__pfet_01v8 l={forward_length} w={forward_width} m={forward_fingers * forward_multiplier}
X1 Vd Vp Vn Vn sky130_fd_pr__nfet_01v8 l={leakred_length} w={leakred_width} m={leakred_fingers * leakred_multiplier}
.ends