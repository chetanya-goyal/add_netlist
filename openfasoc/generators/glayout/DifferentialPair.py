####
# Compiled Glayout
# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
# 2024-08-12 09:43:54.994944

from glayout.flow.pdk.mappedpdk import MappedPDK
from gdsfactory import Component
from glayout.flow.pdk.util.comp_utils import move, movex, movey, prec_ref_center, evaluate_bbox, center_to_edge_distance
from glayout.flow.pdk.util.port_utils import remove_ports_with_prefix
from glayout.flow.primitives.fet import nmos
from glayout.flow.primitives.fet import pmos
from glayout.flow.primitives.guardring import tapring
from glayout.flow.primitives.mimcap import mimcap
from glayout.flow.primitives.mimcap import mimcap_array
from glayout.flow.primitives.via_gen import via_stack
from glayout.flow.primitives.via_gen import via_array
from glayout.flow.placement.two_transistor_interdigitized import two_nfet_interdigitized
from glayout.flow.placement.four_transistor_interdigitized import generic_4T_interdigitzed
from glayout.flow.placement.two_transistor_interdigitized import two_pfet_interdigitized
from glayout.flow.placement.common_centroid_ab_ba import common_centroid_ab_ba
from glayout.flow.blocks.diff_pair import diff_pair_generic
from glayout.flow.routing.smart_route import smart_route
from glayout.flow.routing.L_route import L_route
from glayout.flow.routing.c_route import c_route
from glayout.flow.routing.straight_route import straight_route

def DifferentialPair_cell(
	pdk: MappedPDK,
	width: float, 
	length: float, 
	fingers: int, 
):
	pdk.activate()
	DifferentialPair = Component(name="DifferentialPair")
	maxmetalsep = pdk.util_max_metal_seperation()
	double_maxmetalsep = 2*pdk.util_max_metal_seperation()
	triple_maxmetalsep = 3*pdk.util_max_metal_seperation()
	quadruple_maxmetalsep = 4*pdk.util_max_metal_seperation()
	# placing A centered at the origin
	A = pmos(pdk,**{'width': width, 'length': length, 'fingers': fingers, 'rmult': 1, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'dnwell': False})
	A_ref = prec_ref_center(A)
	DifferentialPair.add(A_ref)
	DifferentialPair.add_ports(A_ref.get_ports_list(),prefix="A_")
	# placing B centered at the origin
	B = pmos(pdk,**{'width': width, 'length': length, 'fingers': fingers, 'rmult': 1, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'dnwell': False})
	B_ref = prec_ref_center(B)
	DifferentialPair.add(B_ref)
	DifferentialPair.add_ports(B_ref.get_ports_list(),prefix="B_")
	# move B right A
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(A_ref,3) + center_to_edge_distance(B_ref,1))
	movex(B_ref,destination=(relativemovcorrection_0 + A_ref.center[0]))
	remove_ports_with_prefix(DifferentialPair,"B_")
	DifferentialPair.add_ports(B_ref.get_ports_list(),prefix="B_")
	DifferentialPair << smart_route(pdk,DifferentialPair.ports["A_source_W"],DifferentialPair.ports["B_source_W"],A_ref,DifferentialPair,**{})
	return DifferentialPair
