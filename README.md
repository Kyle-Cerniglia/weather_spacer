# weather_spacer

An application that will insert empty rows into a .csv file where there is missing weather station data.

Requires Python 3.11.3 or newer to be installed.
Link: https://www.python.org/downloads/

Instructions:
1: Copy your .csv file containing your weather data to the folder containing the weather_spacer.py file.

2: Open a cmd window in the directory containing the weather_spacer.py file.

3: Run the file with the following command: weather_spacer.py INPUT_FILE_NAME.csv OUTPUT_FILE_NAME.csv

Example: weather_spacer.py QBHA3.csv QBHA3_formatted.csv

4: Script will read data from the INPUT FILE NAME, then create a new file called OUTPUT FILE NAME and dump the corrected data there.