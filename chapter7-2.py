# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
index = 0
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        index = line.index('0')
        line = float(line[index:])
        sum = sum + line
        count = count + 1

print("Average spam confidence:", sum / count)