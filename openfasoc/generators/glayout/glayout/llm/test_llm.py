import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from train_and_run import GlayoutLLMSessionHandler

custom = GlayoutLLMSessionHandler()
out = custom.generate("create an n-type current mirror with two transistors with width and length as parameters")
print("...done....")
with open("curroutput.convo", 'w') as f:
    f.write(out)
# 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