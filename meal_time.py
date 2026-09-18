def convert(time):
    parts = time.split(":")
    hour = int(parts[0])
    minute = int(parts[1])
    return float(hour + (minute / 60))
    
def meal_time():
    time_hm = input("What time is it?")
    time_decimal = convert(time_hm)
    if time_decimal > 6.5 and time_decimal < 11.5:
        print("Time for breakfast")
    elif time_decimal > 11.5 and time_decimal < 16.5:
        print("Time for lunch")
    elif time_decimal > 16.5 and time_decimal < 22.5:
        print("Time for dinner")
    else time_decimal 
        print("Go back to sleep!)

meal_time()
