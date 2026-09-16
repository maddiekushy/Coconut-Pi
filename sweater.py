t = int(input("What is the temperature?"))
if t > 60 and t < 100:
    print("You don't need a sweater.")
elif t >= 100:
    print("Way too hot for a sweater!")
elif t <= 32:
    print("Too cold for a sweater! You need a coat.")
else:
    print("You need a sweater.")