let vin1_width = 2.5
let vin2_width = 2.5
let vin1_length = 2.5
let vin2_length = 2.5
let vin1_multiplier = 2
let vin2_multiplier = 2
let vin1_fingers = 2
let vin2_fingers = 2

.subckt PTypeDiffPair
X0 ref vin1 commsource commsource sky130_fd_pr__pfet_01v8 l={vin1_length} w={vin1_width} m={vin1_fingers * vin1_multiplier}
X1 mirr vin2 commsource commsource sky130_fd_pr__pfet_01v8 l={vin2_length} w={vin2_width} m={vin2_fingers * vin2_multiplier}
.ends