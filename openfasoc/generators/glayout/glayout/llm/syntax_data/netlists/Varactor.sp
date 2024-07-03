let control_width = 2.5
let accumulation_width = 2.5
let control_length = 2.5
let accumulation_length = 2.5
let control_multiplier = 2
let accumulation_multiplier = 2
let control_fingers = 2
let accumulation_fingers = 2

.subckt Varactor Vp Vn Vbias
X0 Vbias Vp Vbias Vbias sky130_fd_pr__nfet_01v8 l={control_length} w={control_width} m={control_fingers * control_multiplier}
X1 Vbias Vn Vbias Vbias sky130_fd_pr__nfet_01v8 l={accumulation_length} w={accumulation_width} m={accumulation_fingers * accumulation_multiplier}
.ends