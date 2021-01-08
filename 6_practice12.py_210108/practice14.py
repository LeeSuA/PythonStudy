#성적표 예제

import operator
from functools import reduce

doggy = [90, 85, 70]
ducky = [88, 79, 92]
sole = [100, 100,100]
miche = [90, 60, 70]

students = [doggy, ducky, sole, miche]

for scores in students:
    
    total = 0
    
    for s in scores:
        total = total + s
    average = total / 3
    
    print(scores, total, average)

#다른 방법
print('\nanother way')
for scores in students:

    total = reduce(operator.add, scores)  
    average = total / len(scores)
    
    print(scores, total, average)
    
