####
# Compiled Glayout
# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
# 2024-08-05 08:40:08.093728

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

def MimCapArray_cell(
	pdk: MappedPDK,
	size: float, 
):
	pdk.activate()
	MimCapArray = Component(name="MimCapArray")
	maxmetalsep = pdk.util_max_metal_seperation()
	double_maxmetalsep = 2*pdk.util_max_metal_seperation()
	triple_maxmetalsep = 3*pdk.util_max_metal_seperation()
	quadruple_maxmetalsep = 4*pdk.util_max_metal_seperation()
	# placing m1 centered at the origin
	m1 = mimcap(pdk,**{'size': size})
	m1_ref = prec_ref_center(m1)
	MimCapArray.add(m1_ref)
	MimCapArray.add_ports(m1_ref.get_ports_list(),prefix="m1_")
	# placing m2 centered at the origin
	m2 = mimcap(pdk,**{'size': size})
	m2_ref = prec_ref_center(m2)
	MimCapArray.add(m2_ref)
	MimCapArray.add_ports(m2_ref.get_ports_list(),prefix="m2_")
	# placing m3 centered at the origin
	m3 = mimcap(pdk,**{'size': size})
	m3_ref = prec_ref_center(m3)
	MimCapArray.add(m3_ref)
	MimCapArray.add_ports(m3_ref.get_ports_list(),prefix="m3_")
	# placing m4 centered at the origin
	m4 = mimcap(pdk,**{'size': size})
	m4_ref = prec_ref_center(m4)
	MimCapArray.add(m4_ref)
	MimCapArray.add_ports(m4_ref.get_ports_list(),prefix="m4_")
	# placing m5 centered at the origin
	m5 = mimcap(pdk,**{'size': size})
	m5_ref = prec_ref_center(m5)
	MimCapArray.add(m5_ref)
	MimCapArray.add_ports(m5_ref.get_ports_list(),prefix="m5_")
	# placing m6 centered at the origin
	m6 = mimcap(pdk,**{'size': size})
	m6_ref = prec_ref_center(m6)
	MimCapArray.add(m6_ref)
	MimCapArray.add_ports(m6_ref.get_ports_list(),prefix="m6_")
	# move m2 right m1
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(m1_ref,3) + center_to_edge_distance(m2_ref,1))
	movex(m2_ref,destination=(relativemovcorrection_0 + m1_ref.center[0]))
	remove_ports_with_prefix(MimCapArray,"m2_")
	MimCapArray.add_ports(m2_ref.get_ports_list(),prefix="m2_")
	# move m3 right m2
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(m2_ref,3) + center_to_edge_distance(m3_ref,1))
	movex(m3_ref,destination=(relativemovcorrection_0 + m2_ref.center[0]))
	remove_ports_with_prefix(MimCapArray,"m3_")
	MimCapArray.add_ports(m3_ref.get_ports_list(),prefix="m3_")
	# move m4 below m1
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(m1_ref,4) + center_to_edge_distance(m4_ref,2))
	movey(m4_ref,destination=(relativemovcorrection_0 + m1_ref.center[1]))
	remove_ports_with_prefix(MimCapArray,"m4_")
	MimCapArray.add_ports(m4_ref.get_ports_list(),prefix="m4_")
	# move m5 right m4
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(m4_ref,3) + center_to_edge_distance(m5_ref,1))
	movex(m5_ref,destination=(relativemovcorrection_0 + m4_ref.center[0]))
	remove_ports_with_prefix(MimCapArray,"m5_")
	MimCapArray.add_ports(m5_ref.get_ports_list(),prefix="m5_")
	# move m6 right m5
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(m5_ref,3) + center_to_edge_distance(m6_ref,1))
	movex(m6_ref,destination=(relativemovcorrection_0 + m5_ref.center[0]))
	remove_ports_with_prefix(MimCapArray,"m6_")
	MimCapArray.add_ports(m6_ref.get_ports_list(),prefix="m6_")
	# move m5 below m1
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(m1_ref,4) + center_to_edge_distance(m5_ref,2))
	movey(m5_ref,destination=(relativemovcorrection_0 + m1_ref.center[1]))
	remove_ports_with_prefix(MimCapArray,"m5_")
	MimCapArray.add_ports(m5_ref.get_ports_list(),prefix="m5_")
	# move m6 below m2
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(m2_ref,4) + center_to_edge_distance(m6_ref,2))
	movey(m6_ref,destination=(relativemovcorrection_0 + m2_ref.center[1]))
	remove_ports_with_prefix(MimCapArray,"m6_")
	MimCapArray.add_ports(m6_ref.get_ports_list(),prefix="m6_")
	MimCapArray << straight_route(pdk,MimCapArray.ports["m1_top_met_E"],MimCapArray.ports["m2_top_met_W"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m2_top_met_E"],MimCapArray.ports["m3_top_met_W"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m4_top_met_E"],MimCapArray.ports["m5_top_met_W"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m5_top_met_E"],MimCapArray.ports["m6_top_met_W"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m1_top_met_S"],MimCapArray.ports["m4_top_met_N"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m2_top_met_S"],MimCapArray.ports["m5_top_met_N"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m3_top_met_S"],MimCapArray.ports["m6_top_met_N"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m1_bottom_met_E"],MimCapArray.ports["m2_bottom_met_W"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m2_bottom_met_E"],MimCapArray.ports["m3_bottom_met_W"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m4_bottom_met_E"],MimCapArray.ports["m5_bottom_met_W"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m5_bottom_met_E"],MimCapArray.ports["m6_bottom_met_W"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m1_bottom_met_S"],MimCapArray.ports["m4_bottom_met_N"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m2_bottom_met_S"],MimCapArray.ports["m5_bottom_met_N"],**{'width': 1})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m3_bottom_met_S"],MimCapArray.ports["m6_bottom_met_N"],**{'width': 1})
	return MimCapArray
