import RPi.GPIO as gpio

pin_st = 7 
pin_nd = 11 

gpio.setmode(gpio.BOARD)
gpio.setup(pin_st, gpio.OUT)
gpio.setup(pin_nd, gpio.OUT)

while 1:
	data = raw_input("Enter 2-bit's lenght -> ")
	if(len(data) == 2):
		gpio.output(pin_st,int(data[0]))
		gpio.output(pin_nd,int(data[1]))

