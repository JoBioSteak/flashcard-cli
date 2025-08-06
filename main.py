import tkinter as tk

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
skipped_cards = []
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


#make class when I need more than one window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.current_card = 0
        self.user_score = 0
        self.flashcards = flashcards
        self.skipped = skipped_cards

        #top frame
        top_frame = tk.Frame(self, bg="#ea9eff")
        top_frame.pack(pady=20)

        self.question_label = tk.Label(top_frame, text="", background="#fffb04", font=("Helvetica", 16), wraplength=600)
        self.question_label.pack()

        self.feedback_label = tk.Label(top_frame, text="", background="#777777", font=("Arial", 12))
        self.feedback_label.pack(pady=5)

        #middle frame
        middle_frame = tk.Frame(self, bg="#ea9eff")
        middle_frame.pack(pady=10)

        self.answer_entry = tk.Entry(middle_frame, background="#DCC8FE", width=40, font=("Arial", 12))
        self.answer_entry.pack(side="left", padx=5)

        self.submit_button = tk.Button(middle_frame, text="Submit", command=self.submit_answer, background="#838383")
        self.submit_button.pack(side="left", padx=5)

        self.skip_button = tk.Button(middle_frame, text="Skip", command=self.skip_card, background="#2F7B15")
        self.skip_button.pack(side="left", padx=5)

        #bottom frame
        bottom_frame = tk.Frame(self, bg="#ea9eff")
        bottom_frame.pack(pady=30)

        self.score_label = tk.Label(bottom_frame, text="Score: 0", background="#04c5ff", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.retry_button = tk.Button(bottom_frame, text="Redo", command=self.redo_skipped, background="#ff8000")
        self.retry_button.pack(pady=5)

        self.end_button = tk.Button(bottom_frame, text="End Session", command=self.end_session, background="#ff0000")
        self.end_button.pack(pady=5)

        self.show_question()
        
        
    def submit_answer(self):
        self.submit_button.config(state="normal")
        self.skip_button.config(state="normal")
        user_answer =  self.answer_entry.get()
        correct_answer = self.flashcards[self.current_card].getanswer()
        score = self.flashcards[self.current_card].getscore()
        Ua = nlp(user_answer)
        Ca = nlp(correct_answer)
        if Ua.similarity(Ca) >= 0.75:
            self.user_score += score
            self.score_label.config(text=f"Score: {self.user_score}")
            self.feedback_label.config(text= "That is correct!")
            self.current_card += 1
        else:
            self.feedback_label.config(text= "That is incorrect!")
            score -= 1
        self.answer_entry.delete(0,tk.END)
        self.show_question()
            
                
           
    def skip_card(self):
        skipped_cards.append(self.flashcards[self.current_card])
        self.current_card += 1
        self.answer_entry.delete(0,tk.END)
        self.show_question()
    
    def redo_skipped(self):
        if self.current_card > len(self.flashcards) and len(skipped_cards) > 0:
            self.flashcards = skipped_cards
            self.show_question()
        else:
            self.feedback_label.config(text="You can only redo skipped questions as the end of the quiz.")
        
            
        
    
    def end_session(self):
        self.question_label.config(text="Quiz complete! Good luck studying!")
        self.submit_button.config(state="disabled")
        self.skip_button.config(state="disabled")
        self.feedback_label.config(text="")
        self.retry_button.config(state="disabled")
       
    
    def show_question(self):
        if self.current_card < len(self.flashcards):
            self.question_label.config(text=self.flashcards[self.current_card].getquestion())
        else:
            self.question_label.config(text="Quiz complete!")
            self.submit_button.config(state="disabled")
            self.skip_button.config(state="disabled")
        
        

     
#setting up main window
main_w = App()
main_w.title('CogniHelp')
main_w.configure(background="#ea9eff")



#centering window on launch
main_w.geometry('600x600')
window_height = 500
window_width = 900
screen_width = main_w.winfo_screenwidth()
screen_height = main_w.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
main_w.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


main_w.mainloop()






