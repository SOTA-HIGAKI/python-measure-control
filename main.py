import time
import pyvisa

from time import sleep

from pymeasure.instruments.srs.sr830 import SR830

# 詳細設定
SLEEP_TIME = 1  # 電圧を読みとる待機時間
IMIN = 0  # 初期電流値
IMAX = 1  # MAX電流値
DURATION = 0.01  # 間隔

# LIAの設定
LIA = SR830("GPIB0::8::INSTR")
LIA.sensitivity = 100e-6
LIA.set_scaling('Y', 3.0)
LIA.reference_source = 'Internal'
LIA.reference_source_trigger = 'SINE'
LIA.frequency = 200

# DC電源の設定
DCA_ADDR = "TCPIP0::169.254.100.192::inst0::INSTR"
# DCB_ADDR = "TCPIP0::169.254.205.92::inst0::INSTR"
DCB_ADDR = "USB0::0x0B3E::0x1029::WD000275::INSTR"
rm = pyvisa.ResourceManager()
DCA = rm.open_resource(DCA_ADDR)
DCB = rm.open_resource(DCB_ADDR)
DCA.write('OUTP 1')  # type: ignore
DCB.write('OUTP 1')  # type: ignore

iList = []  # 電源Aの電流リスト
x = IMIN
while x <= IMAX:
    iList.append(x)
    x += DURATION
x = IMAX
while x > IMIN:
    x -= DURATION
    iList.append(x)

result = []
# 設定の反映が終わるまで待つ！
time.sleep(10)
# 電源Aの出力
for aOut in iList:
    DCA.write(f'CURR {aOut}')  # type: ignore
    # 指定時間待機
    time.sleep(SLEEP_TIME)
    vb = 0.00
    vb1 = 0.00

    e = 0.00
    e1 = 0.00
    e2 = 0.00

    # ここをじどうかできればいいのでは？
    Kp = Ki = Kd = 0.2

    goal = 0.00
    lia_y = LIA.y

    while abs(lia_y) > 0.000005:  # type: ignore
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
        e = lia_y - goal  # type: ignore

        vb = vb1 + Kp * (e - e1) + Ki * e + Kd * ((e - e1) - (e1 - e2))

        # 電圧降下できるなにかをさがす？

        # VBの電圧の値を送る。電流は抵抗から求められる
        vb = 5 if vb > 5 else vb
        print(vb) # 一旦上のロジックが問題ないことを確認でき次第下を実行する
        DCB.write(f'VOLT {vb}')
        sleep(0.01)
        #  LIAの値を読み取る(y軸の値)
        lia_y = LIA.y

    result.append([aOut, vb])
    print([aOut, vb], end="")

print(result)

# with open("result.csv") as f:
#   write(result)
