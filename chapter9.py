name = input("Enter file:")
froms = dict()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith('From '):
        sented = (line.rstrip().split())[1]
        froms[sented] = froms.get(sented, 0) + 1
    else:
        continue

max = None
maxkey = None
for key, value in froms.items():
    if max == None or value > max:
        max = value
        maxkey = key

print(maxkey, max)