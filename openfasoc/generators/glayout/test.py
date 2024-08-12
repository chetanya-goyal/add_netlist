# from glayout.llm.manage_data import load_preprocessed_data_in_messages_format
# from glayout.llm.rag import RAGdb
# import pathlib
# import sys, os
# # sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
# prompt = 'Create an nfet differential pair. Do not use any matching techniques, simply place 2 nfets side by side and route their sources.'

# RAGvecdb = RAGdb(pathlib.Path(__file__).resolve().parent / "glayout" / "llm" / "rag_data")
# # train
# acx = load_preprocessed_data_in_messages_format()

from MimCapArray import MimCapArray_cell
from DifferentialPair import DifferentialPair_cell
from CurrentMirrorCommonCentroid import CurrentMirrorCommonCentroid_cell
from WilsonCurrentMirror import WilsonCurrentMirror_cell
from glayout.flow.pdk.sky130_mapped import sky130_mapped_pdk as sky
from InterdigitatedNMOS import InterdigitatedNMOS_cell    

# comp = MimCapArray_cell(sky, 5, 5)
# comp.name = 'mimcp'
# comp.write_gds('a.gds')

# comp = CurrentMirrorCommonCentroid_cell(sky, 5, 1, 1)
# comp.name = 'yes'
# comp.write_gds('a.gds')

# comp = DifferentialPair_cell(sky, 5, 1, 1)
# comp.name = 'yes'
# comp.write_gds('a.gds')

# comp = WilsonCurrentMirror_cell(sky, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# comp.name = 'yes'
# comp.write_gds('a.gds')

comp = InterdigitatedNMOS_cell(sky, 2, 2, 5, 5, 1, 1, 1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 1, 1, 5, 5, 1, 1,  1, 1, 1, 1)
comp.name = 'yes'
comp.write_gds('a.gds')
