let srcfoll_width = 2.5
let isrc_width = 2.5
let srcfoll_length = 2.5
let isrc_length = 2.5
let srcfoll_multiplier = 2
let isrc_multiplier = 2
let srcfoll_fingers = 2
let isrc_fingers = 2

.subckt SourceFollow
X0 out vb gnd gnd sky130_fd_pr__nfet_01v8 l={isrc_length} w={isrc_width} m={isrc_fingers * isrc_multiplier}
X1 vdd vin out gnd sky130_fd_pr__nfet_01v8 l={srcfoll_length} w={srcfoll_width} m={srcfoll_fingers * srcfoll_multiplier}
.ends
