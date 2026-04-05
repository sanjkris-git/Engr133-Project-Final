"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Imports CSV lap time data for Lando Norris and Oscar Piastri, converts them to lists and graphs the race lap data. Then, calculates average lap time and graphs the delta.

Assignment Information:
    Assignment:     18.2 - Dream Project
    Team ID:        008 - 17
    Author:         Sanjay Krishnan, krish379@purdue.edu
    Date:           11/30/2025

Contributors:
    -- W3Schools for code examples on glob and dictionary usage. --
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work. 

    Sources of help: 
        Glob - https://www.w3schools.com/python/ref_module_glob.asp
        Dictionary - https://www.w3schools.com/python/python_dictionaries.asp
"""
import csv
import os
import glob
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def season_report(search_path=None, show_plot=True, save_plot_path=None):
    if search_path is None:
        search_path = os.path.join(os.path.dirname(__file__), '.') 
    csv_files = glob.glob(os.path.join(search_path, '*.csv')) #Gets all csv files in the directory
    if not csv_files:
        print(f"No CSV files found in {search_path}") #Error handling for no csv files found
        return {}
    races = {}
    for file_path in csv_files: #Interates through all csv files in the directory
        race_name = os.path.basename(file_path).replace('.csv', '') 
        LapNum = []
        NorrisTime = []
        PiastriTime = []
        try:
            with open(file_path, newline='') as fh:
                reader = csv.reader(fh)
                next(reader, None)  # skip possible header
                for column in reader:
                    if len(column) < 3:
                        continue
                    try:
                        lap = int(column[0])
                        n_time = float(column[1])
                        p_time = float(column[2])
                    except ValueError: #Error handling for invalid data entries
                        continue
                    LapNum.append(lap)
                    NorrisTime.append(n_time)
                    PiastriTime.append(p_time)
            if LapNum:
                races[race_name] = (LapNum, NorrisTime, PiastriTime) #Stores data in dictionary
        except Exception as e:
            print(f"Error reading {file_path}: {e}") #Error handling for file read issues
            continue
    if not races:
        print("No valid race data loaded.") #Error handling for no valid data
        return {}
    averages = {}
    for race, (laps, n_times, p_times) in sorted(races.items()): #Calculates average lap times for each
        n_avg = sum(n_times) / len(n_times) if n_times else None
        p_avg = sum(p_times) / len(p_times) if p_times else None
        averages[race] = {'Norris Avg': n_avg, 'Piastri Avg': p_avg}
    races_sorted = sorted(averages.keys())
    x = list(range(len(races_sorted)))
    norris_vals = [averages[r]['Norris Avg'] for r in races_sorted] #Prepares data for plotting
    piastri_vals = [averages[r]['Piastri Avg'] for r in races_sorted] #Prepares data for plotting

    # Plotting the average lap times
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.plot(x, piastri_vals, marker='o', linestyle='-', color='blue', label='Oscar Piastri')
    ax.plot(x, norris_vals, marker='o', linestyle='-', color='orange', label='Lando Norris')
    
    # Customize x-axis labels
    ax.set_xticks(x)
    ax.set_xticklabels(races_sorted, rotation=45, ha='right')
    ax.set_xlabel('Race')
    ax.set_ylabel('Average Lap Time (s)')
    ax.set_title('2024 McLaren F1 Team Season Average Pace Comparison')
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    # Ensure rotated x-axis labels are not clipped
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.2)
    plt.show()

if __name__ == '__main__':
    season_report()