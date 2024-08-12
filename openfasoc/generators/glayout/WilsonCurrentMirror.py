####
# Compiled Glayout
# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
# 2024-08-12 11:37:14.886004

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

def WilsonCurrentMirror_cell(
	pdk: MappedPDK,
	top_left_width: float, 
	top_right_width: float, 
	bottom_left_width: float, 
	bottom_right_width: float, 
	top_left_length: float, 
	top_right_length: float, 
	bottom_left_length: float, 
	bottom_right_length: float, 
	top_left_multiplier: int, 
	top_right_multiplier: int, 
	bottom_left_multiplier: int, 
	bottom_right_multiplier: int, 
	top_left_fingers: int, 
	top_right_fingers: int, 
	bottom_left_fingers: int, 
	bottom_right_fingers: int, 
):
	pdk.activate()
	WilsonCurrentMirror = Component(name="WilsonCurrentMirror")
	maxmetalsep = pdk.util_max_metal_seperation()
	double_maxmetalsep = 2*pdk.util_max_metal_seperation()
	triple_maxmetalsep = 3*pdk.util_max_metal_seperation()
	quadruple_maxmetalsep = 4*pdk.util_max_metal_seperation()
	# placing top_left centered at the origin
	top_left = nmos(pdk,**{'width': top_left_width, 'length': top_left_length, 'fingers': top_left_fingers, 'rmult': 1, 'multipliers': top_left_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'with_dnwell': False})
	top_left_ref = prec_ref_center(top_left)
	WilsonCurrentMirror.add(top_left_ref)
	WilsonCurrentMirror.add_ports(top_left_ref.get_ports_list(),prefix="top_left_")
	# placing top_right centered at the origin
	top_right = nmos(pdk,**{'width': top_right_width, 'length': top_right_length, 'fingers': top_right_fingers, 'rmult': 1, 'multipliers': top_right_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'with_dnwell': False})
	top_right_ref = prec_ref_center(top_right)
	WilsonCurrentMirror.add(top_right_ref)
	WilsonCurrentMirror.add_ports(top_right_ref.get_ports_list(),prefix="top_right_")
	# placing bottom_left centered at the origin
	bottom_left = nmos(pdk,**{'width': bottom_left_width, 'length': bottom_left_length, 'fingers': bottom_left_fingers, 'rmult': 1, 'multipliers': bottom_left_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'with_dnwell': False})
	bottom_left_ref = prec_ref_center(bottom_left)
	WilsonCurrentMirror.add(bottom_left_ref)
	WilsonCurrentMirror.add_ports(bottom_left_ref.get_ports_list(),prefix="bottom_left_")
	# placing bottom_right centered at the origin
	bottom_right = nmos(pdk,**{'width': bottom_right_width, 'length': bottom_right_length, 'fingers': bottom_right_fingers, 'rmult': 1, 'multipliers': bottom_right_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'with_dnwell': False})
	bottom_right_ref = prec_ref_center(bottom_right)
	WilsonCurrentMirror.add(bottom_right_ref)
	WilsonCurrentMirror.add_ports(bottom_right_ref.get_ports_list(),prefix="bottom_right_")
	# move top_left below bottom_left
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(bottom_left_ref,4) + center_to_edge_distance(top_left_ref,2))
	movey(top_left_ref,destination=(relativemovcorrection_0 + bottom_left_ref.center[1]))
	remove_ports_with_prefix(WilsonCurrentMirror,"top_left_")
	WilsonCurrentMirror.add_ports(top_left_ref.get_ports_list(),prefix="top_left_")
	# move top_right below bottom_right
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(bottom_right_ref,4) + center_to_edge_distance(top_right_ref,2))
	movey(top_right_ref,destination=(relativemovcorrection_0 + bottom_right_ref.center[1]))
	remove_ports_with_prefix(WilsonCurrentMirror,"top_right_")
	WilsonCurrentMirror.add_ports(top_right_ref.get_ports_list(),prefix="top_right_")
	# move top_right right top_left
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(top_left_ref,3) + center_to_edge_distance(top_right_ref,1))
	movex(top_right_ref,destination=(relativemovcorrection_0 + top_left_ref.center[0]))
	remove_ports_with_prefix(WilsonCurrentMirror,"top_right_")
	WilsonCurrentMirror.add_ports(top_right_ref.get_ports_list(),prefix="top_right_")
	# move bottom_right right bottom_left
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(bottom_left_ref,3) + center_to_edge_distance(bottom_right_ref,1))
	movex(bottom_right_ref,destination=(relativemovcorrection_0 + bottom_left_ref.center[0]))
	remove_ports_with_prefix(WilsonCurrentMirror,"bottom_right_")
	WilsonCurrentMirror.add_ports(bottom_right_ref.get_ports_list(),prefix="bottom_right_")
	WilsonCurrentMirror << smart_route(pdk,WilsonCurrentMirror.ports["top_left_gate_E"],WilsonCurrentMirror.ports["top_right_gate_E"],top_left_ref,WilsonCurrentMirror,**{})
	WilsonCurrentMirror << smart_route(pdk,WilsonCurrentMirror.ports["top_left_source_E"],WilsonCurrentMirror.ports["top_right_source_E"],top_left_ref,WilsonCurrentMirror,**{})
	WilsonCurrentMirror << smart_route(pdk,WilsonCurrentMirror.ports["bottom_left_gate_E"],WilsonCurrentMirror.ports["bottom_right_gate_E"],top_left_ref,WilsonCurrentMirror,**{})
	WilsonCurrentMirror << smart_route(pdk,WilsonCurrentMirror.ports["bottom_left_source_E"],WilsonCurrentMirror.ports["bottom_right_source_E"],top_left_ref,WilsonCurrentMirror,**{})
	WilsonCurrentMirror << smart_route(pdk,WilsonCurrentMirror.ports["top_left_drain_E"],WilsonCurrentMirror.ports["top_left_gate_E"],top_left_ref,WilsonCurrentMirror,**{})
	WilsonCurrentMirror << smart_route(pdk,WilsonCurrentMirror.ports["bottom_left_drain_E"],WilsonCurrentMirror.ports["bottom_left_gate_E"],top_left_ref,WilsonCurrentMirror,**{})
	WilsonCurrentMirror << smart_route(pdk,WilsonCurrentMirror.ports["top_left_source_E"],WilsonCurrentMirror.ports["bottom_right_drain_E"],top_left_ref,WilsonCurrentMirror,**{})
	WilsonCurrentMirror << smart_route(pdk,WilsonCurrentMirror.ports["top_right_source_E"],WilsonCurrentMirror.ports["bottom_left_drain_E"],top_left_ref,WilsonCurrentMirror,**{})
	return WilsonCurrentMirror
