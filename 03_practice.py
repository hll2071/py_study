#다음 코드의 결괏값은 무엇일까?
a = "Life is too short, you need python"

if "wife" in a : print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else : print("none")
#1,2번은 거짓 3번이 참 4번도 참이므로 3번 shirt가 출력되고 끝나게 된다.

#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자.
res = 0
i = 1
while i <= 1000 :
    if i % 3 == 0 :
        res += i
    i+=1
print(res) #166833

#while문으로 별찍기
i=0
while True :
    i+=1
    if i>5 : break
    print("*"*i)

#for문을 사용해 1부터 100까지 출력하기
for i in range(1,101) :
    print(i)

#for 문을 이용해 A학급의 평균 점수 구하기
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for i in A :
    total += i
avg = total/len(A)
print(avg)

#리스트 내포를 이용하여 홀수에만 2를 곱해서 저장
num = [1,2,3,4,5]
res = [i*2 for i in num if i%2==1]
print(res)