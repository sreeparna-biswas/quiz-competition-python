import random
import math
class Quiz: 
    def __init__(self,ques_bank):
        self.ques_bank=ques_bank
        self.ques_no=0
        self.score=0
 
    def Check_answer(self):
        user_ans=input("\tPlease give your answer in True/False: ")
        act_ans=self.ques_bank[self.ques_no]['correct_answer']

        if str(user_ans.lower())==str(act_ans):
            self.score=self.score+1
            print("\tYou have given Correct Answer.")
            print(f"\tYour Current Score is: {self.score}/{10}")
        else:
            self.score=self.score-0.5
            print("\tYou have given Wrong Answer.")
            print(f"\tYour Current Score is: {self.score}/{10}")

    def Next_question(self):
        #if(self.ques_no<len(question)):
        j=0
        self.Shuffle_ques()
        for i in range(1,11):
            self.ques_no=list2[j]
            print()
            print(f"{i}. ",end='')
            print(self.ques_bank[self.ques_no]['question'])
            self.Check_answer()
            j=j+1


    def Cleared_test(self):
        if math.ceil(self.score)>=4:
            print("You have Passed the quiz")
        else:
            print("You have failed the quiz")

    
    def Shuffle_ques(self):
        global list2
        print()
        list1=range(1,15)
        list2=[]
        rand_ques=random.choice(list1)
        k=1
        while(True):
            if k>10:
                break
            else:
                if rand_ques not in list2:
                    list2.append(rand_ques)
                    k=k+1
                else:
                    rand_ques=random.choice(list1)
        
        #print(list2)
        
        