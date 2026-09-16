def meal_time():
    time = input("What time is it?")

    def convert(time):
         parts = time.split(":")
         hour = int(parts[0])
         minute = int(parts[1])
         time = hour + (minute / 60)
         time = float()
         if time > 6.5 and time < 11.5:
            print("Time for breakfast")
         elif time > 11.5 and time < 16.5:
            print("Time for lunch")
         elif time > 16.5 and time < 22.5:
            print("Time for dinner")
         elif time > 22.5 and time < 6.5: 
            print("Go back to sleep!")

meal_time()