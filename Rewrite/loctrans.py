# LOCTRANS schedule generator ~ CRiSTi, xizz3l

from datetime import time
from datetime import datetime
from datetime import timedelta

# dt[i] - time it takes to reach station i from station i-1
# if first stop (dt[0]), then arrival time
#
# tr[i] - time difference between trip starting times
# if first trip(tr[0]), then arrival time

#Add minutes to time
def add_time(tm, min):
    fulldate = datetime(1000, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + timedelta(minutes=min)
    return fulldate.time()

# Generic writer for all lines
def write_line(dt, tr, stops, start_time, file):
	for stop_nr in range( len(stops) ):
		file.write(stops[stop_nr])
		if stop_nr < len(stops)-1:
			file.write(",")
		else:
			file.write("\n")
		
	for trip_nr in range( len(tr) ):
		start_time = add_time(start_time, tr[trip_nr])
		cr_time = start_time
		for stop_nr in range( len(stops) ):
			cr_time = add_time(cr_time, dt[stop_nr])
			file.write(cr_time.strftime("%H:%M"))
			if stop_nr < len(stops)-1:
				file.write(",")
			else:
				file.write("\n")

def generate_L1_LV_T():
	dt = [0, 3, 3, 1, 1, 2, 1, 1, 1, 2, 2, 1]
	tr = [0, 50, 50, 50, 50, 55, 50, 85, 50, 50, 50, 55, 50, 50, 50, 50, 50]
	stops = ["ACH", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "UNION", "MINULESCU", "ARCULUI", "FINANTE", "VALCEA", "METALURGIC", "STEAUA"]
	
	file = open("l1_lv_t.csv", "w")
	start_time = time(6)
	write_line(dt, tr, stops, start_time, file)
	file.close()
	
def generate_L1_LV_R():
	dt = [0, 1, 2, 2, 2, 2, 3, 3]
	tr = [0, 50, 50, 50, 50, 50, 55, 50, 85, 50, 50, 50, 55, 50, 50, 50, 50]
	stops = ["STEAUA", "METALURGIC", "FABRA", "LPS", "HELIOS", "PARC HOTEL", "CATEDRALA", "ACH"]
	
	file = open("l1_lv_r.csv", "w")
	start_time = time(5, 35)
	write_line(dt, tr, stops, start_time, file)
	file.close()
	
def generate_L1_SD_T():
	dt = [0, 4, 2, 1, 1, 1, 2, 2, 1, 2, 1, 1]
	tr = [0, 80, 80, 80, 80, 50]
	stops = ["ACH", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "UNION", "MINULESCU", "ARCULUI", "FINANTE", "VALCEA", "METALURGIC", "STEAUA"]
	
	file = open("l1_sd_t.csv", "w")
	start_time = time(7)
	write_line(dt, tr, stops, start_time, file)
	file.close()

def generate_L1_SD_R():
	dt = [0, 1, 1, 2, 2, 2, 3, 3]
	tr = [0, 80, 80, 80, 80, 50]
	stops = ["STEAUA", "METALURGIC", "FABRA", "LPS", "HELIOS", "PARC HOTEL", "CATEDRALA", "ACH"]

	file = open("l1_sd_r.csv", "w")
	start_time = time(7, 25)
	write_line(dt, tr, stops, start_time, file)
	file.close()

def generate_L1A_LV_T():
	dt = [0, 3, 3, 1, 1, 2, 1, 2, 3, 2]
	tr = [0, 80, 400]
	stops = ["ACH", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "VALCEA", "METALURGIC", "STEAUA", "PIRELLI", "TMK"]

	file = open("l1a_lv_t.csv", "w")
	start_time = time(6)
	write_line(dt, tr, stops, start_time, file)
	file.close()

def generate_L1A_LV_R():
	dt = [0, 3, 3, 1, 2, 2, 2, 2, 3, 3]
	tr = [0, 530]
	stops = ["TMK", "PIRELLI", "STEAUA", "METALURGIC", "FABRA", "LPS", "HELIOS", "PARC HOTEL", "CATEDRALA", "ACH"]

	file = open("l1a_lv_r.csv", "w")
	start_time = time(6, 30)
	write_line(dt, tr, stops, start_time, file)
	file.close()

def generate_L1A_SD_T():
	dt = [0, 3, 2, 2, 1, 3, 1, 1, 4, 2]
	tr = [0]
	stops = ["ACH", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "VALCEA", "METALURGIC", "STEAUA", "PIRELLI", "TMK"]

	file = open("l1a_sd_t.csv", "w")
	start_time = time(5, 50)
	write_line(dt, tr, stops, start_time, file)
	file.close()

def generate_L1B_LV_T():
	dt = [0, 3, 3, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 3, 3]
	tr = [0, 480, 480]
	stops = ["ACH", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "UNION", "MINULESCU", "ARCULUI", "FINANTE", "VALCEA", "METALURGIC", "TUNARI", "ARTILERIEI", "CAO", "PRYSMIAN1", "PRYSMIAN2"]
	
	file = open("l1b_lv_t.csv", "w")
	start_time = time(6)
	write_line(dt, tr, stops, start_time, file)
	file.close()
	
def generate_L1B_LV_R():
	dt = [0, 3, 3, 2, 1, 3, 2, 2, 2, 2, 1, 2, 2, 6, 3]
	tr = [0, 480, 480]
	stops = ["PRYSMIAN2", "PRYSMIAN1", "LIDL", "GARA", "TUNARI", "METALURGIC", "FABRA", "LPS", "HELIOS", "ACR", "ROMTELECOM", "FINANTE", "13 DECEMBRIE", "CATEDRALA", "ACH"]
	
	file = open("l1b_lv_r.csv", "w")
	start_time = time(7, 20)
	write_line(dt, tr, stops, start_time, file)
	file.close()

def generate_L1B_SD_T():
	dt = [0, 3, 3, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 3, 5]
	tr = [0, 730, 240]
	stops = ["ACH", "CATEDRALA", "SPITAL", "ACR", "ROMTELECOM", "UNION", "MINULESCU", "ARCULUI", "FINANTE", "VALCEA", "METALURGIC", "TUNARI", "ARTILERIEI", "CAO", "PRYSMIAN1", "PRYSMIAN2"]
	
	file = open("l1b_sd_t.csv", "w")
	start_time = time(5, 50)
	write_line(dt, tr, stops, start_time, file)
	file.close()
	
def generate_L1B_SD_R():
	dt = [0, 5, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 3, 2, 3]
	tr = [0, 720, 240]
	stops = ["PRYSMIAN2", "PRYSMIAN1", "LIDL", "GARA", "TUNARI", "METALURGIC", "FABRA", "LPS", "HELIOS", "ACR", "ROMTELECOM", "FINANTE", "13 DECEMBRIE", "CATEDRALA", "ACH"]
	
	file = open("l1b_sd_r.csv", "w")
	start_time = time(7, 20)
	write_line(dt, tr, stops, start_time, file)
	file.close()

#    TEMPLATE
#def generate_Lx_WW_Y():	
#	dt = []
#	tr = []
#	stops = []
#	
#	file = open("lx_ww_y.csv", "w")
#	start_time = time(t)
#	write_line(dt, tr, stops, start_time, file)
#	file.close()

def main():
	generate_L1_LV_T()
	generate_L1_LV_R()
	generate_L1_SD_T()
	generate_L1_SD_R()

	generate_L1A_LV_T()
	generate_L1A_LV_R()
	generate_L1A_SD_T()
	
	generate_L1B_LV_T()
	generate_L1B_LV_R()
	generate_L1B_SD_T()
	generate_L1B_SD_R()
	
if __name__ == "__main__":
    main()
