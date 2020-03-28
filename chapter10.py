name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = dict()
lists = list()
for line in handle:
    if line.startswith('From '):
        hrs = line.split()[5].split(':')[0]
        hours[hrs] = hours.get(hrs, 0) + 1
    else:
        continue

for k,v in hours.items():
    lists.append((k, v))

lists.sort()

for a, b in lists:
    print(a, b)
# print(lists)