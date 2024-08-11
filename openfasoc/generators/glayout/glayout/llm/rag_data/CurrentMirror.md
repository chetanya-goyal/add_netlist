# Current Mirror or Current Source
A current mirror is a circuit designed to copy a current. It uses either two pmos or two nmos transistors. Current is copied from a transistor called reference to the other transistor called mirror. The ratio of the current in the drain of the reference to the current in the drain of mirror is equal to the ratio the W/L of the mirror to the W/L of the reference. This is a very important circuit, often used as a current source in many analog circuits. 

## Routing 
Only route together these ports, nothing else
1. Connect the source of reference to the source of mirror. 
2. Connect the gate of reference to the gate of mirror. 
3. Connect the drain of reference to the gate of reference.