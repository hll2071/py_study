#List 함수
a = [1,2,3]
print(len(a)) #리스트의 길이를 구함, 튜플과 딕셔너리, 문자열에서도 사용 가능

del a[2] #해당 인덱스의 요소를 삭제함
print(a)
a.append(3) #리스트의 마지막에 요소를 추가 ) append([4,5]) 리스트 안에 리스트도 넣을 수 있음
print(a)

a = [1,4,2,3]
a.sort() #정렬 알파벳도 정렬 가능
print(a)

a = [1,4,3,2]
print(a.index(3)) #요소의 위치를 찾아줌 ) 없는 요소면 에러

a.reverse() #요소를 뒤집어서 출력
print(a)

a.insert(4,5) #요소를 삽입 ) 인덱스, 넣을 요소
print(a)

a.remove(5) #제일 처음 오는 요소를 삭제 ) 값이 2개라면 첫 번째 값만 삭제
print(a)

print(a.pop(2)) #결과 : 4 ) 요소를 꺼냄, 꺼낸 요소는 삭제
print(a)

print(a.count(3)) #결과 : 1 ) 원하는 요소의 갯수를 셈

a.extend([4,5,6]) #리스트를 확장 넣은 원래 리스트에 새로 만든 리스트를 더함
print(a)