# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

speed_of_light = 299792458.0        # meters per second 
cycles_per_second = 2700000000.0    # 2.7 GHz
cycle_distance_in_meter = speed_of_light / cycles_per_second
cycle_distance_in_centimeter = cycle_distance_in_meter * 100

print cycle_distance_in_meter
print cycle_distance_in_centimeter