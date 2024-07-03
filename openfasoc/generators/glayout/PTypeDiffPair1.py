####
# Compiled Glayout
# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
# 2024-07-02 16:50:21.507955

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

def PTypeDiffPair_cell(
	pdk: MappedPDK,
	vin1_width: float, 
	vin2_width: float, 
	vin1_length: float, 
	vin2_length: float, 
	vin1_multiplier: int, 
	vin2_multiplier: int, 
	vin1_fingers: int, 
	vin2_fingers: int, 
):
	pdk.activate()
	PTypeDiffPair = Component(name="PTypeDiffPair")
	maxmetalsep = pdk.util_max_metal_seperation()
	double_maxmetalsep = 2*pdk.util_max_metal_seperation()
	triple_maxmetalsep = 3*pdk.util_max_metal_seperation()
	quadruple_maxmetalsep = 4*pdk.util_max_metal_seperation()
	# placing vin1 centered at the origin
	vin1 = pmos(pdk,**{'width': vin1_width, 'length': vin1_length, 'fingers': vin1_fingers, 'rmult': 1, 'multipliers': vin1_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True})
	vin1_ref = prec_ref_center(vin1)
	PTypeDiffPair.add(vin1_ref)
	PTypeDiffPair.add_ports(vin1_ref.get_ports_list(),prefix="vin1_")
	# placing vin2 centered at the origin
	vin2 = pmos(pdk,**{'width': vin2_width, 'length': vin2_length, 'fingers': vin2_fingers, 'rmult': 1, 'multipliers': vin2_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True})
	vin2_ref = prec_ref_center(vin2)
	PTypeDiffPair.add(vin2_ref)
	PTypeDiffPair.add_ports(vin2_ref.get_ports_list(),prefix="vin2_")
	# move vin1 left vin2
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(vin2_ref,1) + center_to_edge_distance(vin1_ref,3))
	movex(vin1_ref,destination=(relativemovcorrection_0 + vin2_ref.center[0]))
	remove_ports_with_prefix(PTypeDiffPair,"vin1_")
	PTypeDiffPair.add_ports(vin1_ref.get_ports_list(),prefix="vin1_")
	PTypeDiffPair << smart_route(pdk,PTypeDiffPair.ports["vin1_source_E"],PTypeDiffPair.ports["vin2_source_W"],vin1_ref,PTypeDiffPair,**{})
	return PTypeDiffPair
