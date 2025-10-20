import time

timestamp=(time.strftime("%H:%M"))
a=int(time.strftime("%H"))
if a>12 and a<17 :
    print(f"The current time is {timestamp}, Good afternoon!")
elif a>17 or a==17:
    print(f"the current time is {timestamp},good evenining!")
else:
    print("goodmorning!")

    