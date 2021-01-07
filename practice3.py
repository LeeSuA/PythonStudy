while True:
    year = int(input())
    if (year%4 == 0) & (year%100 == 0) & (year % 400 == 0):
        print('윤년')
    elif (year%4 == 0) & (year%100 == 0):
        print('평년')
    elif (year%4 == 0):
        print('윤년')
    else :
        print('평년')
