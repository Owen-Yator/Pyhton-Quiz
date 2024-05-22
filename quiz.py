questions = [
    {
        "prompt": "What is the capital of France?",
        "Options": ["A. Paris", "B. London", "C. Berlin"],
        "Answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Berlin?",
        "Options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "Answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "Options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "Answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["Options"]:
            print(option)
        answer = input("Enter your answer (A,B,C,D): ").strip().upper()
        if answer == question["Answer"]:
            print("Correct, hooray!!\n")
            score += 1
        else:
            print("Wrong, the correct answer is", question["Answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)