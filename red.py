from __future__ import print_function  ## for Python 2.XX
import nltk
import csv

## import CSV file.
## Please keep the CSV on same directory, or change path. ----
with open('sample.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    line = [row for row in reader]

## -----------------------------------------------------------

#title = "price of Banana"
#value = [100, 120, 140, 110, 100, 100]
#month = ["January", "February", "March", "April", "May", "June"]

## Store data of month and value into List.----------------
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
        
#sentence = "Price of banana"

## Debug ---------
#print(sentence)
#print(month)
#print(value)

## ---------------

## Output sequenses -----------------------------------------------------------------------
for i in range(len(value)-1):
    
    sub = abs(value[i] - value[i+1])
    
    print(sentence, end=' ')
    
    if value[i] > value[i+1]:
        print("decrease from " + month[i] + " to " + month[i+1] + " by " + str(sub) + ".")
    elif value[i] < value[i+1]:
        print("increase from " + month[i] + " to " + month[i+1] + " by " + str(sub) + ".")
    else:
        print("remain stable from " + month[i] + " to " + month[i+1] + ".")



