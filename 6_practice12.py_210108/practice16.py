# 각 자리 숫자의 합을 구하는 함수(map 이용)
def sumthing(a):
    
    temp = map(int, list(str(a)))
    return sum(temp)

inpt = int(input())
print(sumthing(inpt))
