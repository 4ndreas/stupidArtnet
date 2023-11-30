from lib.StupidArtnet import StupidArtnet
import time
import random

# # THESE ARE MOST LIKELY THE VALUES YOU WILL BE NEEDING
# target_ip = '192.168.2.80'		# typically in 2.x or 10.x range
# universe = 65					# see docs
# packet_size = 100				# it is not necessary to send whole universe

# # CREATING A STUPID ARTNET OBJECT
# # SETUP NEEDS A FEW ELEMENTS
# # TARGET_IP   = DEFAULT 127.0.0.1
# # UNIVERSE    = DEFAULT 0
# # PACKET_SIZE = DEFAULT 512
# # FRAME_RATE  = DEFAULT 30
# a = StupidArtnet(target_ip, universe, packet_size,0)

# # CHECK INIT
# print(a)


# a.set_single_value(1, 42)			# magic

# # # #  set color
# a.set_single_value(2, 1)			# cmd
# a.set_single_value(3, 2)			# channel 
# a.set_single_value(4, 1)			# offset
# a.set_single_value(5, 0)			# color code	// default = 4(GRB) 

# # # ... AND SEND
# a.show()							# send data


def setOutputColor(target_ip, channel, offset, color):
    universe = 66					# see docs
    packet_size = 100
    a = StupidArtnet(target_ip, universe, packet_size,0)
    print(a)
    print('channel:',channel, 'offset:', offset, 'color:', color)
    a.set_single_value(1, 42)			# magic
    # # #  set color
    a.set_single_value(2, 1)			# cmd
    a.set_single_value(3, channel)		# channel 
    a.set_single_value(4, offset)		# offset
    a.set_single_value(5, color)		# color code	// default = 4(GRB) 
    a.show()
    time.sleep(1)	

def saveConfig(target_ip):
    universe = 66
    packet_size = 100
    a = StupidArtnet(target_ip, universe, packet_size,0)
    print(a)
    a.set_single_value(1, 42)	# magic
    a.set_single_value(2, 2)    # save config
    a.show()

def readConfig(target_ip):
    universe = 66
    packet_size = 100
    a = StupidArtnet(target_ip, universe, packet_size,0)
    print(a)
    a.set_single_value(1, 42)	# magic
    a.set_single_value(2, 4)    # read config
    a.show()

def resetDevice(target_ip):
    universe = 66
    packet_size = 100
    a = StupidArtnet(target_ip, universe, packet_size,0)
    print(a)
    a.set_single_value(1, 42)	# magic
    a.set_single_value(2, 66)    # read config
    a.show()

def offsetLEDs(target_ip, en):
    universe = 66
    packet_size = 100
    a = StupidArtnet(target_ip, universe, packet_size,0)
    print(a)
    a.set_single_value(1, 42)	# magic
    a.set_single_value(2, 5)    # enable/disable status LEDs
    a.set_single_value(3, en)   # 0=off; 1 == on
    a.show()


def defaultConfig(target_ip):
    universe = 66
    packet_size = 100
    a = StupidArtnet(target_ip, universe, packet_size,0)
    print(a)
    a.set_single_value(1, 42)	# magic
    a.set_single_value(2, 3)    # default config
    a.show()


def setOutputColorPPBox(target_ip, magic, color):
    universe = 254					# see docs
    packet_size = 30
    a = StupidArtnet(target_ip, universe, packet_size,0)
    print(a)

    a.set_single_value(1, magic)			# magic
    a.set_single_value(2, 1)			    # cmd
    a.set_single_value(3, len(color))		# num leds

    for i in range(0, len(color)):
        a.set_single_value(4+i, color[i])	# color code	// default = 4(GRB) 
    
    a.show()


def saveConfigPPBox(target_ip, magic):
    universe = 254					# see docs
    packet_size = 30
    a = StupidArtnet(target_ip, universe, packet_size,0)
    print(a)
    a.set_single_value(1, magic)			# magic
    # # #  set color
    a.set_single_value(2, 3)			    # cmd
    a.show()






# for i in range (12,16):
#     setOutputColor(target_ip, i, 0, 4)
#     time.sleep(1)

# saveConfig(target_ip)

# setOutputColor(target_ip, 0, 1, 4)
# setOutputColor(target_ip, 1, 0, 4)
# setOutputColor(target_ip, 2, 0, 0)
# setOutputColor(target_ip, 3, 0, 0)

# setOutputColor(target_ip, 5, 0, 0)
# setOutputColor(target_ip, 6, 0, 0)
# setOutputColor(target_ip, 7, 0, 0)
# setOutputColor(target_ip, 8, 0, 0)
# setOutputColor(target_ip, 9, 0, 0)
# setOutputColor(target_ip, 10, 0, 0)
# setOutputColor(target_ip, 11, 0, 0)
# setOutputColor(target_ip, 12, 0, 0)
# setOutputColor(target_ip, 13, 0, 0)
# setOutputColor(target_ip, 14, 0, 0)
# setOutputColor(target_ip, 15, 0, 0)


# # 0 = RGB // maiskoblen
# # 1 = GRB
# # 2 = BGR
# # 3 = RBG
# # 4 = GBR // default for strips
# # 5 = BRG

# target_ip= '192.168.2.80'
# setOutputColor(target_ip, 0, 0, 4)
# saveConfig(target_ip)
# setOutputColor(target_ip, channel, offset, color):
# target_ip= '10.39.0.20'
target_ip= '10.39.0.21'


# for i in range (0,15):
#     setOutputColor(target_ip, i, 1, 4)
#     time.sleep(0.1)

# for i in range (0,3):
#     setOutputColor(target_ip, i, 1, 4)
#     time.sleep(0.1)

# for i in range (4,15):
#     setOutputColor(target_ip, i, 0, 4)
#     time.sleep(0.1)

# for i in range (0,15):
#     setOutputColor(target_ip, i, 1, 0)
#     time.sleep(0.1)

# setOutputColor(target_ip, 0, 1, 4)
# setOutputColor(target_ip, 1, 1, 4)
# setOutputColor(target_ip, 2, 1, 4)
# setOutputColor(target_ip, 3, 1, 4)

# setOutputColor(target_ip, 4, 1, 4)
# setOutputColor(target_ip, 5, 1, 4)
# setOutputColor(target_ip, 6, 1, 4)
# setOutputColor(target_ip, 7, 1, 4)

# setOutputColor(target_ip, 2, 1, 0)
# setOutputColor(target_ip, 3, 1, 0)

offsetLEDs(target_ip,0)
saveConfig(target_ip)
time.sleep(4) # Sleep for 3 second


# readConfig(target_ip)

# resetDevice(target_ip)

# offsetLEDs(target_ip, 1)
