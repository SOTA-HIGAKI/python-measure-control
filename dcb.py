import sys
import time
import pyvisa

# 詳細設定
SLEEP_TIME = 3  # 電圧を読みとる待機時間
IMIN = 0  # 初期電流値
IMAX = 0.2  # MAX電流値
DURATION = 0.02  # 間隔
DCA_ADDR = "TCPIP0::169.254.100.192::inst0::INSTR" #複数機器が接続されている場合は[]内の数字で指定

DCB_ADDR = "USB0::0x0B3E::0x1029::WD000275::INSTR"
rm = pyvisa.ResourceManager()

DCB = rm.open_resource(DCA_ADDR)
DCB.write('OUTP 1')  # type: ignore

# iList = []  # 電源Aの電流リスト
# x = IMIN
# while x <= IMAX:
#     iList.append(x)
#     x += DURATION
# x = IMAX
# while x > IMIN:
#     x -= DURATION
#     iList.append(x)

# for aOut in iList:
aOut = float(sys.argv[1])
print(f'aOut: {aOut}')

DCB.write(f'CURR {aOut}')  # type: ignore
# 指定時間待機
time.sleep(SLEEP_TIME)
DCB.write(f'MEAS:CURR?')
print(DCB.read())
DCB.write(f'MEAS:VOLT?')
print(DCB.read())
# print(f'cur: {curr}, volt: {volt}')
