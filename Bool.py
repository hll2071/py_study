#불(bool) 자료형
a = True #bool ) 참 거짓을
b = False
print(type(a)) #bool이라는 자료형으로 지정된 것을 알 수 있다.
print(type(b))

print(1==1) #조건이 참이면 True 거짓이면 False를 반환
print(2>1)
print(2<1)

#자료형에서의 참과 거짓 ) 문자열,리스트,튜플,딕셔너리의 값이 비어있으면 거짓, 하나라도 있으면 참
#숫자형은 0이면 거짓 다른 숫자들은 참

#ex )
a = [1,2,3,4]
while a :
    print(a.pop()) #리스트 안에 요소들을 하나씩 뽑음, 리스트 아에 값이 사라지면 False가 되므로 반복문 탈

if [1,2,3] :
    print("참")
else :
    print("거짓")
print(bool("python"))
print(bool(""))
print(bool([]))
print(bool(0))
print(bool(3))