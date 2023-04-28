import csv
import sys
import re
from datetime import datetime

#Read command line arguments
if len(sys.argv) != 3:
    print('Formatting error!')
    print('Example: weather_spacer.py <IN_FILE> <OUT_FILE>')
    quit()

print("Processing...")
    
#Configure .csv files
in_file = sys.argv[1]
out_file = sys.argv[2]

#Clarify variables (Not necessary)
date_old = 0
parsed_date = 0
month_old = 0
day_old = 0
year_old = 0
hour_old = 0
minute_old = 0
sum_old = 0
month_new = 0
day_new = 0
year_new = 0
hour_new = 0
minute_new = 0
empty_cnt = 0

#Open files and get to work
with open(out_file, 'w', newline='') as csv_out_file, open(in_file) as csv_in_file:
    csv_writer = csv.writer(csv_out_file, delimiter=',')
    csv_reader = csv.reader(csv_in_file, delimiter=',')
    line_cnt = 0
    line_pos = 0
    
    #Search input file for data row by row
    for row in csv_reader:
        #Copy the first 8 rows in the file header
        if line_cnt < 8:
            csv_writer.writerow(row)
        #Use first line of data to configure variables
        elif line_cnt == 8:
            #Read date cell
            date = row[1]
            #Parse numbers from the date cell
            parsed_date = re.findall(r'\d+', date)
            #Convert parsed string digits to integers
            month_old = int(parsed_date[0])
            day_old = int(parsed_date[1])
            year_old = int(parsed_date[2])
            hour_old = int(parsed_date[3])
            minute_old = int(parsed_date[4])
            #Write row to output file
            csv_writer.writerow(row)
        else:
            #Read date cell
            date = row[1]
            #Parse numbers from the date cell
            parsed_date = re.findall(r'\d+', date)
            #Convert parsed string digits to integers
            month_new = int(parsed_date[0])
            day_new = int(parsed_date[1])
            year_new = int(parsed_date[2])
            hour_new = int(parsed_date[3])
            minute_new = int(parsed_date[4])
            
            #Convert date numbers into a date object to easily manipulate it
            dt_new = datetime(year_new, month_new, day_new, hour_new, minute_new)
            dt_old = datetime(year_old, month_old, day_old, hour_old, minute_old)
            
            #Figure out how many minutes are between readings
            dt_diff = dt_new - dt_old
            diff_h = int(dt_diff.total_seconds() / 3600)
            
            #Shift new data to be old data
            year_old = year_new
            month_old = month_new
            day_old = day_new
            hour_old = hour_new
            minute_old = minute_new
            
            #Inject empty rows if data is missing
            loop_cnt = 1
            while loop_cnt < diff_h:
                csv_writer.writerow('\r')
                loop_cnt = loop_cnt + 1
                empty_cnt = empty_cnt + 1
            
            #Write row to output file
            csv_writer.writerow(row)
        line_cnt = line_cnt + 1

#End info
print("Processing finished!")
out_str = "Data entries processed:" + str(line_cnt - 7)
print(out_str)
out_str = "Missing data entries:" + str(empty_cnt)
print(out_str)
exit()