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

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
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
"""
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import ImportedUDF as udf
def get_lap_data(path): #Function to read lap data from a CSV file
    LapNum = []
    NorrisTime = []
    PiastriTime = []
    while True:
        try:
            with open(path, newline='') as fh:
                reader = csv.reader(fh)
                for column in reader:
                    if len(column) < 3:
                        continue
                    LapNum.append(column[0])
                    NorrisTime.append(column[1])
                    PiastriTime.append(column[2])
            break
        except FileNotFoundError:
            print(f"File not found: {path}")
            # Prompt for a new path inside the loop
            path = input("Please input the csv file path (e.g. Abu_Dhabi2024.csv): ").strip()
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None, None
    LapNum = LapNum[1:]
    NorrisTime = NorrisTime[1:]
    PiastriTime = PiastriTime[1:]
    return LapNum, NorrisTime, PiastriTime
def Piastri_v_Norris(path): #Function to compare lap times and plot them
    LapNum, NorrisTime, PiastriTime = get_lap_data(path)
    if LapNum is None:
        return [], []
    x = []
    norris = []
    piastri = []
    for lx, ln, lp in zip(LapNum, NorrisTime, PiastriTime): #Converts data to appropriate types and handles errors
        try:
            xi = int(lx) #Lap number as integer
            ni = float(ln) #Norris lap time as float
            pi = float(lp) #Piastri lap time as float
        except ValueError: #Error handling for invalid data entries
            continue
        x.append(xi)
        norris.append(ni)
        piastri.append(pi) 
    if not x:
        print("No valid lap data found after processing.")
        return [], [] 
    NorrisSum = sum(norris)
    PiastriSum = sum(piastri)
    NorrisCount = len(norris)
    PiastriCount = len(piastri)
    NorrisAvg = NorrisSum / NorrisCount
    PiastriAvg = PiastriSum / PiastriCount
    print(f"Norris Average Lap Time: {NorrisAvg:.3f} seconds over {NorrisCount} laps.")
    print(f"Piastri Average Lap Time: {PiastriAvg:.3f} seconds over {PiastriCount} laps.")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, norris, color='orange', label='Norris', linewidth=2) #Plot Norris lap times
    ax.plot(x, piastri, color='blue', label='Piastri', linewidth=2) #Plot Piastri lap times
    ax.set_xlabel('Lap Number', fontsize=12)
    ax.set_ylabel('Lap Time (seconds)', fontsize=12)
    ax.set_title('Lap Times for Lando Norris and Oscar Piastri', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=10, integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    ax.grid(which='major', linestyle='--', alpha=0.5)
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.tick_params(axis='both', which='minor', labelsize=0)
    fig.tight_layout()
    plt.show()
    return norris, piastri 
def Calculate_Delta(norris, piastri): #Function to calculate and plot delta lap times
    if not norris or not piastri:
        print("Cannot calculate delta: input lap time lists are empty.")
        return
    Delta_List = [a - b for a, b in zip(norris, piastri)]
    Absolute_Delta_List = [abs(x) for x in Delta_List]
    num_laps = len(Absolute_Delta_List)
    x = [i + 1 for i in range(num_laps)] 
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, Absolute_Delta_List, color='orange', label='Absolute Delta', linewidth=2) #Plot absolute delta
    ax.set_xlabel('Lap Number', fontsize=12)
    ax.set_ylabel('Lap Time Delta (seconds)', fontsize=12)
    ax.set_title('Absolute Delta Lap Times (Norris vs Piastri)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(which='major', linestyle='--', alpha=0.5) 
    ax.xaxis.set_major_locator(MaxNLocator(nbins=10, integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    fig.tight_layout()
    plt.show()
def main(): 
    path = input("Please input the csv file path (e.g. Abu_Dhabi2024.csv): ").strip() #Prompt for CSV file path
    norris, piastri = Piastri_v_Norris(path)
    Calculate_Delta(norris, piastri)
    udf.season_report()
if __name__ == '__main__':
    main()
