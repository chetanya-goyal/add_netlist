import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import glayout.syntaxer.dynamic_load
from glayout.flow.pdk.sky130_mapped import sky130_mapped_pdk as sky130
from pathlib import Path
from PTypeDiffPair1 import PTypeDiffPair_cell
convo_path = Path(__file__).parent.resolve() / "syntax_data" / "convos"
netlist_path = Path(__file__).parent.resolve() / "syntax_data" / "netlists"

done_so_far = ["ULPD.convo", "Varactor.convo", "VoltageFollower.convo", "SourceFollow.convo", "RegulatedCascode.convo", "PTypeDiffPair.convo", "PTATVoltageGen.convo", "NOR.convo", "NoiseXDiffConv.convo"]

# leaving out push pull

def run_lvs(convo_file, netlist_path):
    """Run LVS on a given conversation file and save the netlist to the given path"""
    try:
        session_code = glayout.syntaxer.dynamic_load.run_session(load_conversation=convo_file, restore_and_exit=True)
        comp = glayout.syntaxer.dynamic_load.run_glayout_code_cell(sky130, session_code)
        name = convo_file.resolve().stem.removesuffix(".convo")
        comp.name = name
        netlist_file = netlist_path / f"{name}.sp"
        
        sky130.lvs_netgen(comp, comp.name, netlist = netlist_file)
    except:
        print(f'Error running session with {convo_file}')
    os.system("rm *.ext")

def run_all():
    for convo_file in convo_path.iterdir():
        if str(convo_file.resolve().stem) + ".convo" not in done_so_far:
            continue
        run_lvs(convo_file, netlist_path)

def write_gds(convo_file):
    session_code = glayout.syntaxer.dynamic_load.run_session(load_conversation=convo_file, restore_and_exit=True)
    comp = glayout.syntaxer.dynamic_load.run_glayout_code_cell(sky130, session_code)
    comp.write_gds(convo_file.resolve().stem + ".gds")

run_lvs(convo_path / "NoiseXDiffConv.convo", netlist_path)
