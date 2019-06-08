# Script for Loctrans route calculator ~ CRiSTi

from datetime import datetime
from datetime import timedelta
from datetime import time

lines = ["L1", "L1A", "L1B", "L1C",
         "L2",
         "L3",
         "L4",
         "L5", "L5B"]

# LX_dt[0] - time that the bus takes from station 0 to 1

# L3
l3_stops = ["LPS", "OMV", "AXXA", "EROILOR", "EROILOR", "DECORA", "TMUCB", "GARA", "TUNARI", "FABRA", "LPS"]
l3_dt = [2, 3, 10, 0, 5, 1, 2, 2, 2, 3, 0]

currentTime = datetime(2008, 1, 1, 5, 50)

file = open("L3 Routes.txt", "x")

for stop in l3_stops:
    file.write("{};".format(stop))
file.write("\n")

i = 0
while i < 26:
    for diff in l3_dt:
        file.write("{:02d}:{:02d};".format(currentTime.hour, currentTime.minute))
        currentTime = currentTime + timedelta(minutes=diff)
    file.write("\n");
    i += 1

file.close();