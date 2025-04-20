# Messages
question = "What do you want? "
funny_story = funny_story = "Here is a joke for you! Saira was going to the market. Her programmer friend said, 'Buy one liter of milk, and if they have eggs, buy a dozen.' Sophia came back with 13 liters of milk. When asked why, she replied, 'Because they had eggs!'"
not_allowed = "Sorry I only tell jokes."

# Main function
def tell_joke():
    answer = input(question)
    answer = answer.strip().lower()

    if "joke" in answer:
        print(funny_story)
    else:
        print(not_allowed)

# Run the program
tell_joke()
