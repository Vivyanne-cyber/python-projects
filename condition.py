#check for the eligibility status of a user
name = input("Hello" + "," + " "+ "Welcome" + "," + " " + "kindly tell us your name?" + " ")
print ("Nice to have you" +  " " + name + "," + "but before moving ahead" + "," "we would love to confirm your eligibility status")
age = int (input("How old are you?" + " "))
if age <= 30:
    print ("Welcome onboard" + "," + "na your type we want")
else:
    print ("Nah!!" "," + " " + "not allowed here" + ";" + " " "check the next building for your spec")    