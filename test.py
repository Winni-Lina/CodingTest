# 약수의 합
def solution(n):
    answer = 0
    for a in range(1, n + 1):
        if n % a == 0:
            answer += a
    return answer


# 평균
def average(arr):
    result = 0
    for a in arr:
        result += a
    result /= len(arr)
    return result


# py
def py(s):
    answer = True
    p = 0
    y = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p += 1
        elif s[i] == 'y' or s[i] == 'Y':
            y += 1
    if p == y:
        return True
    return False


# 중간
def 중간(s):
    answer = s[len(s) // 2 - 1] + s[len(s) // 2] if len(s) % 2 == 0 else s[len(s) // 2]
    return answer


# 두 개 뽑아서 더하기
def 뽑아더하기(numbers):
    answer = list()
    # numbers[i]는 첫 번째로 뽑은 숫자
    # numbers[j]는 두 번째로 뽑은 숫자
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            두수의합 = numbers[i] + numbers[j]
            answer.append(두수의합)
    # 중복제거
    answer = list(set(answer))
    # 오름차순 정렬
    answer.sort()


def 중복제거(characters):
   result = ""
   result += characters[0]
   for i in range(1, len(characters)):
       if characters[i - 1] != characters[i]:
           result += characters[i]
   return result

