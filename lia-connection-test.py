from time import sleep
from pymeasure.instruments.srs.sr830 import SR830

LIA = SR830("GPIB0::8::INSTR")
LIA.reset()
print(LIA.id)
print(LIA.sensitivity)
xy = LIA.xy
print(f"xy:{xy}")

# ストリーミング読み込み：宿題