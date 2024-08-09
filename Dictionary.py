#딕셔너리 (Dictionary)
#대응 관계를 나타낼 수 있는 자료형 ) 연관배열, 해쉬라고도 한다. 파이썬에서는 딕셔너리
#딕셔너리는 key와 value를 한 쌍으로 갖는 자료형. if ) people : 사람, 야구 : baseball

dic = {'name' : 'pey', 'phone' : '011-1234-1234', 'birth' : '0409'}
#딕셔너리는 이렇게 중괄호로 사용하고 위에서 키는 name,phone,birth고 value는 pey, 011-1234-1234, 0409가 된다.
#주의사항 : key는 중복되어선 안 됨, key에는 리스트 사용 불가 하지만 튜플은 가능 ) 키 값은 변하면 안 돼서

a = {'a':[1,2,3]} #이렇게 value에는 리스트도 들어갈 수 있다.
a['b'] = [4,5,6] #이렇게 딕셔너리에 쌍을 추가할 수도 있다. ) key가 b이고 value가 [4,5,6]인 쌍 추가
print(a['b']) #key가 'b'인 value만 반환

del a['a'] #딕셔너리 요소 삭제 ) key가 'a'인 key:value 삭제
print(a)

#딕셔너리 관련 함수
print(a.keys()) #해당 딕셔너리의 key만 모아서 dict_keys 객체를 돌려줌 ) 리스트로 변환하려면 list(a.keys())
print(a.values()) #해당 딕셔너리의 value만 모아서 dict_value 객체를 돌려줌
print(a.items()) #해당 딕셔너리의 key와 value의 쌍을 튜플로 묶어 dict_items 객체로 돌려줌
print(a.get('b')) #해당 key에 대응되는 value를 돌려줌, a['b']와 같음 ) 차이점은 a['b']일 때 b가 없으면 에러, get은 none을 돌려.
#get()에서 key값이 없을 때 미리 정해둔 디폴트 값을 가져오게 할 수 있다 ) get('key', '디폴트')
print('b' in a) #해당 key가 딕셔너리에 있는 지 확인, 있으면 True 없으면 False
a.clear() #key:value 쌍을 모두 지운다.
print(a)
