#!/usr/bin/env python3

print("Corbin Woods's Test Scores App") #prints first welcome message

# display a welcome message
print("The Test Scores Program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
score1 = int(input("Enter test score: ")) # user enters first score
score2 = int(input("Enter test score: ")) # user enters second score
score3 = int(input("Enter test score: ")) # user enters third score

# calculate total score
total_score = score1 + score2 + score3

# calculate average score
average_score = round(total_score / 3)
             
# format and display the results
print("======================")
print("Your Scores:", score1 , score2 , score3)
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye")


