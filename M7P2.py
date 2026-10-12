start_val= int(input("Enter the starting value: "))
stop_val= int(input("Enter the stopping value: "))
increment= int(input("Enter the increment value: "))

current_val = start_val
while current_val < stop_val:
    print(current_val)
    current_val += increment