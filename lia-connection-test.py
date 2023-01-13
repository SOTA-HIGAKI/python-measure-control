from time import sleep
from pymeasure.instruments.srs.sr830 import SR830

LIA = SR830("GPIB0::8::INSTR")
LIA.reset()
print(LIA.id)
print(LIA.sensitivity)
LIA.sensitivity = 100e-6
# offsetをかける
LIA.auto_offset('Y')
LIA.reference_source = 'Internal'
LIA.reference_source_trigger = 'SINE'
LIA.frequency = 200
xy = LIA.y
print(f"xy:{abs(xy)}")

# ストリーミング読み込み：宿題