#music

print("Welcome to the Music Preferences Survey!")
print("Please answer the following questions:\n")

questions = [
    "What is your favorite music?",
    "Who is your favorite artist or band?",
    "Do you prefer listening to music at home or at concerts?",
    "What's your favorite song right now?"
]

while True:
    answers = []
    
    # Ask all questions
    for question in questions:
        answer = input(question + " ")
        answers.append(answer)
    
    # Display summary
    print("\nThank you for your answers!")
    print("Here's what you told us:")
    for i in range(len(questions)):
        print(f"{i+1}. {questions[i]}")
        print(f"   - {answers[i]}")
    
    # Ask if they want to take the survey again
    repeat = input("\nWould you like to take the survey again? (yes/no) ").lower()
    if repeat != 'yes':
        break

print("\nThank you for participating in our music survey!")