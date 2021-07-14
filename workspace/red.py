from __future__ import print_function  ## for Python 2.XX
import nltk
import csv
import inflection as infl

## import CSV file.
## Please keep the CSV on same directory, or change path. ----
with open('sample.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    line = [row for row in reader]

## -----------------------------------------------------------


## Store data of month and value into List ----------------
value = []
month = []
for i in range(len(line)):
    if i == 0: ## First line should be title.
        sentence = line[i][0]
    elif line[i][0] == '': ## if there no word, continue.
        continue;
    else:
        month.append(line[i][0])
        value.append(int(line[i][1]))

## --------------------------------------------------------

## Divide subject with NLTK ----------------------------
divide = nltk.word_tokenize(sentence)
pos = nltk.pos_tag(divide)
flag = 0
for i in range(len(pos)):
    if pos[i][1] in ["IN"]: ## if subject is "A of B"
        head = infl.pluralize(divide[i-1])
        tail = divide[i+1]
        flag = 1
        OF = 1
        break;
    else:
        continue;
if flag == 0: ## TODO: This "if" block is unverified !!
    for i in range(len(pos)): ## if subject is "A B"
        if pos[i][1] in ["NN", "NNP", "NNS"]:
            head = divide[i]
            tail = infl.pluralize(divide[i+1])
            OF = 0
            break;
        else:
            continue;

## --------------------------------------------------------

## Change subject 5 pattern ----------------------------------
subject = []
if OF == 1:
    subject.append(head + " of " + tail)
    subject.append(tail.capitalize() + " " + head.lower())
    subject.append("The " + head.lower())
    subject.append(head)
    subject.append("They")

if OF == 0: ## TODO: This "if" block is unverified !!
    subject.append(head + " " + tail)
    subject.append(tail.capitalize() + " of " + head.lower())
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
for i in range(len(value)-1):
    
    sub = abs(value[i] - value[i+1])
    
    print(subject[i], end=' ')
    
    if value[i] > value[i+1]:
        print("decrease from " + month[i] + " to " + month[i+1] + " by " + str(sub) + ".")
    elif value[i] < value[i+1]:
        print("increase from " + month[i] + " to " + month[i+1] + " by " + str(sub) + ".")
    else:
        print("remain stable from " + month[i] + " to " + month[i+1] + ".")




