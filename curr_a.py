

import csv
import statistics
import time
import pyvisa
from pymeasure.instruments.srs.sr830 import SR830


IMIN = 0  # 初期電流値
IMAX = 0.8 * 10  # MAX電流値 /
DURATION = 0.1 * 10  # 間隔

DCB_ADDR = "USB0::0x0B3E::0x1029::WD000275::INSTR"
rm = pyvisa.ResourceManager()
DCB = rm.open_resource(DCB_ADDR)
DCB.write('OUTP 1')  # type: ignore

iList = []  # 電源Aの電流リスト
x = IMIN
while x <= IMAX:
    iList.append(x)
    x += DURATION
x = IMAX
while x > IMIN + 0.0001:
    x -= DURATION
    iList.append(x)
print(iList)
LIA = SR830("GPIB0::8::INSTR")
# LIA.reset()

# LIA.sensitivity = 100e-6
# # offsetをかける
# LIA.auto_offset('Y')
# LIA.reference_source = 'External'
# LIA.reference_source_trigger = 'SINE'
# LIA.frequency = 200
with open("0215_6.csv", "a", newline='') as f:
    cw = csv.writer(f)
    for i, aOut in enumerate(iList):
        DCB.write(f'VOLT {aOut / 10}')  # type: ignore
        time.sleep(30.0)
        mg = []
        x = []
        y = []
        for i in range(100):
            time.sleep(0.03)
            mg.append(LIA.magnitude)
            x.append(LIA.x)
            y.append(LIA.y)
        DCB.write(f"MEAS:VOLT?")
        cw.writerow([float(DCB.read()), statistics.mean(mg), statistics.mean(x), statistics.mean(y)])

# print(mg)
# plt.plot(np.array(iList) ,np.array(mg))
# plt.show()
