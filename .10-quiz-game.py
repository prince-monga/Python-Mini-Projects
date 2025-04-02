# Quiz Game 

# Dictionary of questions and answers
quiz_questions = {
    "What is the capital of India?": ["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Hyderabad"],
    "Which language is used for web development?": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
    "What is 5 + 3?": ["A. 7", "B. 8", "C. 9", "D. 10"],
    "Which planet is known as the Red Planet?": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"]
}

# Correct answers dictionary
correct_answers = {
    "What is the capital of India?": "C",
    "Which language is used for web development?": "C",
    "What is 5 + 3?": "B",
    "Which planet is known as the Red Planet?": "C"
}

score = 0  # Initialize score

# Loop through questions
for question, options in quiz_questions.items():
    print("\n" + question)  # Print question
    for option in options:
        print(option)  # Print answer choices
    
    # Get user input
    answer = input("Enter Your Answer (A, B, C, D): ").upper()

    # Check correctness
    if answer == correct_answers[question]:  # Use question key here
        print("Correct!")
        score += 1
    else:
        print(f" Wrong! The correct answer is {correct_answers[question]}.")

# Show final score
print("\nQuiz Completed!")
print(f" Your final score: {score}/{len(quiz_questions)}")
