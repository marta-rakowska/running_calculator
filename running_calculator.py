#Marathon Time Calculator

#Step 1: INPUT: Ask the runner for their pace (e.g. 5:25)
str_pace = input("Enter your pace in min/km (e.g. 5:21): ")

#Step 2: PROCESS: Convert this input into a number of seconds: e.g. 5:25 = 5 * 60 + 25 = 325 seconds
split_pace = str_pace.split(":")
minutes = int(split_pace[0])
seconds = int(split_pace[1])
pace = minutes * 60 + seconds

#Step 3: PROCESS: Multiply this total by 42 as there are 42km in a Marathon
total_time = pace * 42.195

#Step 4: PROCESS: Convert this new total using the hh:mm:ss format. (e.g 3:47:30)
hours = total_time // 3600
time_left = total_time % 3600

minutes = time_left // 60
seconds = time_left % 60

#Step 5: OUTPUT: Display this new total on screen (using the hh:mm:ss format). (e.g 3:47:30)
print(f'You should complete a marathon in {str(int(hours))}:{str(int(minutes))}:{str(int(seconds)).zfill(2)}.')