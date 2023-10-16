# Project1.py
# Author:


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game
# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
# the return value should be a boolean (True or False) for whether the user was correct

# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).

# Function to ask a question and check the answer



def ask_question(question, options, correct_answer):
    print(question)
    print("Options:")
    for i in range(len(options)):
        print(f"{chr(97 + i)}. {options[i]}")

    user_answer = input("Enter your answer (a, b, c, d): ").strip().lower()

    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong. The correct answer is {correct_answer}.\n")
        return False
def display_score(score):
    print(f"Your total score is: {score}")


def main():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions. Each correct answer is worth 1 point.\n")
    
    score = 0

    questions = [
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Venus", "Mars", "Saturn", "Jupiter"],
            "correct_answer": "d",
        },
        {
            "question": "Which gas do humans breathe in for respiration?",
            "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Methane"],
            "correct_answer": "b",
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["5", "6", "7", "8"],
            "correct_answer": "a",
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct_answer": "d",
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "correct_answer": "b",
        },
    ]

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            score += 1

    display_score(score)

if __name__ == "__main__":
    main()















