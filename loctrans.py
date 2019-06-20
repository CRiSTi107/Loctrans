# Script for Loctrans route calculator ~ CRiSTi

from datetime import datetime
from datetime import timedelta
from time import gmtime, strftime

lines = ["L1", "L1A", "L1B", "L1C",
         "L2",
         "L3",
         "L4",
         "L5", "L5B"]

def is_time_equal_to(current_datetime, hour, minutes):
    time_to_compare = datetime(2008, 1, 1, hour, minutes)
    if current_datetime.time() == time_to_compare.time():
        return True
    return False

def is_time_later_than(current_datetime, hour, minutes):
    time_to_compare = datetime(2008, 1, 1, hour, minutes)
    if current_datetime.time() >= time_to_compare.time():
        return True
    return False


# LX_dt[0] - time that the bus takes from station 0 to 1

l1_stops = ["ACH", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "UNION", "MINULESCU", "ARCULUI", "FINANTE", "VALCEA", "METALURGIC", "STEAUA", "STEAUA", "METALURGIC", "FABRA", "LPS", "HELIOS", "PARC HOTEL", "CATEDRALA", "ACH"]
l1a_stops = ["ACH", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "VALCEA", "METALURGIC", "STEAUA", "PIRELLI", "TMK", "TMK", "PIRELLI", "STEAUA", "METALURGIC", "FABRA", "LPS", "HELIOS", "PARC HOTEL", "CATEDRALA", "ACH"]
l1b_stops = ["ACH", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "UNION", "MINULESCU", "ARCULUI", "FINANTE", "VALCEA", "METALURGIC", "TUNARI", "ARTILERIEI", "CAO", "PRYSMIAN1", "PRYSMIAN2", "PRYSMIAN2", "PRYSMIAN1", "LIDL", "GARA", "TUNARI", "METALURGIC", "FABRA", "LPS", "HELIOS", "ACR", "ROMTELECOM", "FINANTE", "13 DECEMBRIE", "CATEDRALA", "ACH"]
l1c_stops = []
l2_stops = ["GARA", "ARTILERIEI", "CAO", "STEAUA", "METALURGIC", "VALCEA", "LPS", "HELIOS", "PARC HOTEL", "CATEDRALA", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "VALCEA", "METALURGIC", "STEAUA", "KAUFLAND", "GARA"]
l3_stops = ["LPS", "OMV", "AXXA", "EROILOR", "EROILOR", "DECORA", "TMUCB", "GARA", "TUNARI", "FABRA", "LPS"]

def generate_L1_LV():
    l1_dt = [3, 3, 1, 1, 2, 1, 1, 1, 2, 2, 1, 7, 1, 2, 2, 2, 2, 3, 3, 0]

    current_time = datetime(2008, 1, 1, 5, 35)
    file = open("L1_LV.out.csv", "w")

    for stop in l1_stops:
        file.write("{};".format(stop))
    file.write("\n")

    # Add a twisted route
    stop_count = 0
    stop_index = 0
    for stop in l1_stops:
        if(stop == "STEAUA"):
            stop_count += 1

        if(stop_count == 2):
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))
            current_time += timedelta(minutes=l1_dt[stop_index])
        else:
            file.write(";")

        stop_index += 1
    file.write("\n")
    current_time = datetime(2008, 1, 1, 6, 0)

    i = 0
    while i < 17:

        for diff in l1_dt:
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))
            if is_time_equal_to(current_time, 20, 30):
                break
            current_time += timedelta(minutes=diff)
        file.write("\n")

        if is_time_equal_to(current_time, 10, 00):
            current_time += timedelta(minutes=5)

        if is_time_equal_to(current_time, 11, 45):
            current_time += timedelta(minutes=35)

        if is_time_equal_to(current_time, 15, 40):
            current_time += timedelta(minutes=5)

        current_time += timedelta(minutes=10)

        i += 1

    file.close()

def generate_L1_SD():
    l1_dt = [4, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1, 7, 1, 1, 2, 2, 2, 3, 3, 0]

    current_time = datetime(2008, 1, 1, 7, 00)
    file = open("L1_SD.out.csv", "w")

    for stop in l1_stops:
        file.write("{};".format(stop))
    file.write("\n")

    i = 0
    while i < 6:

        for diff in l1_dt:
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))
            if is_time_equal_to(current_time, 20, 30):
                break
            current_time += timedelta(minutes=diff)
        file.write("\n")

        if is_time_equal_to(current_time, 12, 59):
            current_time -= timedelta(minutes=30)

        current_time += timedelta(minutes=41)

        i += 1

    file.close()

def generate_L1A_LV():
    l1a_dt = [3, 3, 1, 1, 2, 1, 2, 3, 2, 12, 3, 3, 1, 2, 2, 2, 2, 3, 3, 0]

    current_time = datetime(2008, 1, 1, 6, 0)
    file = open("L1A_LV.out.csv", "w")

    for stop in l1a_stops:
        file.write("{};".format(stop))
    file.write("\n")

    i = 0
    while i < 3:

        for diff in l1a_dt:
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))
            if(is_time_equal_to(current_time, 7, 38)):
                break
            current_time += timedelta(minutes=diff)
        file.write("\n")

        if (is_time_equal_to(current_time, 7, 38)):
            current_time += timedelta(minutes=22+60*6-29)

        current_time += timedelta(minutes=29)

        i += 1

    file.close()

def generate_L1A_SD():
    l1a_dt = [3, 3, 1, 1, 3, 1, 1, 4, 2, 12, 3, 3, 1, 2, 2, 2, 2, 3, 3, 0]

    current_time = datetime(2008, 1, 1, 5, 50)
    file = open("L1A_SD.out.csv", "w")

    for stop in l1a_stops:
        file.write("{};".format(stop))
    file.write("\n")

    i = 0
    while i < 1:

        for diff in l1a_dt:
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))
            if (is_time_later_than(current_time, 6, 9)):
                break
            current_time += timedelta(minutes=diff)
        file.write("\n")

        i += 1

    file.close()

def generate_L1B_LV():
    l1b_dt = [3, 3, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 3, 3, 52, 3, 3, 4, 1, 5, 2, 2, 2, 2, 1, 2, 2, 6, 3, 0]

    current_time = datetime(2008, 1, 1, 6, 0)
    file = open("L1B_LV.out.csv", "w")

    for stop in l1b_stops:
        file.write("{};".format(stop))
    file.write("\n")

    i = 0
    while i < 3:

        for diff in l1b_dt:
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))

            if(is_time_equal_to(current_time, 15, 31)):
                current_time -= timedelta(minutes=1)

            if(is_time_equal_to(current_time, 15, 48)):
                current_time -= timedelta(minutes=1)

            if(is_time_equal_to(current_time, 23, 26)):
                current_time -= timedelta(minutes=2)

            if(is_time_equal_to(current_time, 23, 29)):
                current_time -= timedelta(minutes=2)

            if(is_time_equal_to(current_time, 23, 44)):
                current_time -= timedelta(minutes=1)

            current_time += timedelta(minutes=diff)

            if(is_time_equal_to(current_time, 23, 40)):
                current_time += timedelta(minutes=1)

            if(is_time_equal_to(current_time, 23, 51)):
                current_time += timedelta(minutes=1)
        file.write("\n")

        if(is_time_equal_to(current_time, 7, 58)):
            current_time += timedelta(minutes=6*60)

        if(is_time_equal_to(current_time, 15, 56)):
            current_time += timedelta(minutes=2+60*6)

        current_time += timedelta(minutes=2)

        i += 1

    file.close()

def generate_L2_LV():
    l2_dt = [1, 2, 1, 1, 2, 2, 2, 2, 3, 9, 3, 1, 1, 2, 1, 1, 2, 2, 0]

    current_time = datetime(2008, 1, 1, 5, 30)
    file = open("L2_LV.out.csv", "w")

    for stop in l2_stops:
        file.write("{};".format(stop))
    file.write("\n")

    i = 0
    while i < 29:
        gap = False

        for diff in l2_dt:
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))
            if is_time_equal_to(current_time, 13, 51):
                break
            current_time += timedelta(minutes=diff)
        file.write("\n")

        if is_time_equal_to(current_time, 15, 28):
            current_time -= timedelta(minutes=23)
            gap = True

        if is_time_equal_to(current_time, 14, 53):
            current_time -= timedelta(minutes=3)
            gap = True

        if is_time_equal_to(current_time, 14, 38):
            current_time -= timedelta(minutes=23)
            gap = True

        if is_time_equal_to(current_time, 13, 51):
            current_time += timedelta(minutes=9)
            gap = True

        if is_time_equal_to(current_time, 10, 43):
            current_time += timedelta(minutes=22)
            gap = True

        if not gap:
            if is_time_later_than(current_time, 15, 43):
                current_time += timedelta(minutes=12)
            else:
                current_time -= timedelta(minutes=13)

        i += 1

    file.close()

def generate_L2_SD():
    l2_dt = [1, 2, 1, 1, 2, 2, 2, 2, 3, 9, 3, 1, 1, 2, 1, 1, 2, 2, 0]

    current_time = datetime(2008, 1, 1, 5, 30)
    file = open("L2_SD.out.csv", "w")

    for stop in l2_stops:
        file.write("{};".format(stop))
    file.write("\n")

    i = 0
    while i < 16:
        gap = False

        for diff in l2_dt:
            file.write("{:02d}:{:02d};".format(current_time.hour, current_time.minute))
            current_time += timedelta(minutes=diff)
        file.write("\n")

        if is_time_equal_to(current_time, 6, 8):
            current_time += timedelta(minutes=62)
            gap = True

        if is_time_equal_to(current_time, 10, 18):
            current_time += timedelta(minutes=47)
            gap = True

        if is_time_equal_to(current_time, 14, 13):
            current_time += timedelta(minutes=52)
            gap = True

        if not gap:
            current_time += timedelta(minutes=12)

        i += 1

    file.close()

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
        file.write("\n")
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
        file.write("\n")
        i += 1

    file.close()

def main():
    print("[{}] Generating bus stops...\n".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))

    generate_L1_LV()
    generate_L1_SD()

    generate_L1A_LV()
    generate_L1A_SD()

    generate_L1B_LV()

    generate_L2_LV()
    generate_L2_SD()

    generate_L3_LV()
    generate_L3_SD()

    print("[{}] Bus stops have been successfully generated!\n".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())))


if __name__ == "__main__":
    main()