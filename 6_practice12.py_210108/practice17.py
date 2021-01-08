#dictionaray형 사용 예제

dic = {}
dic['dictionaray'] = 'blablablabla'
dic['python'] =  'mamamamamamama'
print(dic)
print('검색할 단어를 입력하세요 :')

inpt = input()

print( dic[inpt])

smalldic = {'dictionary': 'reference', 'python': 'snake', 'line' : 'flat'}
del smalldic['dictionary']

print('\nsmalldic key, value 조회\n')
print(smalldic.keys())
print(smalldic.values())

print('is there line in smalldic?','line' in smalldic)

