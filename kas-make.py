import sys

if len(sys.argv)<3:
	print("Usage: {} <new-kas-image> <kernel>".format(sys.argv[0]))
	exit(1)

kas=open(sys.argv[1], "wb")
kernel=open(sys.argv[2], "rb")

kas.write(bytes.fromhex("894B4153")) #sign
kas.write(bytes([0]*16)) #kernel version
kas.write(b" "*128) #kernel cmdline
kas.write(bytes([0]*108)) # header padding
kernel_data=kernel.read()
kernel.close()
kernel_data+=b""*((32*1024*1024)-len(kernel_data))
kas.write(kernel_data)
kas.close()
