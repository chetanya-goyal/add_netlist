# General Context on Electronic Circuits

## Transistor Configurations 

Series Transistors: Say we have 2 or more transistors m1, m2 and so on. They are said to be connected in series when the source of one transistor (say m1) is connected to the drain of another transistor (say m2). If there are more than two transistors. The topmost transistor is said to be the one which doesn't have its drain connected to anything in series, and the bottom most transistor is said to be the one which doesn't have its source connected to anything in series. 

Parallel Transistors: Two or more transistors are said to be connected in parallel when their corresponding ports are connected together. Say we have m1 and m2 in parallel. This means the drains of m1 and m2 are shorted, the gates of m1 and m2 are shorted and the sources of m1 and m2 are shorted. This kind of parallel transistor acts as a single transistor with twice the width of any one of the transistors in parallel. 

## Transistor Placement Techniques / Matching

Interdigitated or Interdigitized: This kind of transistor matching technique places 2 or more transistors (say A, B, C and so on) such that the transistors are placed in the following pattern - A B C A B C. Additionally, the routing is such that each copy of a transistor is in parallel with its other copies - so all A's would be connected in parallel, all B's would be connected in parallel, and so on. 

Common Centroid: this kind of transistor matching techniques places transistors (say A and B) in the following pattern - A B B A. Additionally, the routing is such that each copy of a transistor is in parallel with its other copies - so all A's would be connected in parallel, all B's would be connected in parallel, and so on. 

IMPORTANT: There are already matched placement techniques available as usable functions in the glayout codebase, these need not be implemented from scratch when generating strict syntax. 

## Routing guidelines 
1. Suppose there are two mimcap components placed vertically or horizontally adjacent to each other. When routing between their top metals, it is preferable to use the straight route function in the following way
Assume m1 is above m2 (they are mimcaps)
route between m1_top_met_S and m2_top_met_N using straight_route with width 1

Similarly, assume m1 is to the right of m2
route between m1_top_met_W and m2_top_met_E using straight_route with width 1

2. Suppose you are routing the drain or source terminal of a transistor (say A) placed ABOVE or BELOW another transistor (say B). It is preferable that the same edge of the two ports be routed together so that the route doesn't cut across a component. For example, when routing the drain of A to the drain of B do either of the following 

route between A_drain_E and B_drain_E using smart_route

or 

route between A_drain_W and B_drain_W using smart_route

3. Suppose you are routing a transistor (say A) placed to the LEFT or RIGHT of another transistor (say B). If the same terminals are being routed (that is, gate to gate, drain to drain or source to source) it is preferable to use straight route.

4. VERY IMPORTANT - If there are multiple routes in a single transistor or even between two transistors, try to select the edges such that unintended routes do not end up coinciding. This would lead to LVS issues. 


## Miscellaneous Terminology

### Cross Coupled Inverters 
This involves placing two inverters and connecting the output of one to the input of the other. This can be done using two pmos transistors called pleft and pright, and two nmos transistors called nleft and nright. pleft and pright should be moved above nleft and nright respectively. Then routing should be done between the following port pairs - 
drain of pleft to drain of nleft
gate of pleft to gate of nleft
drain of pright to drain of nright
gate of pright to gate of nright
drain of nright to gate of nleft (use straight route as they are in line with each other)
drain of pleft to gate of pright (use straight route as they are in line with each other)

### Cross Coupled Transistors 
In a cross coupled pair (or XCP) two transistors, either both nmos or both pmos, are used. The gate of each transistor is routed to the drain of the other transistor.   