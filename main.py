import tkinter as tk
#make class in case i need more than one window
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #creating all the widgets
        self.current_card = 0
        self.user_score = 0
        self.question_label = tk.Label(self,text="")
        self.answer_entry = tk.Entry(self)
        self.submit_button = tk.Button(self,text="Submit",command=self.submit_answer)
        self.skip_button = tk.Button(self,text="Skip",command = self.skip_card)
        self.score_label = tk.Label(self,text="Socre: 0")
        
        #organising them so they look pretty pretty
        self.question_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.answer_entry.grid(row=1, column=0, columnspan=2, pady=10)
        self.submit_button.grid(row=2, column=0, padx=5, pady=10)
        self.skip_button.grid(row=2, column=1, padx=5, pady=10)
        self.score_label.grid(row=3, column=0, columnspan=2, pady=10)
               
    def submit_answer(self):
        pass
           
    def skip_card(self):
        pass
    
    
    
        
    
main_w = App()
main_w.attributes('-fullscreen',True)

main_w.mainloop()


class Flashcard:
    def __init__(self, questionP,answerP,scoreP):
        self.question = questionP
        self.answer = answerP
        self.score = int(scoreP.strip())
        self.attempts = 0
    
    def getquestion(self):
        return self.question
    def getanswer(self):
        return self.answer
    def getscore(self):
        return self.score
    
    
import json
flashcards = []
def loadflashcards():
    try:
        with open('flashcard.json','r') as jsonfile:
            json_reader = json.load(jsonfile)
            for row in json_reader:
                q = row["Question"]
                a = row["Answer"]
                s = row["Score"]
                flashcards.append(Flashcard(q,a,s)) 
    except IOError:
        print("File was not found")
        return
    
    
import spacy
nlp = spacy.load("en_core_web_lg")

    
loadflashcards()
import random
random.shuffle(flashcards)

user_score = 0



def quiz(set,user_score):
    quit_flag = False
    cards_skipped = 0
    cards_won = 0
    skipped = []
    
    print("Press q to end the session or s to skip a card")
    for card in set:
        while True:
            correct_answer = card.getanswer().strip().lower()
            print(card.getquestion())
            answer = input().strip().lower()
            
            Ua = nlp(answer)
            Ca = nlp(correct_answer)
            
            if Ua.similarity(Ca) >= 0.75:
                user_score += card.getscore()
                print("Correct! Your current score is:", user_score)
                cards_won += 1
                break  
            
            elif answer == 'q': 
                quit_flag = True
                break
            
            elif answer == 's':
                print("Skipped! The answer was", card.getanswer())
                print("Current score is:", user_score)
                cards_skipped += 1
                skipped.append(card)
                break
            
            else:
                card.attempts += 1
                card.score = max(card.score - 1, 0)
                print("Wrong answer. Try again, or type 's' to skip, 'q' to quit.")
        
            if quit_flag:
                break
            
        if quit_flag:
            break
        
    return user_score, cards_won, cards_skipped, skipped

user_score, cards_won, cards_skipped,skipped = quiz(flashcards,user_score)    

while cards_skipped > 0:
        redo = input("Redo skipped cards? y/n: ").strip().lower()
        if redo == 'n':
            print("Thanks for using this app!")
            break
        elif redo == 'y':
            user_score, cards_won, cards_skipped, skipped = quiz(skipped, user_score)
            break
        else:
            print("Invalid input, please type y or n.")
            
print("That's the end!! Your final score is ", user_score)
print("You got",cards_won,"cards correct while skipping",cards_skipped,"cards.")



