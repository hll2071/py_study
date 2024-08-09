#If 제어문
#파이썬에서의 제어문 If는 다른 언어들과 사용법이 다르다.
if 1==1 :
    print(1)
#이렇게 if 다음에 조건식을 쓰고 : 으로 마무리한다. 파이썬은 들여쓰기가 중요하다.
#and or not도 사용이 가능하다.
money = 3000
card = True
if money >= 3000 or card == True:
    print("택시타")
#돈이 3000원 이상이거나 카드가 있다. 둘 중 하나라도 참이면 참이 된다. 저렇게 쓸 수 잇다.
# x in (리스트, 튜플, 문자열) / x not in (리스트, 튜플 ,문자열)
print(1 in [1,2,3]) #1이 리스트 [1,2,3] 인에 있는가? True
print(1 not in [1,2,3]) #1이 리스트 [1,2,3] 안에 없는가? False

if 1==1 : #pass 아무 일도 하지 않도록 설정하고 싶을 때, 1==1이 맞으면 아무 일도 없음, 아니면 거짓 출력
    pass
else :
    print("거짓")

#elif C언어에서의 else if 와 같다.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket : print("택시를 타고 가라")
elif card : print("택시를 타고 가라")
else : print("걸어 가")