sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.

sen = sentence.split(' ')
sen1 = list()
for i in sen:
    if i[0] == i[len(i) - 1]:
        sen1.append(i)
    else:
        continue
same_letter_count = len(sen)