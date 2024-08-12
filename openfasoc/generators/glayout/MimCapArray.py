####
# Compiled Glayout
# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
# 2024-08-12 13:44:46.902139

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
	width: float, 
	height: float, 
):
	pdk.activate()
	MimCapArray = Component(name="MimCapArray")
	maxmetalsep = pdk.util_max_metal_seperation()
	double_maxmetalsep = 2*pdk.util_max_metal_seperation()
	triple_maxmetalsep = 3*pdk.util_max_metal_seperation()
	quadruple_maxmetalsep = 4*pdk.util_max_metal_seperation()
	# placing m_0_0 centered at the origin
	m_0_0 = mimcap(pdk,**{'size': ( width , height )})
	m_0_0_ref = prec_ref_center(m_0_0)
	MimCapArray.add(m_0_0_ref)
	MimCapArray.add_ports(m_0_0_ref.get_ports_list(),prefix="m_0_0_")
	# placing m_0_1 centered at the origin
	m_0_1 = mimcap(pdk,**{'size': ( width , height )})
	m_0_1_ref = prec_ref_center(m_0_1)
	MimCapArray.add(m_0_1_ref)
	MimCapArray.add_ports(m_0_1_ref.get_ports_list(),prefix="m_0_1_")
	# placing m_0_2 centered at the origin
	m_0_2 = mimcap(pdk,**{'size': ( width , height )})
	m_0_2_ref = prec_ref_center(m_0_2)
	MimCapArray.add(m_0_2_ref)
	MimCapArray.add_ports(m_0_2_ref.get_ports_list(),prefix="m_0_2_")
	# placing m_1_0 centered at the origin
	m_1_0 = mimcap(pdk,**{'size': ( width , height )})
	m_1_0_ref = prec_ref_center(m_1_0)
	MimCapArray.add(m_1_0_ref)
	MimCapArray.add_ports(m_1_0_ref.get_ports_list(),prefix="m_1_0_")
	# placing m_1_1 centered at the origin
	m_1_1 = mimcap(pdk,**{'size': ( width , height )})
	m_1_1_ref = prec_ref_center(m_1_1)
	MimCapArray.add(m_1_1_ref)
	MimCapArray.add_ports(m_1_1_ref.get_ports_list(),prefix="m_1_1_")
	# placing m_1_2 centered at the origin
	m_1_2 = mimcap(pdk,**{'size': ( width , height )})
	m_1_2_ref = prec_ref_center(m_1_2)
	MimCapArray.add(m_1_2_ref)
	MimCapArray.add_ports(m_1_2_ref.get_ports_list(),prefix="m_1_2_")
	# move m_0_1 right m_0_0
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(m_0_0_ref,3) + center_to_edge_distance(m_0_1_ref,1))
	movex(m_0_1_ref,destination=(relativemovcorrection_0 + m_0_0_ref.center[0]))
	remove_ports_with_prefix(MimCapArray,"m_0_1_")
	MimCapArray.add_ports(m_0_1_ref.get_ports_list(),prefix="m_0_1_")
	# move m_0_2 right m_0_1
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(m_0_1_ref,3) + center_to_edge_distance(m_0_2_ref,1))
	movex(m_0_2_ref,destination=(relativemovcorrection_0 + m_0_1_ref.center[0]))
	remove_ports_with_prefix(MimCapArray,"m_0_2_")
	MimCapArray.add_ports(m_0_2_ref.get_ports_list(),prefix="m_0_2_")
	# move m_1_0 below m_0_0
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(m_0_0_ref,4) + center_to_edge_distance(m_1_0_ref,2))
	movey(m_1_0_ref,destination=(relativemovcorrection_0 + m_0_0_ref.center[1]))
	remove_ports_with_prefix(MimCapArray,"m_1_0_")
	MimCapArray.add_ports(m_1_0_ref.get_ports_list(),prefix="m_1_0_")
	# move m_1_1 below m_0_0
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(m_0_0_ref,4) + center_to_edge_distance(m_1_1_ref,2))
	movey(m_1_1_ref,destination=(relativemovcorrection_0 + m_0_0_ref.center[1]))
	remove_ports_with_prefix(MimCapArray,"m_1_1_")
	MimCapArray.add_ports(m_1_1_ref.get_ports_list(),prefix="m_1_1_")
	# move m_1_2 below m_0_0
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(m_0_0_ref,4) + center_to_edge_distance(m_1_2_ref,2))
	movey(m_1_2_ref,destination=(relativemovcorrection_0 + m_0_0_ref.center[1]))
	remove_ports_with_prefix(MimCapArray,"m_1_2_")
	MimCapArray.add_ports(m_1_2_ref.get_ports_list(),prefix="m_1_2_")
	# move m_1_1 right m_1_0
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(m_1_0_ref,3) + center_to_edge_distance(m_1_1_ref,1))
	movex(m_1_1_ref,destination=(relativemovcorrection_0 + m_1_0_ref.center[0]))
	remove_ports_with_prefix(MimCapArray,"m_1_1_")
	MimCapArray.add_ports(m_1_1_ref.get_ports_list(),prefix="m_1_1_")
	# move m_1_2 right m_1_1
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(m_1_1_ref,3) + center_to_edge_distance(m_1_2_ref,1))
	movex(m_1_2_ref,destination=(relativemovcorrection_0 + m_1_1_ref.center[0]))
	remove_ports_with_prefix(MimCapArray,"m_1_2_")
	MimCapArray.add_ports(m_1_2_ref.get_ports_list(),prefix="m_1_2_")
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_0_top_met_E"],MimCapArray.ports["m_0_1_top_met_W"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_1_top_met_E"],MimCapArray.ports["m_0_2_top_met_W"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_1_0_top_met_E"],MimCapArray.ports["m_1_1_top_met_W"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_1_1_top_met_E"],MimCapArray.ports["m_1_2_top_met_W"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_0_top_met_S"],MimCapArray.ports["m_1_0_top_met_N"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_1_top_met_S"],MimCapArray.ports["m_1_1_top_met_N"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_2_top_met_S"],MimCapArray.ports["m_1_2_top_met_N"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_0_bottom_met_E"],MimCapArray.ports["m_0_1_bottom_met_W"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_1_bottom_met_E"],MimCapArray.ports["m_0_2_bottom_met_W"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_1_0_bottom_met_E"],MimCapArray.ports["m_1_1_bottom_met_W"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_1_1_bottom_met_E"],MimCapArray.ports["m_1_2_bottom_met_W"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_0_bottom_met_S"],MimCapArray.ports["m_1_0_bottom_met_N"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_1_bottom_met_S"],MimCapArray.ports["m_1_1_bottom_met_N"],**{})
	MimCapArray << straight_route(pdk,MimCapArray.ports["m_0_2_bottom_met_S"],MimCapArray.ports["m_1_2_bottom_met_N"],**{})
	return MimCapArray
