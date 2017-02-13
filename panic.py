#Panic For Pinos by Maxim Pinigin (c) 2016-2017

import time

def panic(reason):
	print("")
	print("Pinos Panic: " + reason)
	time.sleep(10);
	exit()
