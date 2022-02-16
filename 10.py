t = int(input())

for f in range(t):

    target, current_run, ball = input().split()
    target = int(target)
    current_run = int(current_run)
    ball = int(ball)

    over_remains = ball /6
    played_overs = (50*6 - ball)/6
    
    current_run_rate = current_run / played_overs
    current_run_rate = "{:.2f}".format(current_run_rate)

    target_run_rate = (target+1-current_run) / over_remains
    target_run_rate = "{:.2f}".format(target_run_rate)

    print(current_run_rate, target_run_rate)