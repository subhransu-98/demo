# kbc questions and answer
# import time # for use of sleep

def kbc_quiz():
    print("Welcome to KBC - Kaun Banega Crorepati!")
  
    
    question = "What is the capital of France?"
    options = ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"]
    correct_answer = "C"
    
    print("\nQuestion:")
    print(question)
    print("\nOptions:")
    for option in options:
        print(option)
    
    user_answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()
    #strip() use for take input except space/tab/any white space
    
    if user_answer == correct_answer:
        print("\nCongratulations! That's the correct answer!")
    else:
        print("\nSorry, that's incorrect. The correct answer is", correct_answer)

kbc_quiz()
