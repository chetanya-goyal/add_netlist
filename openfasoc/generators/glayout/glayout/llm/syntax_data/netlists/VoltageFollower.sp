* sky130_fd_pr__nfet_01v8
let gsc_width=2.5
let tet_width=2.5
let gsc_length=2.5
let tet_length=2.5
let gsc_multiplier=2
let tet_multiplier=2
let gsc_fingers=2
let tet_fingers=2


.subckt VoltageFollower iout gnd vin vout
X0 vout iout gnd gnd sky130_fd_pr__nfet_01v8 l={gsc_length} w={gsc_width} m={gsc_fingers * gsc_multiplier}
X1 iout vin vout vout sky130_fd_pr__nfet_01v8 l={tet_length} w={tet_width} m={tet_fingers * tet_multiplier}
.ends