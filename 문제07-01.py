#펠린드롬 간단하게 만들어보기
#a[0]과 a[4]를 비교
#a[1]과 a[3]을 비교
#둘다 참이어야만 하죠
######[2]는 비교x 
a = "neven"
a = "seven"

#5글자인 경우
##하나라도 만족하지 못하면, 펠린드롬이 아니다.
if a[0] == a[4]:
    print("펠린드롬이 아니다.")
elif a[1] != a[3]:
    print("펠린드롬이 아니다.")
else:
    print("펠린드롬이다.")

for i in range(2):
    if a[i] != a[4-i]:
        print("펠린드롬이 아니다.")
print("펠린드롬이다.")
a = "enevene"

## 7글자인 경우
##하나라도 만족하지 못하면, 펠린드롬이 아니다.
if a[0] == a[6]:
    print("펠린드롬이 아니다.")
elif a[1] != a[5]:
    print("펠린드롬이 아니다.")
elif a[2] != a[4]:
    print("펠린드롬이 아니다.")
else:
    print("펠린드롬이다.")


for i in range(3):
    if a[i] != a[6-i]:
        print("펠린드롬이 아니다.")
print("펠린드롬이다.")
a = "enevene"