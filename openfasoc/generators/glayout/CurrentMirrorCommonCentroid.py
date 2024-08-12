####
# Compiled Glayout
# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
# 2024-08-12 11:13:05.793896

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

def CurrentMirrorCommonCentroid_cell(
	pdk: MappedPDK,
	width: float, 
	length: float, 
	multiplier: int, 
):
	pdk.activate()
	CurrentMirrorCommonCentroid = Component(name="CurrentMirrorCommonCentroid")
	maxmetalsep = pdk.util_max_metal_seperation()
	double_maxmetalsep = 2*pdk.util_max_metal_seperation()
	triple_maxmetalsep = 3*pdk.util_max_metal_seperation()
	quadruple_maxmetalsep = 4*pdk.util_max_metal_seperation()
	# placing m1 centered at the origin
	m1 = common_centroid_ab_ba(pdk,**{'width': width, 'length': length, 'fingers': multiplier, 'rmult': 1, 'with_substrate_tap': False, 'with_dummy': True})
	m1_ref = prec_ref_center(m1)
	CurrentMirrorCommonCentroid.add(m1_ref)
	CurrentMirrorCommonCentroid.add_ports(m1_ref.get_ports_list(),prefix="m1_")
	CurrentMirrorCommonCentroid << smart_route(pdk,CurrentMirrorCommonCentroid.ports["m1_A_source_W"],CurrentMirrorCommonCentroid.ports["m1_B_source_W"],m1_ref,CurrentMirrorCommonCentroid,**{})
	CurrentMirrorCommonCentroid << smart_route(pdk,CurrentMirrorCommonCentroid.ports["m1_A_gate_W"],CurrentMirrorCommonCentroid.ports["m1_B_gate_W"],m1_ref,CurrentMirrorCommonCentroid,**{})
	CurrentMirrorCommonCentroid << smart_route(pdk,CurrentMirrorCommonCentroid.ports["m1_A_gate_W"],CurrentMirrorCommonCentroid.ports["m1_A_drain_W"],m1_ref,CurrentMirrorCommonCentroid,**{})
	return CurrentMirrorCommonCentroid
