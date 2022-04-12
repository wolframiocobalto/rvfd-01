from machine import ADC
from math import log
from time import sleep
termistor = ADC(28)

while True: 
  lectura = termistor.read_u16()
  VR = (lectura * 3.3 )/ 65535 
  print("TENSION EN R:{}". format(VR))
  R = 10000/((3.3/VR)-1)
  print("RESISTENCIA :{}". format(R))
  T = (1/((log(R/10000)/3950) + (1/298))) - 273
  print("TEMPERATURA:{}". format(T))
  sleep(.5)