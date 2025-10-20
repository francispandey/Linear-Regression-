def temp(a):
    if a=="F":
        f=int(input("Enter the temperatue:"))
        c=(f-32)*(5/9)
        print(f"In Fahrenheit {f} In Celsius {c}")
        
    else:
        c=int(input("enter the temperature:"))
        f=(c*(9/5)+32)
        print(f"In Fahrenheit {f} In Celsius {c}")
a=input("Enter the unit: ")
temp(a)
    