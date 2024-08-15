#def (함수)
#함수를 쓰는 이유 : 같은 내용을 반복해서 작성하지 않도록, 효율적인 코딩

#파이썬에서의 함수 만들기
def add(a, b):
    return a + b
#이렇게 함수를 만든다. 이름은 add, 2개의 입력을 받고 a+b를 반환
a = 1
b = 2
print(add(a, b)) #3이 나옴
print(add(a = 3,b=4)) #이렇게 매개변수를 지정하여 쓸 수도 있다

#입력, 결과가 없는 함수
def say() :
    print("hello")
say() #함수를 호출하자마자 출력하게 된다.

#여러개의 입력
def add_mul(choice, *args): #*args처럼 매개변수 앞에 *을 붙이면 모든 입력값을 모아 튜플로 바꿔준다.
    if choice == "add":     #**이 붙는다면 딕셔너리로 바꾸어 저장한다.
        result = 0
        for i in args:
            result += i
        return result
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

print(add_mul("add", 1,2,3))

#lambda
add = lambda a,b: a+b
print(add(1,2))