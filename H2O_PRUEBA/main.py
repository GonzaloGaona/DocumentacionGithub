from machine import Pin
import sys
import time
inpt=Pin(4, Pin.IN)
tot=0.0
contador=0
lit=0
puls=0

def my_callback(channel):
	global contador, tot, lit
	contador=contador+1
	tot=contador
	lit=contador
	import time
	import sys
	sys.stdout.write('%d' % contador, )
	sys.stdout.flush()
	i=l
	while i<=len (str(contador)):
		sys.stdout.write('\b')
		i=i+1;
inpt.irq(trigger=Pin.IRQ_RISING, handler=my_callback)
while True:
	print((contador*1.0)/398)
	print(contador)
	print(tot)
	time.sleep(2)
