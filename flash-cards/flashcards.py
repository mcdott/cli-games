import json

# Open the data file and parse the JSON
with open('me-capitals.json', 'r') as file:
    data = json.load(file)
    
# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0

# Iterate over the questions from the cards array to get the users's input for each question
for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess == i["a"]:
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
    else:
        print(f"Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")

# End game message based on final score
if score == total:
    print(f"Perfect! Your final score was {score} out of {total}.")
elif score / total > 0.5:
    print(f"Good work! Your final score was {score} out of {total}.")
else:
    print(f"Keep practicing! Your final score was {score} out of {total}.")