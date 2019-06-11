# Script for Loctrans route calculator ~ CRiSTi

from datetime import datetime
from datetime import timedelta

lines = ["L1", "L1A", "L1B", "L1C",
         "L2",
         "L3",
         "L4",
         "L5", "L5B"]

def is_time_equal_to(currentDatetime, hour, minutes):
    if currentDatetime.hour == hour and currentDatetime.minute == minutes:
        return True
    return False


# LX_dt[0] - time that the bus takes from station 0 to 1

l2_stops = ["GARA", "ARTILERIEI", "CAO", "STEAUA", "METALURGIC", "VALCEA", "LPS", "HELIOS", "PARC HOTEL", "CATEDRALA", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "VALCEA", "METALURGIC", "STEAUA", "KAUFLAND", "GARA"]
l3_stops = ["LPS", "OMV", "AXXA", "EROILOR", "EROILOR", "DECORA", "TMUCB", "GARA", "TUNARI", "FABRA", "LPS"]

def generate_L3_LV():
    l3_dt = [2, 3, 10, 0, 5, 1, 2, 2, 2, 3, 0]

    current_time = datetime(2008, 1, 1, 5, 50)
    file = open("L3_LV.out.csv", "w")

    for stop in l3_stops:
        file.write("{};".format(stop))
    file.write("\n")

    i = 0
    while i < 27:
        if is_time_equal_to(current_time, 11, 50):
            current_time += timedelta(minutes=20)
        if is_time_equal_to(current_time, 13, 40):
            current_time += timedelta(minutes=10)
        if is_time_equal_to(current_time, 15, 20):
            current_time += timedelta(minutes=10)
        if is_time_equal_to(current_time, 18, 30):
            current_time += timedelta(minutes=5)
        if is_time_equal_to(current_time, 19, 5):
            current_time += timedelta(minutes=10)
        for diff in l3_dt:
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))
            current_time += timedelta(minutes=diff)
        file.write("\n");
        i += 1

    file.close()

def generate_L3_SD():
    l3_dt = [2, 4, 9, 0, 6, 2, 2, 2, 2, 1, 0]

    current_time = datetime(2008, 1, 1, 7, 35)
    file = open("L3_SD.out.csv", "w")

    for stop in l3_stops:
        file.write("{};".format(stop))
    file.write("\n")

    i = 0
    while i < 4:
        if is_time_equal_to(current_time, 8, 5):
            current_time += timedelta(minutes=50)
        if is_time_equal_to(current_time, 9, 25):
            current_time += timedelta(minutes=50)
        if is_time_equal_to(current_time, 10, 45):
            current_time += timedelta(minutes=50)

        for diff in l3_dt:
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))
            current_time += timedelta(minutes=diff)
        file.write("\n");
        i += 1

    file.close()

def generate_L2_LV():
    l2_dt = [1, 2, 1, 1, 2, 2, 2, 2, 3, 9, 3, 1, 1, 2, 1, 1, 2, 2]

    current_time = datetime(2008, 1, 1, 5, 30)
    file = open("L2_LV.out.csv", "w")

    for stop in l2_stops:
        file.write("{};".format(stop))
    file.write("\n")

def main():
    print("Generating scripts...\n");

    generate_L2_LV()

    generate_L3_LV()
    generate_L3_SD()


    print("Scripts have been successfully generated!");

if __name__ == "__main__":
    main()