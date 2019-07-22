#GTFS-compliant route and trip generator

from datetime import time
from datetime import datetime
from datetime import timedelta

routes = ["1T", "1R", "1AT", "1AR", "1BT", "1BR", "1CT", "1CR",
          "2T", "2R", "3T", "3R", "4T", "4R", "5T", "5R", "5BT", "5BR"]

#Add time delta to time
def addTime(tm, td):
    fulldate = datetime(1000, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + td
    return fulldate.time()
	
#Minutes to time delta
def mnt(mins):
	return timedelta(minutes=mins)
		 
def generate_1T_LV():
	stops = ["ACH1", "CAT1", "SPI", "ACR", "RTC", "UNI", "MIN", "ARC", "FIN1", "VAL", "MET1", "STE1"]

	time_start = [time( 6, 0), time( 6,50), time(7,40), time( 8,30), time( 9,20), time(10,15), 
	                 time(11, 5), time(12,30), time(13,20), time(14,10), time(15, 0), time(15,55),
					 time(16,45), time(17,35), time(18,25), time(19,15), time(20, 5)]
	time_diff = [mnt(0), mnt(3), mnt(3), mnt(1), mnt(1), mnt(2), mnt(1), mnt(1), mnt(1), mnt(2), mnt(2), mnt(1)]
	
	trips_file = open("trips.txt", "a")
	stop_times = open("stop_times.txt", "a")
	
	nr_trips = len(time_start)
	for trip_number in range(nr_trips):
		trip_id = "1TLV" + str(trip_number)
		trips_file.write("1T,LV," + trip_id + ",1\n")

		cr_stop = time_start[trip_number]
		for stop_sequence in range(len(time_diff)):
			cr_stop = addTime(cr_stop, time_diff[stop_sequence])
			cr_stop_str = cr_stop.strftime("%H:%M")
			stop_times.write(trip_id + "," + cr_stop_str + "," + cr_stop_str + "," + stops[stop_sequence] + "," + str(stop_sequence) + "\n")

		
def main():
  generate_1T_LV()
  
if __name__== "__main__":
  main()
