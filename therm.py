import math

def beta(rt2, rt1, t2, t1):
	return math.log(rt2/rt1, math.e)/(1/t2 - 1/t1)

def Rt(temp0, rtemp0, beta, TempX):
	return rtemp0 * math.e**(beta*(1/TempX - 1/temp0))

def CtoK(TC):
	return TC + 273.15

def RG_A(gain):
	return 49400/(gain-1)

def Vdiv(Vin, r1, r2):
	return Vin*(r1/(r1+r2))

def Vdrop(V2, V1):
	return V2-V1

def Wheat(Vin, R1, R3, R2, Rvar):
	return Vdrop( Vdiv(Vin, R2, Rvar), Vdiv(Vin, R1, R3) )

def AmpInstr(gain, Vnoinv, Vinv):
	return gain*(Vnoinv-Vinv)

def main():

	Vp, Vm, = 12, -12
	Vgrnd = -Vp-Vm

	tmp0 = CtoK(0)
	tmp100 = CtoK(100)
	rtmp0 = 32000
	rtmp100 = 750
	b = beta(rtmp100, rtmp0, tmp100, tmp0)
	print(f'beta={b}\n')

	temps = [0, 20, 30, 31, 50, 51, 80, 81, 100]
	temp_to_res = {}
	for i in temps:
		temp_to_res[i] = Rt(tmp0, rtmp0, b, CtoK(i))
		print(f'R({i}°C) = {temp_to_res[i]}')

	print('\nWheatstone:')
	wheat_vs = {}
	for i in temp_to_res:
		wheat_vs[i] = Wheat(12, 10690, 1000, 342180, temp_to_res[i])
		print(f'V({i}°C) = {wheat_vs[i]}')

	gain = 10
	print(f'\nAmplificación con A={gain} RG={RG_A(gain)}')
	transfer_amp = {}
	for i in wheat_vs:
		transfer_amp[i] = AmpInstr(gain, wheat_vs[i], Vgrnd)
		print(f'V({i}°C) = {transfer_amp[i]}')


if __name__ == '__main__':
	main()

