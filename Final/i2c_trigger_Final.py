from smbus2 import SMBus
import time
#/sys/bus/i2c/devices/i2c-1/bus_clk_rate   - can change clock rate at this file if need be

i2c_channel = 1
i2c_address = 0x0a
byteLength = 18
delay = 0.25

def Thermal_Values():

    #read a block of data
    with SMBus(i2c_channel) as bus:
        #read a block of bytes from address 0x0a, offset 0
        block = bus.read_i2c_block_data(i2c_address, 0, byteLength)
        temps = []
        for i in range(2,17,2):
            if block[i+1] == 2:
                #time.sleep(delay)
                return True
            elif block[i] >= 245 and block[i+1] == 1:
                #time.sleep(delay)
                return True
    #time.sleep(delay)
    return False

