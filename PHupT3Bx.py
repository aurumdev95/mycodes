import subprocess
import datetime
import os
import csv
from schedule import *

schedules = []
readCSV = ""
rows = ""
totalRows = ""

try:
    with open('schedule.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        rows = list(readCSV)
        totalRows = len(rows)
except FileNotFoundError:
    print("schedules.csv not found")
    quit()


for i, column in enumerate(rows):
    schedules.append(Schedule(column[0], column[1], column[2], column[3], column[4], column[5]))

for schedule in schedules:
    print (schedule.baseName)
    print (schedule.channel)
    print (schedule.recordToday)
    print (schedule.startTime)
    print (schedule.endTime)
    print (schedule.highres)