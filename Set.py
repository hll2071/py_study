#Set (집합)
s1 = set([3,2,1]) #집합 자료형은 set()키워드를 사용해 만들 수 있다.
s2 = set("Hello") #set()안에 리스트를 젛거나 문자열을 입력하여 만들 수도 있다.
print(s1) #결과 : 1,2,3
print(s2) #결과 : o, l, h, e

#집합의 특징 : 중복 안 됨, 순서가 없다.(오름차순인 것 같다.1,2,3순 a,b,c)
#set 자료형은 순서가 없어서 인덱싱을 못함, 하려면 리스트나 튜플로 변환하여 써야 됨
li = list(s1) #s1은 순서가 없어 오름차순인 1,2,3으로 된 게 리스트료 변한다.
print(li[0])
t1 = tuple(s1)
print(t1[0])
#print(s1[0]) : 오류가 뜨게 된다.

s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
#교집합
print(s3 & s4) #교집합 ) 두 집합에서 같은 것만 골라온다.
print(s3.intersection(s4)) #교집합 함수 ) 교집합과 같은 값을 반환한다.
#합집합
print(s3 | s4) #합집합 ) 두 집합을 합친다. 중복은 한 번만 출력한다.
print(s3.union(s4)) #합집합 함수 ) 합잡합이다.
#차집합
print(s3 - s4) #차집합 ) 두 집합을 뺸다. 무엇을 빼는지에 따라 달라진다.
print(s4 - s3)
print(s3.difference(s4)) #차집합 함수
print(s4.difference(s3))

#집합 관련 함수
s5 = set([1,2,3])
s5.add(4) #1개의 요소만 추가
print(s5)
s5.update([5,6]) #여러 개의 요소를 추가
print(s5)
s5.remove(1) #특정 값을 삭제
print(s5)