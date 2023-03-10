""" 
[리스트] list
- 여러 개의 데이터를 묶어서 관리
- [값1, 값2, ...]
- 순서 유지
"""
# index 0, 1, 2 / [값1, 값2, 값3]은 요소 또는 원소 (영어로 element)라고 부름 
#class에 대한 설명은 다음 강의때 

num = 5
print('num >>', num)
print('num의 자료형 >>', type(num))

data = [1, 3, 5]
print('data >>', data)
print('data의 자료형 >>', type(data))

## 인덱싱 : 하나의 요소 추출
print('첫번째 요소 추출 >>', data[0]) 
#여기서 0은 인덱스 0을 의미함 
print('두번째 요소 추출 >>', data[1]) 
print('마지막 요소 추출1 >>', data[2])
print('마지막 요소 추출2 >>', data[-1])
#오른쪽부터 시작될 경우, -1부터 시작 (마지막 요소 추출할 때 -1을 쓰는 게 좋음)

## 슬라이싱 : 연속된 여러 개의 요소 추출
print('첫번째~두번째 요소 추출1 >>', data[0:2])
# 대괄호 안에서는 띄어쓰기 하지 않음 (일반적인 문법에서)
# 시작 인덱스는 포함, 끝 인덱스는 제외 
print('첫번째~두번째 요소 추출2 >>', data[:2])
# 인덱스 : 처음에 생략하면, 처음부터
print('두번째~마지막 요소 추출1 >>', data[1:3])
# 인덱스 2까지만 있는데, 없는 인덱스 3을 넣은거임 (문법때문에..) 좋은 형태가 아님
print('두번째~마지막 요소 추출2 >>', data[1:])
# 인덱스 : 뒤에 생략하면, 마지막 요소까지
print('시작 인덱스, 끝 인덱스 모두 생략 >>', data[:])
# 처음부터 끝까지 (다 나옴)
print('data >>', data)
# data 프린트랑 결과값이 같게 보이는 거고, 내부적인 처리가 다르다 ! 

even = [2, 4, 6, '육', 2.2, [12, 14, 16], 8, 10]
# 정수, 실수, 문자열 데이터 같이 들어있어도 (어떤 type이 와도) 문제가 없음..!
# 다른 언어는 배열 안에 같은 type만 있어야 함 / 파이썬은 리스트 안에 여러 type 같이 써도 됨
print('요소 개수(길이) >>', len(even))
print('리스트 요소 추출 >>', even[-3])
print('리스트 요소 추출 >>', even[-3][0])
