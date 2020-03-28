fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        lines = line.rstrip().split()
        count = count + 1
        print(lines[1])
    else:
        continue

print("There were", count, "lines in the file with From as the first word")
