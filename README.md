# ENGR 13300 Final Project - F1 Telemetry Visualizer
A Python-based data analysis tool that ingests raw Formula 1 CSV lap data to compare the performance of McLaren drivers Lando Norris and Oscar Piastri. The script cleans the data, calculates averages, and generates comparative visualizations.

**F1 Telemetry Analyzer**
Python program built to parse and visualize Formula 1 race data. Processes raw CSV lap times, handles missing data points, and utilizes matplotlib to graph head-to-head performance and absolute lap deltas between drivers Oscar Piastri and Lando Norris. Built for Purdue University's _ENGR 13300 - Transforming Ideas To Innovation_ Final Project.

**How It's Made:**
Tech used: Python, Matplotlib, CSV module, OS module

This project was built to automate the analysis of raw racing telemetry. The program starts by reading a CSV file containing lap-by-lap data for a specific race. Real-world data is rarely perfect, so I utilized Python's csv module alongside custom logic to skip malformed rows (checking if the column length was less than 3).

From there, I built a data pipeline that:
1. Extracts the raw string data for Lap Number, Norris's time, and Piastri's time.
2. Scrubs the data, converting strings into functional int and float arrays using a try/except block to catch ValueErrors and filter out bad entries.
3. Calculates the average lap times over the course of the race.
4. Uses matplotlib to generate two distinct visualizations: a head-to-head lap time comparison and an absolute delta graph showing the time gap between the two drivers per lap.

(Note: The script also relies on an external local module, ImportedUDF.py, which handles a season report output at the end of the execution.)

**Optimizations**
I implemented a try/except block checking for FileNotFoundError. If the file is missing, the script loops and prompts the user to input the correct file path (e.g., Abu_Dhabi2024.csv) dynamically in the terminal. Additionally, using the zip() function allowed me to iterate through the lap, Norris, and Piastri arrays simultaneously in a highly efficient, readable manner without relying on clunky index counters.
