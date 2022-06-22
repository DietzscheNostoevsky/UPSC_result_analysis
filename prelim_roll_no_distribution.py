
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
