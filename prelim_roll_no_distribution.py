
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

for lums in roll:
