"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
unique_ph_no = []
for i in range(len(calls)):
    if calls[i][0] not in unique_ph_no:
        unique_ph_no.append(calls[i][0])
    if calls[i][1] not in unique_ph_no:
        unique_ph_no.append(calls[i][1])
unique_ph_no_dur = [0]*len(unique_ph_no)
for j in range(len(unique_ph_no)):
    for k in range(len(calls)):
        if unique_ph_no[j] in calls[k]:
            unique_ph_no_dur[j]+=int(calls[k][3])
index = unique_ph_no_dur.index(max(unique_ph_no_dur))

print(unique_ph_no[index],'spent the longest time,',unique_ph_no_dur[index],'seconds, on the phone during September 2016.')