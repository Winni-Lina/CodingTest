#펠린드롬 간단하게 만들어보기
#a[0]과 a[4]를 비교
#a[1]과 a[3]을 비교
#둘다 참이어야만 하죠
######[2]는 비교x 

a = "neven"
b = "abccba"

## 5글자인 경우
for i in range(3):
    if a[i] != a[len(a)-1 -i]:
        print("펠린드롬이 아니다.")
print("펠린드롬이다.")
