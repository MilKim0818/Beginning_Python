
ex = (2, 4, (1, 3), [10, 20, 30])

## [문제 1] 튜플 변수 ex의 길이
print('튜플 변수 길이1 >>', len(ex))

## [문제 2] 튜플 변수 ex의 리스트 요소에 40을 추가 (단, 마지막 위치에 추가)
print('리스트 요소', ex[-1])
print('리스트 요소', type(ex[-1]))
ex[-1].append(40)
print('ex >>', ex)
print('튜플 변수 길이2 >>', len(ex))
