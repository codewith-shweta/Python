import time

my_time = int(input("Enter the time in second:"))
for x in range(my_time,0,-1):
    print(x)
time.sleep(5)
print("Time is up!")
