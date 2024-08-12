####
# Compiled Glayout
# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
# 2024-08-12 19:00:20.233342

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

def InterdigitatedNMOS_cell(
	pdk: MappedPDK,
	top_numcols: int, 
	bottom_numcols: int, 
	top_width: float, 
	bottom_width: float, 
	top_length: float, 
	bottom_length: float, 
	top_multiplier: int, 
	bottom_multiplier: int, 
	top_fingers: int, 
	bottom_fingers: int, 
	n_ref_width: float, 
	n_mirr_width: float, 
	n_ref_length: float, 
	n_mirr_length: float, 
	n_ref_multiplier: int, 
	n_mirr_multiplier: int, 
	n_ref_fingers: int, 
	n_mirr_fingers: int, 
	p_ref_width: float, 
	p_mirr_width: float, 
	p_ref_length: float, 
	p_mirr_length: float, 
	p_ref_multiplier: int, 
	p_mirr_multiplier: int, 
	p_ref_fingers: int, 
	p_mirr_fingers: int, 
):
	pdk.activate()
	InterdigitatedNMOS = Component(name="InterdigitatedNMOS")
	maxmetalsep = pdk.util_max_metal_seperation()
	double_maxmetalsep = 2*pdk.util_max_metal_seperation()
	triple_maxmetalsep = 3*pdk.util_max_metal_seperation()
	quadruple_maxmetalsep = 4*pdk.util_max_metal_seperation()
	# placing top centered at the origin
	top = two_pfet_interdigitized(pdk,**{'numcols': top_numcols, 'with_substrate_tap': False, 'with_tie': True, 'dummy': True})
	top_ref = prec_ref_center(top)
	InterdigitatedNMOS.add(top_ref)
	InterdigitatedNMOS.add_ports(top_ref.get_ports_list(),prefix="top_")
	# placing bottom centered at the origin
	bottom = two_nfet_interdigitized(pdk,**{'numcols': bottom_numcols, 'with_substrate_tap': False, 'with_tie': True, 'dummy': True})
	bottom_ref = prec_ref_center(bottom)
	InterdigitatedNMOS.add(bottom_ref)
	InterdigitatedNMOS.add_ports(bottom_ref.get_ports_list(),prefix="bottom_")
	# placing n_ref centered at the origin
	n_ref = nmos(pdk,**{'width': n_ref_width, 'length': n_ref_length, 'fingers': n_ref_fingers, 'rmult': 1, 'multipliers': n_ref_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'with_dnwell': False})
	n_ref_ref = prec_ref_center(n_ref)
	InterdigitatedNMOS.add(n_ref_ref)
	InterdigitatedNMOS.add_ports(n_ref_ref.get_ports_list(),prefix="n_ref_")
	# placing n_mirr centered at the origin
	n_mirr = nmos(pdk,**{'width': n_mirr_width, 'length': n_mirr_length, 'fingers': n_mirr_fingers, 'rmult': 1, 'multipliers': n_mirr_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'with_dnwell': False})
	n_mirr_ref = prec_ref_center(n_mirr)
	InterdigitatedNMOS.add(n_mirr_ref)
	InterdigitatedNMOS.add_ports(n_mirr_ref.get_ports_list(),prefix="n_mirr_")
	# placing p_ref centered at the origin
	p_ref = pmos(pdk,**{'width': p_ref_width, 'length': p_ref_length, 'fingers': p_ref_fingers, 'rmult': 1, 'multipliers': p_ref_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'dnwell': False})
	p_ref_ref = prec_ref_center(p_ref)
	InterdigitatedNMOS.add(p_ref_ref)
	InterdigitatedNMOS.add_ports(p_ref_ref.get_ports_list(),prefix="p_ref_")
	# placing p_mirr centered at the origin
	p_mirr = pmos(pdk,**{'width': p_mirr_width, 'length': p_mirr_length, 'fingers': p_mirr_fingers, 'rmult': 1, 'multipliers': p_mirr_multiplier, 'with_substrate_tap': False, 'with_tie': True, 'with_dummy': True, 'dnwell': False})
	p_mirr_ref = prec_ref_center(p_mirr)
	InterdigitatedNMOS.add(p_mirr_ref)
	InterdigitatedNMOS.add_ports(p_mirr_ref.get_ports_list(),prefix="p_mirr_")
	# move bottom left top
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(top_ref,1) + center_to_edge_distance(bottom_ref,3))
	movex(bottom_ref,destination=(relativemovcorrection_0 + top_ref.center[0]))
	remove_ports_with_prefix(InterdigitatedNMOS,"bottom_")
	InterdigitatedNMOS.add_ports(bottom_ref.get_ports_list(),prefix="bottom_")
	# move n_ref below bottom
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(bottom_ref,4) + center_to_edge_distance(n_ref_ref,2))
	movey(n_ref_ref,destination=(relativemovcorrection_0 + bottom_ref.center[1]))
	remove_ports_with_prefix(InterdigitatedNMOS,"n_ref_")
	InterdigitatedNMOS.add_ports(n_ref_ref.get_ports_list(),prefix="n_ref_")
	# move n_mirr below bottom
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(bottom_ref,4) + center_to_edge_distance(n_mirr_ref,2))
	movey(n_mirr_ref,destination=(relativemovcorrection_0 + bottom_ref.center[1]))
	remove_ports_with_prefix(InterdigitatedNMOS,"n_mirr_")
	InterdigitatedNMOS.add_ports(n_mirr_ref.get_ports_list(),prefix="n_mirr_")
	# move n_ref left n_mirr
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(n_mirr_ref,1) + center_to_edge_distance(n_ref_ref,3))
	movex(n_ref_ref,destination=(relativemovcorrection_0 + n_mirr_ref.center[0]))
	remove_ports_with_prefix(InterdigitatedNMOS,"n_ref_")
	InterdigitatedNMOS.add_ports(n_ref_ref.get_ports_list(),prefix="n_ref_")
	# move p_ref above top
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(top_ref,2) + center_to_edge_distance(p_ref_ref,4))
	movey(p_ref_ref,destination=(relativemovcorrection_0 + top_ref.center[1]))
	remove_ports_with_prefix(InterdigitatedNMOS,"p_ref_")
	InterdigitatedNMOS.add_ports(p_ref_ref.get_ports_list(),prefix="p_ref_")
	# move p_mirr above top
	relativemovcorrection_0 = 1*(maxmetalsep + center_to_edge_distance(top_ref,2) + center_to_edge_distance(p_mirr_ref,4))
	movey(p_mirr_ref,destination=(relativemovcorrection_0 + top_ref.center[1]))
	remove_ports_with_prefix(InterdigitatedNMOS,"p_mirr_")
	InterdigitatedNMOS.add_ports(p_mirr_ref.get_ports_list(),prefix="p_mirr_")
	# move p_ref left p_mirr
	relativemovcorrection_0 = -1*(maxmetalsep + center_to_edge_distance(p_mirr_ref,1) + center_to_edge_distance(p_ref_ref,3))
	movex(p_ref_ref,destination=(relativemovcorrection_0 + p_mirr_ref.center[0]))
	remove_ports_with_prefix(InterdigitatedNMOS,"p_ref_")
	InterdigitatedNMOS.add_ports(p_ref_ref.get_ports_list(),prefix="p_ref_")
	InterdigitatedNMOS << c_route(pdk,InterdigitatedNMOS.ports["top_A_source_W"],InterdigitatedNMOS.ports["bottom_A_source_W"],**{})
	InterdigitatedNMOS << c_route(pdk,InterdigitatedNMOS.ports["top_A_gate_W"],InterdigitatedNMOS.ports["bottom_A_gate_W"],**{})
	InterdigitatedNMOS << c_route(pdk,InterdigitatedNMOS.ports["top_B_source_E"],InterdigitatedNMOS.ports["bottom_B_source_E"],**{})
	InterdigitatedNMOS << c_route(pdk,InterdigitatedNMOS.ports["top_B_gate_E"],InterdigitatedNMOS.ports["bottom_B_gate_E"],**{})
	InterdigitatedNMOS << straight_route(pdk,InterdigitatedNMOS.ports["n_ref_gate_W"],InterdigitatedNMOS.ports["n_mirr_gate_W"],**{})
	InterdigitatedNMOS << straight_route(pdk,InterdigitatedNMOS.ports["n_ref_source_W"],InterdigitatedNMOS.ports["n_mirr_source_W"],**{})
	InterdigitatedNMOS << straight_route(pdk,InterdigitatedNMOS.ports["p_ref_gate_W"],InterdigitatedNMOS.ports["p_mirr_gate_W"],**{})
	InterdigitatedNMOS << straight_route(pdk,InterdigitatedNMOS.ports["p_ref_source_W"],InterdigitatedNMOS.ports["p_mirr_source_W"],**{})
	InterdigitatedNMOS << c_route(pdk,InterdigitatedNMOS.ports["p_ref_drain_W"],InterdigitatedNMOS.ports["top_A_source_W"],**{})
	InterdigitatedNMOS << c_route(pdk,InterdigitatedNMOS.ports["p_mirr_gate_W"],InterdigitatedNMOS.ports["top_B_drain_W"],**{})
	InterdigitatedNMOS << c_route(pdk,InterdigitatedNMOS.ports["n_ref_drain_W"],InterdigitatedNMOS.ports["bottom_A_source_W"],**{})
	InterdigitatedNMOS << c_route(pdk,InterdigitatedNMOS.ports["n_mirr_gate_W"],InterdigitatedNMOS.ports["bottom_B_drain_W"],**{})
	InterdigitatedNMOS << c_route(pdk,InterdigitatedNMOS.ports["n_mirr_drain_W"],InterdigitatedNMOS.ports["p_mirr_drain_W"],**{})
	return InterdigitatedNMOS
