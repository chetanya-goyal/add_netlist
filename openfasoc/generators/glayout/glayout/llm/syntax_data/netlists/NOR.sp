let pullup_width = 2.5
let pulldown_width = 2.5
let pullup_length = 2.5
let pulldown_length = 2.5
let pullup_multiplier = 2
let pulldown_multiplier = 2 
let pullup_fingers = 2
let pulldown_fingers = 2 

.subckt NOR 
XP1 psource A vdd vdd sky130_fd_pr__pfet_01v8 l={pullup_length} w={pullup_width} m={pullup_fingers * pullup_multiplier}
XP2 out B psource vdd sky130_fd_pr__pfet_01v8 l={pulldown_length} w={pulldown_width} m={pulldown_fingers * pulldown_multiplier}
XN1 out A gnd gnd sky130_fd_pr__nfet_01v8 l={pulldown_length} w={pulldown_width} m={pulldown_fingers * pulldown_multiplier}
XN2 out B gnd gnd sky130_fd_pr__nfet_01v8 l={pullup_length} w={pullup_width} m={pullup_fingers * pullup_multiplier}
.ends