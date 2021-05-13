class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts= [
    "Question1?\n(a)\n(b)\n(c)\n(d)\n",
    "Question2?\n(a)\n(b)\n(c)\n(d)\n",
    "Question3?\n(a)\n(b)\n(c)\n(d)\n",
    "Question4?\n(a)\n(b)\n(c)\n(d)\n",
    "Question5?\n(a)\n(b)\n(c)\n(d)\n"
]

question_prompts
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "a"),
]

def run_test(questions):
    score =0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))
    if score >= 3:
        print("Congragulations, you passed the test")
    elif score < 3:
        print("Sorry you failed")
    else:
        print("Sorry, error from our side. We will try to fix it")

run_test(questions)    
    
        
