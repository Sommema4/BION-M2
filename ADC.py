# spitest.py
# A brief demonstration of the Raspberry Pi SPI interface, using the Sparkfun
# Pi Wedge breakout board and a SparkFun Serial 7 Segment display:
# https://www.sparkfun.com/products/11629

import time
import spidev
import optparse

parser = optparse.OptionParser()
parser.add_option('-f', '--file', dest='file', help='Name of the spectrum .SP2 file')
parser.add_option('-b', '--bins', dest='bins', help='Write number of bins per decade', type=int)
(options, args) = parser.parse_args()

reset = 0
readout = 0
lvds_swing = 350
lvds_swing_en = 0
high_perf_1 = 0
high_perf_2 = 0
gain = 0.0
pattern = 'normal'
lvds_clk_strength = 100
lvds_data_strength = 100
data_format = '2s_complement'
lvds_cmos = 'lvds'
cmos_clk_strength = 0
clk_rise_en = 0
clk_rise_pos = 0
clk_fall_en = 0
clk_fall_pos = 0
low_latency_dis = 0
standby = 0
power_down_global = 0
power_down_output = 0

lvds_swing_dict = {350:0B000000, 410:0B011011, 465:0B110010, 570:0B010100, 200:0B111110, 125:0B001111}
high_perf_1_dict = {0:0B00, 1:0B11}
gain_dict = {0.0:0B0000, 0.5:0B0001, 1.0:0B0010, 1.5:0B0011, 2.0:0B0100, 2.5:0B0101, 3.0:0B0110, 3.5:0B0111, 4.0:0B1000, 4.5:0B1001, 5.0:0B1010, 5.5:0B1011, 6.0:0B1100}
pattern_dict = {'normal':0B000, 'zeros':0B001, 'ones':0B010, 'toggle':0B011, 'ramp':0B100, 'custom':0B101}
lvds_clk_strength_dict = {100:0B0, 50:0B1}
lvds_data_strength_dict = {100:0B0, 50:0B1}
data_format_dict = {'dfs_pin':0B00, '2s_complement':0B10, 'offset_binary':0B11} 
lvds_cmos_dict = {'dfs_pin':0B00, 'lvds':0B01, 'cmos':0B11}
cmos_clk_strength_dict = {'maximum':0B00, 'medium':0B01, 'low':0B10, 'very_low':0B11} 
clk_rise_pos_dict = 1 
clk_fall_pos_dict = 1

# We only have SPI bus 0 available to us on the Pi
bus = 0

#Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 1

# Enable SPI
spi = spidev.SpiDev()

# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

spi.xfer2(msg)
