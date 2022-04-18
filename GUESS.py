print("Welcone to my computer quiz!")
print("COPYRIGHT @BLUE BIRD")

playing = input("Do you want to play the game : \n")

if playing.upper()!="YES":
    quit()

print("Okay Lets Get Started :)\n")

score = 0

#Q1
answer = input("What does CPU stands for- \n")

if answer.lower() == "central processing unit":
    score+=1

    print("Correct ! Lets go ")

else:
    print("Incorrect answer => correct answer is central processing unit !")

#Q2
answer = input("What does ALU stands for - \n")

if answer.lower() == "arithematic and logical unit":
     score+=1

     print("Correct ! Let's go ")

else:
    print("Incorrect answer => correct answer is arithematic and logical unit ! ")

#Q3
answer = input("What does GPU stands for - \n")

if answer.lower() == "graphics processing unit":
    score+=1

    print("Correct ! Lets go ")

else:
    print("Incorrect answer => correct answer is graphics processing unit !")

#Q4
answer = input("What does CU stands for - \n")

if answer.lower() == "control unit":
    score+=1

    print("Correct ! Lets go ")

else:
    print("Incorrect answer => correct answer is control unit !")

#Q5
answer = input("What does RAM stands for - \n")

if answer.lower() == "random access memory":
    score+=1

    print("Correct ! Lets go ")

else:
    print("Incorrect answer => correct answer is random access memory !")

 #Q6   
answer = input("What does ROM stands for - \n")
if answer.lower() == "read only memory":
    score+=1

    print("Correct ! Lets go ")

else:
    print("Incorrect answer => correct answer is read only memory !")

print(f"Good job ! You got {score} questions correct !\n")

print(f"Your score was {(score/6)*100}% \n")

print("Make sure to improve the code by adding more question to it or minimising the lines of code because that's what an actual programmer needs I guess !\n")
