def sumOfDigits(a):   
    if a >= 1:
        return a % 10 + sumOfDigits(a // 10)
    else:
        return 0
    
inpt = int(input())
print(sumOfDigits(inpt))
