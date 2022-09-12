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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# Find all unique numbers making outgoing calls
# Find all unique numbers receiving calls
out_cal_num = []
out_cal_num_unq = []
in_cal_num = []
in_cal_num_unq = []
for call in calls:
    out_cal_num.append(call[0])
    in_cal_num.append(call[1])
out_cal_num_unq = [*set(out_cal_num)]
in_cal_num_unq = [*set(in_cal_num)]
# Find all unique numbers sending texts
# Find all unique numbers receiving texts
out_txt_num = []
out_txt_num_unq = []
in_txt_num = []
in_txt_num_unq = []
for text in texts:
    out_txt_num.append(text[0])
    in_txt_num.append(text[1])
out_txt_num_unq = [*set(out_txt_num)]
in_txt_num_unq = [*set(in_txt_num)]
# Find numbers making outgoing calls but not receiving incoming calls or sending text or receiving text
tm_num_unq = []
for num in out_cal_num_unq:
    if num not in in_cal_num_unq:
        if num not in out_txt_num_unq:
            if num not in in_txt_num_unq:
                tm_num_unq.append(num)
tm_num_unq.sort()
print('These numbers could be telemarketers:','\n')
for n in tm_num_unq:
    print(n,'\n')
