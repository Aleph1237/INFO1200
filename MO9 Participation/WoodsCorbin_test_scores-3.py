#!/usr/bin/env python3

def display_welcome():     #welcome message with instructions
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    #list variable for the scores
    scores = [] 
    while True:
        score = input("Enter test score: ") #prompts user to enter scores, and collects imput
        if score == "x":
            return  scores   #if the user enters an x, the program returns the scores and calculations.
        else:
            score = int(score)
            if score >= 0 and score <= 100:   #dictates that score must be between 0 and 100
                scores.append(score)    #adds a new score to the list
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")    #error message if user enters a score higher than 100.

def process_scores(scores):
    #sorts the scores from low to high by default.
    scores.sort()

    #calculate the total scores
    total = 0
    for score in scores:
        total += score

    #find the number of scores
    numScores = len(scores)

    # calculate average score
    average = total / numScores

    #calculate lowest score
    lowScore = min(scores)

    #calculate high score
    highScore = max(scores)

    #median variable
    median = 0
    #calculate median score
    medScore = numScores // 2
    #checks if amount of list items is odd
    if numScores % 2 == 1:
        median = scores[medScore]
        #calculates median for even amount of items in list
    else:
        midOne = scores[medScore]
        midTwo = scores[medScore-1]
        median = (midOne + midTwo) / 2

    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", numScores) 
    print("Average Score:     ", average)
    print("Low Score:         ", lowScore)
    print("High Score:        ", highScore)
    print("Median Score:      ", median)

def main():
    display_welcome()
    #retrives the list the get_scores function
    scores = get_scores()
    #retieves and displays values for the provided list
    process_scores(scores)
    print("")
    print("Bye!") #exit message

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


