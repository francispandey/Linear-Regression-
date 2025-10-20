import random 

guess=False
count=0
while True:
 random_int=random.randint(1,5)
 while guess==False:
       z=int(input("enter the number:"))
       if z==random_int:
        
        print(f"Congratulations the number was {random_int}")
        break
       else:
        count=count+1
 print(f"{count} is the number of attempts it took for you")
 z=input("do you wish to continue?[Y/n]")
 if z!="Y":
   break
 else:
   count=0
   

    