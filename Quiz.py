question_dict={
    "Ques1":{"ques":"What is the capital of India?",
              "options":"A. Mumbai\nB. New Delhi\nC. Chennai\nD. Kolkata",
              "answer":"B"},

    "Ques2":{"ques":"Which keyword is used to define a function in Python?",
              "options":"A. function\nB. define\nC. def\nD. fun",
              "answer":"C"},

    "Ques3":{"ques":"Which data type is used to store multiple values in a single variable in Python?",
              "options":"A. int\nB. float\nC. list\nD. str",
              "answer":"C"},

    "Ques4":{"ques":"What will be the output of print(2 ** 3) in Python?",
              "options":"A. 6\nB. 8\nC. 9\nD. 23",
              "answer":"B"},

    "Ques5":{"ques":"Which symbol is used for comments in Python?",
              "options":"A. //\nB. <!-- -->\nC. #\nD. /* */",
              "answer":"C"},
}
Score=0



def Quiz():
    global Score
    print(f"\nMax Score={len(question_dict)}")
    print(f"Your Score={Score}")
    for i in range(1,len(question_dict)+1):
        print(f"\nQues{i}:{question_dict[f'Ques{i}']['ques']}\n")
        print(f"{question_dict[f'Ques{i}']['options']}\n")
        Ans=input("Answer=").strip().capitalize()
        if Ans==question_dict[f"Ques{i}"]["answer"]:
             print("\nCorrect Answer!")
             Score+=1
             print(f"Your Score={Score}")
        else:
             print("\nIncorrect Answer!")
             print(f"Your Score={Score}")
    print(f"Final Score={Score}\n")
    


def menu():
    global Score
    width=60
    welcome=["Welcome to Quiz Application!","Ready for a Quiz"]
    print("="*width)
    for line in welcome:
        print(f"{line:^{width}}")
    print("="*width)
    while True:
        user=input("A: Start Quiz\n" \
                "B: Exit\n" \
                "Enter the option=").strip().capitalize()
        if user=="A":
            Score=0
            Quiz()
        elif user=="B":
            break



menu()