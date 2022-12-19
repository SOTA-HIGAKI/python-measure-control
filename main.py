import time

from pymeasure.instruments.srs.sr830 import SR830

SLEEP_TIME = 0.001
IMIN = 10  # 初期電流値
IMAX = 100  # MAX電流値
DURATION = 1  # 間隔
LIA = SR830("GPIB::4")

iList = []  # 電源Aの電流リスト
x = IMIN
while x <= IMAX:
    iList.append(x)
    x += DURATION
x = IMAX
while x > IMIN:
    x -= DURATION
    iList.append(x)

print(iList)
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
    lia = 10  # 読みとる

    while abs(lia) > 0.001:
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
        e = lia - goal

        vb = vb1 + Kp * (e - e1) + Ki * e + Kd * ((e - e1) - (e1 - e2))

        # VBの電圧の値を送る。電流は抵抗から求められる
        # send_vb(vb if vb < 10 else 10)
        # SLEEP_TIME
        #  LIAの値を読み取る(y軸の値)
        lia = 10

    result.append([aOut, vb])

print(result)

# with open("result.csv") as f:
#   write(result)
