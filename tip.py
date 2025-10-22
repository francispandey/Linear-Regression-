questions=["Capital of Nepal","Capital Of india","Capital Of japan"]
Answers=["Ktm","delhi","Tokyo"]
answer=[]
k=0
points=0
for i in questions:
    print(i)
    j=input("Enter the answer:")
    answer.append(j)
    if answer[k]==Answers[k]:
        print("Correct answer")
        points+=10

    else:
        print("Incorrect Answer")
    k+=1
print(f"the total points are {points}")
    
