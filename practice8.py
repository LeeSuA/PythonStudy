scp1, scp2 = map(int, input().split())
L = list(map(int, input().split()))
for i in L:
    if i == -999: break
    elif scp1 <= i <= scp2:
        print('Nothing to report')
    else:
        print('Alert!')
        break
