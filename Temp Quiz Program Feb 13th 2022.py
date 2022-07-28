import random
import time

def no_of_participants():
    while True:
        try:
            num = int(input("How many people are participating in this quiz? "))
            break
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")
    return num

def no_of_questions():
    while True:
        try:
            no_ques = int(input("How many questions you want to answer? "))
            break
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")
    return  no_ques

def select_category():
    while True:
        try:
            opt = int(input("Press 1 for questions from Science: \nPress 2 for questions from Technology: \nPress 3 for questions from Cricket: \nPress 4 for questions from Movies:\nPress 5 for questions from Mythology: \nPress 6 for questions from History:\nPress 7 for questions from All Categories: "))
            break
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")
    return opt

def science_category(list_q, list_a):
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\science quiz\\science_questions.txt", "r") as f9:
        list_q = f9.readlines()
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\science quiz\\science_answers.txt", "r") as f10:
        list_a = f10.readlines()
    return list_q, list_a

def technology_category(list_q, list_a):
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\technology quiz\\technology_questions.txt", "r") as f9:
        list_q = f9.readlines()
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\technology quiz\\technology_answers.txt", "r") as f10:
        list_a = f10.readlines()
    return list_q, list_a

def cricket_category(list_q, list_a):
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\cricket quiz\\cricket_questions.txt", "r") as f9:
        list_q = f9.readlines()
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\cricket quiz\\cricket_answers.txt", "r") as f10:
        list_a = f10.readlines()
    return list_q, list_a

def movies_category(list_q, list_a):
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\movies quiz\\movies_questions.txt", "r") as f9:
        list_q = f9.readlines()
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\movies quiz\\movies_answers.txt", "r") as f10:
        list_a = f10.readlines()
    return list_q, list_a

def mythology_category(list_q, list_a):
   with open("C:\\Users\\balan\\Desktop\\Minor Project\\mythology quiz\\mythology_questions.txt", "r") as f9:
        list_q = f9.readlines()
   with open("C:\\Users\\balan\\Desktop\\Minor Project\\mythology quiz\\mythology_answers.txt", "r") as f10:
        list_a = f10.readlines()
   return list_q, list_a

def history_category(list_q, list_a):
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\history quiz\\history_questions.txt", "r") as f9:
        list_q = f9.readlines()
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\history quiz\\history_answers.txt", "r") as f10:
        list_a = f10.readlines()
    return list_q, list_a

def mixed_category(list_q, list_a):
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\mixed quiz\\mixed_questions.txt", "r") as f9:
        list_q = f9.readlines()
    with open("C:\\Users\\balan\\Desktop\\Minor Project\\mixed quiz\\mixed_answers.txt", "r") as f10:
        list_a = f10.readlines()
    return list_q, list_a


def participant(num, name, len_q, no_ques):
    i = 0
    correct_ans = 0
    wrong_ans = 0
    total_ans = 0
    ques_list=[]
    ques_list=random.sample(range(0,len_q),no_ques)
    while i < no_ques:

            t1=time.time()
            answer = input(list_q[ques_list[i]])
            t2=time.time()

            if t2-t1>10:
                print("Sorry, you have exceeded the time limit. Correct answer is option "+list_a[ques_list[i]].rstrip().upper()+"!! Try the next question!!\n")
                i=i+1
                
            else:  
                if list_a[ques_list[i]].rstrip().upper() == answer.upper(): 
                    print("Correct answer!!")
                    correct_ans = correct_ans + 1
                else:
                    print("Wrong answer!! correct answer is "+list_a[ques_list[i]].rstrip().upper())
                    wrong_ans = wrong_ans + 1
            
                i = i + 1
                total_ans = correct_ans + wrong_ans
    print_scores(name, correct_ans)
    list_scores.append([name, correct_ans])
    i = i + 1


def print_scores(name, correct_ans):
    print(name.upper() + ", you have answered " + str(correct_ans) + " correctly")

def display_one_result(list_scores):
    for data in list_scores:
        print(str(data[0].upper())+"  "+str(data[1]))

def display_results(list_scores):
    print("Here are the results of the quiz competion:")
    print("NAME        SCORE")
    print("****************")
    for data in list_scores:
        #print(str(data[0].upper())+"    "+str(data[1]))
        print('{:<10s}{:>4s}'.format(data[0].upper(),str(data[1])))

    i = 0
    winner1_score = 0
    winner2_score=0
    winner1_name=""
    winner2_name=""
    no_of_winners=1
    
    while i < num:
        if (winner1_score < list_scores[i][1]):
            winner1_score = list_scores[i][1]
            winner1_name = list_scores[i][0]
        i = i + 1

  #To check if there is more than one winner with the same score
    i=0
    while i < num:
        if (winner1_score == list_scores[i][1]) and list_scores[i][0]!=winner1_name:
            winner2_name=list_scores[i][0]
            no_of_winners+=1
        i = i + 1

    if no_of_winners==1:
        print("                ")
        print(winner1_name.upper()+ " is the winner of this quiz with a score of " + str(winner1_score))
        print("Congratulations, "+winner1_name.upper()+"!")
    else:
        print("                ")
        print(winner1_name.upper() + " and "+winner2_name.upper()+ " are the  joint winners of this quiz with a score of "+str(winner1_score))
        print("Congratulations, "+winner1_name.upper()+" and "+winner2_name.upper()+"!")

#****************************
#The main program starts here
#****************************    
list_scores = []
list_a = []
list_q = []
print("Welcome to the quiz program!")

#Selecting the maximum number of participants allowed to participate in the Quiz competition
num=no_of_participants()
while num>10:
    print("Only 10 participants are allowed to participate. Try again")
    num=no_of_participants()

#Selecting the maximum number of questions a participant is allowed to answer
no_ques=no_of_questions()
while no_ques>10:
    print("The participant can choose a max of 10 questions. Try again")
    no_ques=no_of_questions()

#Selecting the quiz category among various options
opt=select_category()
while opt not in [1,2,3,4,5,6,7]:
    print("You have entered an invalid category number.Please enter a category number between 1 and 7")
    opt=select_category()

if opt == 1:
    list_q, list_a = science_category(list_q, list_a)
elif opt == 2:
    list_q, list_a = technology_category(list_q, list_a)
elif opt == 3:
    list_q, list_a = cricket_category(list_q, list_a)
elif opt == 4:
    list_q, list_a = movies_category(list_q, list_a)
elif opt==5:
    list_q, list_a = mythology_category(list_q, list_a)
elif opt==6:
    list_q, list_a = history_category(list_q, list_a)
elif opt==7:
    list_q, list_a = mixed_category(list_q, list_a)

#print(len(list_q))
len_q = len(list_q)
i = 0
if no_ques > len_q:
    print("You've entered invalid number of questions")
else:
    while i < num:
        name = input("Enter your name: ")
        participant(num, name, len_q, no_ques)
        i = i + 1

if num==1:
    display_one_result(list_scores)
else:
    display_results(list_scores)
