# Flight Calculator Functions
#
# 2019-06-02
#
# This file contains the functions that will be used by the flight calculator
# GUI and possibly a web version

###############################################################################
#
#                           CONSTANTS
#
###############################################################################

# Statute Miles, Nautical Miles

statute_mile_in_nautical_mile = 1.1508

nautical_mile_in_statute_mile = 1 / statute_mile_in_nautical_mile

# Feet, meters

feet_in_a_meter = 3.28084

meter_in_a_foot = 1 / feet_in_a_meter  # 0.3048 meter in a foot


###############################################################################
#
#                           TIME SPEED DISTANCE
#
###############################################################################

# Base Formula : Distance = Rate * Time


def distance_(rate_, time_):
    return float(rate_) * float(time_)


def rate_(distance_, time_):
    return float(distance_) / float(time_)


def time_(distance_, rate_):
    return float(distance_) / float(rate_)


###############################################################################
#
#                           CONVERSIONS
#
###############################################################################

###############################################################################
#
#                           Statute, Nautical Miles & Kilometers
#
###############################################################################

def quick_miles():
    print('statute miles in a nautical mile:', statute_mile_in_nautical_mile)
    print('nautical mile in a statute: ', nautical_mile_in_statute_mile)

###############################################################################
#
#                           Feet & Meters
#
###############################################################################


def quick_feet_meters():
    print('Feet in a meter:', feet_in_a_meter)
    print('Meter in a foot: ', meter_in_a_foot)


def feet_to_meters(feet):
    return feet * meter_in_a_foot


def meter_to_feet(meters):
    return meters * feet_in_a_meter


###############################################################################

###############################################################################

###############################################################################

###############################################################################

###############################################################################
