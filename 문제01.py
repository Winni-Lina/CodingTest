# "S":5%
# "G":10%
# "V":15%

def solution(price, grade):
    if grade == "S":
        return price - price*0.05
    if grade == "G":
        return price - price*0.1
    if grade == "V":
        return price - price*0.15


#testcase를 위한 output
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)
print("ret1의 값은? ", ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)
print("ret2의 값은? ", ret2, ".")