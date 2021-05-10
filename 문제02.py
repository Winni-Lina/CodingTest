#1월 1일 부터 며칠 만큼 떨어져 있는 지 구합니다.
def func_a(month, day):
   month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   total = 0;
   for i in range(month-1 ):
       total += month_list[i]
   total += day
   return total - 1

#1단계. 시작 날짜가 1월 1일로 부터 며칠 만큼 떨어져있는지 구합니다.
#2단계. 끝 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.
#3단계. (2단계에서 구한 날짜)- (1단계에서 구한 날짜)를 구합니다.

def solution(start_month, start_day, end_month, end_day):
   start_total = func_a(start_month, start_day)
   end_total = func_a(end_month, end_day)
   return end_total - start_total


#The following is code to output testcase.
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

