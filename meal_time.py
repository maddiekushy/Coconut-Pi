def meal_time():
    time = input("What time is it?")

    parts = time.split(":")
    hour = int(parts[0])
    minute = int(parts[1])

    decimal_hours = hour + (minute / 60)

    if decimal_hours > 6.5 and decimal_hours < 11.5:
        print("Time for breakfast")
    if decimal_hours > 11.5 and decimal_hours < 16.5:
        print("Time for lunch")
    if decimal_hours > 16.5 and decimal_hours < 22.5:
        print("Time for dinner")
    elif decimal_hours > 22.5 and decimal_hours < 6.5:
        print("Go back to sleep!")

meal_time()