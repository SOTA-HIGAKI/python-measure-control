from time import sleep
import statistics
from pymeasure.instruments.srs.sr830 import SR830
import csv

LIA = SR830("GPIB0::8::INSTR")
# LIA.reset()
# print(LIA.id)
# print(LIA.sensitivity)
# LIA.sensitivity = 100e-6
# # offsetをかける
# LIA.auto_offset('Y')
# LIA.reference_source = 'Internal'
# LIA.reference_source_trigger = 'SINE'
# LIA.frequency = 200
ys = []
for i in range(100):
    ys.append(LIA.magnitude)
print(ys, statistics.mean(ys))
with open("result_noag.csv", "a", newline='') as r:
    cw = csv.writer(r)
    cw.writerow([statistics.mean(ys)])