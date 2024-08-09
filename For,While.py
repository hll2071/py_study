#반복문 While, For
a = 10
while a != 0 : #while문은 C언어에서의 while 문과 동일하다.
    print(a)
    a -= 1

li = ['one', 'two', 'three']
for i in li :
    print(i) #출력 : one two three ) 이렇게 for문의 기본 구조는 for 변수 in (리스트, 튜플, 문자열)이다.

a = [(1,2),(3,4),(5,6)]
for (fst,snd) in a :
    print(fst,snd) #출력 : 1 2/3 4/5 6 ) 이렇게 튜플을 넣을 때는 변수도 튜플로 지정하면 각각의 변수로 자동으로 들어간다.

#점수를 보고 시험 통과인지 아닌지 출력하는 프로그램
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60 :
        print(f"{number}번 학생은 통과입니다.")
    else :
        print(f"{number}반 학생은 미통과입니다.")

#range 함수
a = range(10) #이름 그대로 범위를 가진 객체를 만들어준다, range를 사용하여 위의 코드를 고쳐보자 range(시작값,마지막값-1)
number = 0
for number in range(1,len(marks)+1) :
    if marks[number-1] < 60 : continue
    print(f"{number}번 학생 축하합니다. 통과입니다.")

#for문을 이용한 구구단
for i in range(2,10) : #2~9까지
    for j in range(1,10) : #1~9까지
        print(i*j,end=" ") #i*j 마지막에 공백 출력, 해당 줄에서 계속 출력하도록 함
    print("") #줄바꿈

#리스트 내포
#리스트 각 항목에 a를 곱한 결과를 넣어보자
a = [1,2,3,4]
res1 = []
for i in a :
    res1.append(i*3)
print(res1)

#리스트 내포 사용한 코드
res2 = [i*3 for i in a]
print(res2)

#리스트 내포를 이용해 3으로 곱해진 수가 짝수인 수만 넣고 싶으면
res3 = [i*3 for i in a if i % 2 == 0]
print(res3)

#구구단 리스트 내포
gugudan = [i*j for i in range(2,10) for j in range(1,10)]
print(gugudan)