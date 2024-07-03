let cascode_width = 2.5
let feedback_width = 2.5
let cascode_length = 2.5
let feedback_length = 2.5
let cascode_multiplier = 2
let feedback_multiplier = 2
let cascode_fingers = 2
let feedback_fingers = 2

.subckt RegulatedCascode
X0 out drain1 gate1 gnd sky130_fd_pr__nfet_01v8 l={cascode_length} w={cascode_width} m={cascode_fingers * cascode_multiplier}
X1 drain1 gate1 source1 gnd sky130_fd_pr__nfet_01v8 l={feedback_length} w={feedback_width} m={feedback_fingers * feedback_multiplier}
.ends