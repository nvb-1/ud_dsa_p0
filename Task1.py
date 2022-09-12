"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_ph_no = []
for i in range(len(calls)):
    if calls[i][0] not in unique_ph_no:
        unique_ph_no.append(calls[i][0])
    if calls[i][1] not in unique_ph_no:
        unique_ph_no.append(calls[i][1])
for j in range(len(texts)):
    if texts[j][0] not in unique_ph_no:
        unique_ph_no.append(texts[j][0])
    if texts[j][1] not in unique_ph_no:
        unique_ph_no.append(texts[j][1])
print('There are',len(unique_ph_no),'different telephone numbers in the records')
