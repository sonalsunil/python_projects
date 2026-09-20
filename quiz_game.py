#set methods
quiz=[
     {  "q":"What is the currency of Japan?",
        "opt":["yen","rupee","yuan","dollar"],
        "ans":1
     },
     {
        "q":"How many continents are there on Earth?",
        "opt":["5","6","7","8"],
        "ans":3
     },
     {
         "q":"Which language is primarily used to style web pages?",
         "opt":["Python","HTML","C++","css"],
         "ans":4
     },
     {
         "q":"What is the largest ocean on Earth?",
         "opt":["Atlantic Ocean","Indian Ocean","Arctic Ocean","pacific ocean"],
         "ans":4
     },
     {
         "q":"Which planet is known as the Red Planet?",
         "opt":["venus","mars","mercury","jupiter"],
         "ans":2
     } 
]
score=0
for i in quiz:
     print(i["q"])
     for number,opt in enumerate (i["opt"],start=1):
       print(number,'.',opt)
       
     response=int(input("enter the choice:"))
     if(response>=1 and response<=4):
       if(response== i["ans"]):
               score=score+1 
               print("correct")
       else:
              print("ans is wrong")
              print(i["opt"][i["ans"] - 1])
     else:
        print("invalid response")
print("quiz completed!")
print("score=",score,"/",len(quiz))
print("percentage=",(score/len(quiz))*100,"%") 

    
     


