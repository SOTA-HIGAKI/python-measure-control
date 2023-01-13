import pyvisa
from time import sleep

rm = pyvisa.ResourceManager() #インスタンス生成
# ls_visa = rm.list_resources() #PCに接続された機器のVISAリソース名取得
# print(ls_visa)
DCB = "TCPIP0::169.254.205.92::inst0::INSTR" #複数機器が接続されている場合は[]内の数字で指定
DCA = "TCPIP0::169.254.100.192::inst0::INSTR" #複数機器が接続されている場合は[]内の数字で指定
inst = rm.open_resource(DC2) #接続

inst.write('*IDN?') #指令の送信、*IDN?は多くの機器に設定されている機器情報を聞く指令
print(inst.read()) #指令に対しての返答をプリント
inst.write('OUTP 1')
# inst.write('VOLT 1.5')
sleep(3)
inst.write('MEAS:VOLT?')
print(inst.read())