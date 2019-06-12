# Main for Flight Calculator
from tkinter import *

from flight_calc_functions import *

###############################################################################
#                           Test section
###############################################################################

# tests of the functions

print('=' * 50)

print('*** Check rate time & distance formulas ***\n')

###############################################################################

# Set up variables:

rate = 65
time = 2
distance = 130

print('Distance check:')
print('rate = 65 knots, time = 2 hrs. Should be 65 * 2 = 130 nautical miles')
print('distance_(65, 2): {}'.format(distance_(rate, time)))

print('=' * 50)

print('Rate check:')
print('Distance = 130 nautical miles, time = 2 hrs. Should be 130 / 2 = 65 knots')
print('rate_(distance_, time_): {}'.format(rate_(distance, time)))

print('=' * 50)

print('Time check:')
print('Distance = 130 nautical miles, rate = 65 kts. Should be 130 / 65 = 2 hours')

print('time_(distance_, time_): {}'.format(time_(distance, rate)))

print('=' * 50)

###############################################################################

print('Conversions - Statute and Nautical Miles')

print('**** NEED TO ADD FUNCTION CALLS TO CONFIRM CONVERSIONS ****')
quick_miles()

###############################################################################

print('=' * 50)

print('Conversions - Feet and Meters')

quick_feet_meters()

feet_ = 3
meters_ = 2

print('Convert feet to meters where feet = 3')
print('feet = 3. Should be 0.9144 meters')
print('3 feet = {} meters'.format(feet_to_meters(feet_)))

print('Convert meters to feet where meteres = 2')
print('meters = 2. Should be 6.56168 feet')
print('2 meters = {} feet'.format(meter_to_feet(meters_)))

print('=' * 50)

###############################################################################

###############################################################################
#                           END Test section
###############################################################################





print('****  END  ****')
