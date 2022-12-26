import time
# import struct
import pyvisa

from time import sleep

from pymeasure.instruments.srs.sr830 import SR830

SLEEP_TIME = 0.001
IMIN = 10  # 初期電流値
IMAX = 100  # MAX電流値
DURATION = 1  # 間隔
LIA = SR830("GPIB0::8::INSTR")
DCA = ""
DCB_ADDR = "TCPIP0::169.254.205.92::inst0::INSTR"

LIA.sensitivity = 100e-6
rm = pyvisa.ResourceManager()
DCB = rm.open_resource(DCB_ADDR)
DCB.write('OUTP 1')

iList = []  # 電源Aの電流リスト
x = IMIN
while x <= IMAX:
    iList.append(x)
    x += DURATION
x = IMAX
while x > IMIN:
    x -= DURATION
    iList.append(x)

print(f"電源Aの電流値リスト: {iList}")
result = []

# 電源Aの出力
for aOut in iList:
    # 電源AにaOutを送る
    # 指定時間待機
    time.sleep(SLEEP_TIME)
    vb = 0.00
    vb1 = 0.00

    e = 0.00
    e1 = 0.00
    e2 = 0.00

    Kp = Ki = Kd = 0.2

    goal = 0.00
    lia_y = LIA.y

    # while abs(struct.unpack('<f', lia_y)[0]) > 0.001:
    while abs(lia_y) > 0.001:
        """
        M : 与える操作量
        M1 : 一つ前に与えた操作量
        goal : 目的値
        e : 偏差(目的値と現在値の差)
        e1 : 前回の偏差
        e2 : 前々回の偏差
        Kp : 比例制御（P制御)の比例定数
        Ki : 積分制御（I制御)の比例定数
        Kd : 微分制御（D制御)の比例定数
        """

        vb1 = vb
        e2 = e1
        e1 = e
        e = lia_y - goal

        vb = vb1 + Kp * (e - e1) + Ki * e + Kd * ((e - e1) - (e1 - e2))



        # VBの電圧の値を送る。電流は抵抗から求められる
        vb = 10 if vb > 10 else vb
        print(vb) # 一旦上のロジックが問題ないことを確認でき次第下を実行する
        # DCB.write(f'VOLT {vb}')
        sleep(0.01)
        #  LIAの値を読み取る(y軸の値)
        lia_y = LIA.y

    result.append([aOut, vb])

print(result)

# with open("result.csv") as f:
#   write(result)
