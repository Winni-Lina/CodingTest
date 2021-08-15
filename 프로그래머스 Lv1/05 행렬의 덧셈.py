def solution(arr1, arr2):
    answer = [0] * 2
    answer = [[0] * 2]*2
    answer[0][0] = arr1[0][0] + arr2[0][0]
    return answer


arr1 = [
    [1, 2],
    [2, 3]
]

arr2 = [
    [3, 4],
    [5, 6]
]

print(solution(arr1,arr2))