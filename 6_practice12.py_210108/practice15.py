# 각 자리 숫자의 합을 구하는 함수(리스트 이용)


def sumthing(num):
    sum = 0
    lst = list(str(num))
    
    for i in lst:
        sum += int(i)

    return sum

inpt = int(input())
print(sumthing(inpt))
