
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
