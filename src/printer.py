'''
Created on 15.01.2020

@author: Daniel
'''

import csv
from more_itertools import unique_everseen

def to_file(name, tracks):
    print("Collected a total of {} tracks played over the provided time window.".format(len(tracks)))
    
    with open("".join([name, ".csv"]), "w", newline="") as csvfile:
        
        unique = list(unique_everseen(tracks, key=tuple))
        print("Collected a total of {} unique tracks.".format(len(unique)))
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["artist", "title"])
        for row in unique:
            writer.writerow(row)
        csvfile.close()
        print("Tracks were successfully written to .csv")
