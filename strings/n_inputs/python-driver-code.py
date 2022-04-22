# Python Driver Code

def solve(opening_time: str, duration: str) -> str:
  def solve(start_time, total_duration):
    ending_hr = (start_time[0] +total_duration[0]) % 24
    ending_minute = (start_time[1] + total_duration[1])
    if ending_minute > 59:
        ending_hr +=1
        if ending_hr>=24:
            ending_hr -=24
        ending_minute -=60
    print(ending_hr, ending_minute)
    
n = int(input())
for i in range(n):
    start_time = list(map(int, input().split(" ")))
    total_duration = list(map(int, input().split(" ")))
    solve(start_time, total_duration)

  return 

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  a = input()
  b = input()
  answer = solve(a, b)
  print(answer)
