# Check the score grade of students
stds_score = int (input("Input your score to check grade: "))
if stds_score <= 35:
    print ("Sorry you failed")
elif stds_score <= 40:
     print ("You got a weak pass")
elif stds_score <= 54:
    print ("You got a good pass")
elif stds_score <=59:
    print ("You got a C")
elif stds_score <=69:
    print ("You got a B")
elif stds_score <=100:
    print ("Congratulations, you are among the Valedictorians")
else:
    print("invalid selection, kindly input a valid score to continue")