import json

# Open the data file and parse the JSON
with open('me-capitals.json', 'r') as file:
    data = json.load(file)
    

# Iterate over the questions from the cards array to get the users's input for each question
for i in data["cards"]:
    guess = input(i["q"] + " > ")


# Check the user's input against the answer and display message to user
    if guess.lower() == i["a"].lower():
        print("Correct!")
    else:
        print("Incorrect! The correct answer is ", i["a"])

