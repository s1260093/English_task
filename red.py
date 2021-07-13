from __future__ import print_function
import nltk
title = "price of Banana"
#value = {'Jan':100, 'Feb':120, 'Mar':140, 'Apr':110, 'May':100, 'Jun':150}
value = [100, 120, 140, 110, 100, 100]
month = ["January", "February", "March", "April", "May", "June"]
sentence = "Price of banana"


for i in range(len(value)-1):
    
    sub = abs(value[i] - value[i+1])
    
    print(sentence, end=' ')
    
    if value[i] > value[i+1]:
        print("decrease from " + month[i] + " to " + month[i+1] + " by " + str(sub) + ".")
    elif value[i] < value[i+1]:
        print("increase from " + month[i] + " to " + month[i+1] + " by " + str(sub) + ".")
    else:
        print("remain stable from " + month[i] + " to " + month[i+1] + ".")


