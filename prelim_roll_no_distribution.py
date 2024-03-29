#!/usr/bin/env python
# 2022 prelims result analysis

import csv
import readline


# %%
fname = "result_prelims_2022.txt"
# %%
roll = []
with open(fname, 'r') as fileref:
    lines = fileref.readlines()
    for line in lines:
        b = line.strip()
        roll.append(b)
# %%
quali = []
for nums in roll:
    if len(nums) < 1:
        continue
    else:
        num = nums.split()

        for n in num:
            quali.append(n)

quali.sort()

# list quali contains all the roll numbers of the qualified candidates
# %%
# opening the csv file in 'w+' mode
file = open('qualified.csv', 'w+')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerow(quali)


# %%
quali_int = []
for q in quali:
    q = int(q)
    quali_int.append(q)
# %%
for a in range(0, 10000000, 1000000):
    print(a)

# %%
quali_dict = {}
for a in range(0, 10000000, 1000000):
    for num in quali_int:
        if num > a and num < (a+1000000):
            quali_dict[a] = quali_dict.get(a, 0) + 1


# %%
