import re
file = open('regex_sum_2.txt')
sum = 0
count = 0
for line in file:
    numbers = re.findall('[0-9]+', line)
    count = count + len(numbers)
    for number in numbers:
        sum = sum + int(number)

print(count)
print(sum)