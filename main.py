from quiz import Quiz
from question_bank import questions
q=Quiz(questions)
print(r"""
             _     
            (_)    
  __ _ _   _ _ ____
 / _` | | | | |_  /
| (_| | |_| | |/ / 
 \__, |\__,_|_/___|
    | |            
    |_|        
          """)
nam=input("Enter your name: ")
print(f"Welcome {nam} to the quiz, All the Best!!")
print()
#for h in range(11):
q.Next_question()

print()
print("======================================================")
print()
print(f"Thank you for playing. Your final score is: {q.score}/{10}")
print()
q.Cleared_test()
print()
        

    
    









