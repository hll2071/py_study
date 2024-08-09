#String 함수
a = "hobby"
print(a.count('b')) #결과 : 2 ) 문자열에서 원하는 문자의 갯수를 찾아줌

a = "Python is the best choice"
print(a.find('b')) #결과 : 14 ) 원하는 문자열의 위치를 찾아준다, 없으면 -1

a = "Life is too short"
print(a.index('t')) #결과 : 8 ) 원하는 문자열의 위치를 찾아준다, 없으면 에러

print(",".join(['a','b','c','d'])) #원하는 문자열을 삽입

a = "hi"
print(a.upper()) #대문자로 변환

a = "HI"
print(a.lower()) #소문자로 변환

a = "  HI"
print(a.lstrip()) #왼쪽 공백 삭제

a = "hi  "
print(a.rstrip()) #오른쪽 공백 삭제

a = "  hi  "
print(a.strip()) #양쪽 공백 삭제

a = "Ramen is the best choice"
print(a.replace("Ramen","DDeokbbokyee")) #문자열에 있는 내용을 바꿈

a = "Life is too short"
print(a.split()) #문자열을 원하는 기준으로 나누어 준다. ) 아무것도 없으면 공백을 기준