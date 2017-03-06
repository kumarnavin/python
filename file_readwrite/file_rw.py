# Reading from a file
all_names = []
with open('namelist.txt', 'r') as namelist_file:
    all_names = namelist_file.read().splitlines()

# first implementation
unique_names1 = {}
for name in all_names:
    try:
        unique_names1[name] += 1
    except KeyError:
        unique_names1[name] = 1

for pair in unique_names1.items():
    print('first', pair)

# second implementation
unique_names2 = {}
for name in all_names:
    if name in unique_names2:
        unique_names2[name] += 1
    else:
        unique_names2[name] = 1

for pair in unique_names2.items():
    print('second', pair)

namelist_file.close()

# third implementation
unique_names3 = {}
with open('namelist.txt', 'r') as namelist_file:
    line = namelist_file.readline()
    while line:
        line = line.strip()
        if line in unique_names3:
            unique_names3[line] += 1
        else:
            unique_names3[line] = 1
        line = namelist_file.readline()

for pair in unique_names3.items():
    print('third', pair)

# End of file
