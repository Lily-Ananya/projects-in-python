print("welcome to my computer quiz !")

playing = input("Do you want to play ??")

if playing != "yes":
    quit()

print("Okay ! let's play :")    
score=0
#question  no 1.
answer=input("what does HTML stand for ?? ")
if answer.lower() == "hypertext markup language":
    print("correct !!")
    score +=1
else:
    print("incorrect")

#question  no 2.
answer=input("what does OSI stand for ?? ")
if answer.lower() == "open system interconnection ":
    print("correct !!")
    score +=1
else:
    print("incorrect")


#question  no 3.
answer=input("what does API stand for ?? ")
if answer.lower() == "application programming interface ":
    print("correct !!")
    score +=1
else:
    print("incorrect")


#question  no 4.
answer=input("what does DSA stand for ?? ")
if answer.lower() == "data structure and algorithm":
    print("correct !!")
    score +=1
else:
    print("incorrect")


#question  no 5.
answer=input("what does URL stand for ?? ")
if answer.lower() == "uniform resource locator":
    print("correct !!")
    score +=1
else:
    print("incorrect")

    
print("you got " + str(score) + "question correct !")
print("you got " + str((score/5)*100)+ " %.")
                     