from __future__ import print_function  ## for Python 2.XX
import nltk ## NEED: % pip install nltk
import csv
import inflection as infl ## NEED: % pip install inflection
import matplotlib.pyplot as plt ## NEED: % pip install matplotlib

## import CSV file.
## Please keep the CSV on same directory, or change path. ----
with open('sample.csv', 'r', newline='', encoding='utf-8-sig') as csvFile:
    reader = csv.reader(csvFile)
    line = [row for row in reader]

## -----------------------------------------------------------

## Store data of month and value into List.----------------
value = []
month = []
for i in range(len(line)):
    if i == 0: ## First line should be title.
        sentence = line[i][0]
    elif line[i][0] == '': ## if there no word, continue.
        continue;
    else:
        if len(line[0]) > 2:
            for j in range(len(line[0])):
                month.append(line[i][j])
                value.append(int(line[i+1][j]))
            break;
        else:
            month.append(line[i][0])
            value.append(int(line[i][1]))

## --------------------------------------------------------

## Divide subject with NLTK ----------------------------
divide = nltk.word_tokenize(sentence)
pos = nltk.pos_tag(divide)
flag = 0
tail_ = ""
for i in range(len(pos)):
    if pos[i][1] in ["IN"]: ## if subject is "A of B"
        head_ = infl.pluralize(divide[i-1])
        for j in range(i, len(pos)-1):
            tail_ = tail_ + divide[j+1]
            if j == len(pos)-2:
                break;
            tail_ = tail_ + " "
        flag = 1
        OF = 1
        break;
    else:
        continue;
if flag == 0:
    for i in range(len(pos)): ## if subject is "A B"
        if pos[i][1] in ["NN", "NNP", "NNS", "NNPS"]:
            head_ = divide[i]
            tail_ = infl.pluralize(divide[i+1])
            OF = 0
            break;
        else:
            continue;

head = head_.lower()
tail = tail_.lower()

## --------------------------------------------------------

## Change subject 5 pattern ----------------------------------
subject = []
if OF == 1:
    subject.append(head.capitalize() + " of " + tail)
    subject.append(tail.capitalize() + " " + head)
    subject.append("The " + head)
    subject.append(head.capitalize())
    subject.append("They")

if OF == 0:
    subject.append(head.capitalize() + " " + tail)
    subject.append(tail.capitalize() + " of " + head)
    subject.append("The " + tail)
    subject.append(tail.capitalize())
    subject.append("They")

## ------------------------------------------------------------

## Debug ---------
#print(sentence)
#print(month)
#print(value)
#print(head)
#print(tail)
#print(subject)

## ---------------

## Output sequenses -----------------------------------------------------------------------
upVerbs = ["increase", "gain", "rise"]
downVerbs = ["decrease", "fall", "decline"]
sameVerbs = ["remain stable", "keep stable ", "maintain stable"]
graph_m = [1, 2, 3, 4, 5, 6]
x = 0
y = 0
z = 0

for i in range(len(value)-1):
    
    sub = abs(value[i] - value[i+1])
    
    print(subject[i], end=' ')
    
    if value[i] > value[i+1]:
        print(downVerbs[x] + " from " + month[i] + " to " + month[i+1] + " by " + str(sub) + ".")
        x+=1
    elif value[i] < value[i+1]:
        print(upVerbs[y] + " from " + month[i] + " to " + month[i+1] + " by " + str(sub) + ".")
        y+=1
    else:
        print(sameVerbs[z] + " from " + month[i] + " to " + month[i+1] + ".")
        z+=1

    if x == len(upVerbs)-1:
        x=0
    if y == len(downVerbs)-1:
        y=0
    if z == len(sameVerbs)-1:
        z=0

plt.plot(graph_m, value)
plt.show()
