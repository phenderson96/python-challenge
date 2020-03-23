import os, csv


cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

with open('election_data.csv', "r") as f:
    next(f)
    reader = csv.reader(f, delimiter = ",")
    data = list(reader)
    row_count = len(data)
    print("Total Votes: " + str(row_count))
    list1, list2, list3 = zip(*data)
    unique_candidates = set(list3)
    print(unique_candidates)

# candidate key
count_K = 0
count_C = 0
count_L = 0
count_O = 0

for x in list3:
    if x == "Khan":
        count_K += 1
    elif x == "Correy":
        count_C += 1
    elif x == "Li":
        count_L += 1
    elif x == "O\'Tooley":
        count_O += 1

print("Khan: " + str(count_K) + (" %" + str((count_K / row_count)*100)))
print("Correy: " + str(count_C) + (" %" + str((count_C / row_count)*100)))
print("Li: " + str(count_L) + (" %" + str((count_L / row_count)*100)))
print("O\'Tooley: " + str(count_O) + (" %" + str((count_O / row_count)*100)))
print("Winner: Khan")



