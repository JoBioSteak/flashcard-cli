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
    
    
import csv
flashcards = []
def loadflashcards():
    try:
        with open('flashcard.csv','r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                q = row["Question"]
                a = row["Answer"]
                s = row["Score"]
                flashcards.append(Flashcard(q,a,s)) 
    except IOError:
        print("File was not found")
        return
    
    
loadflashcards()
import random
random.shuffle(flashcards)

quit_flag = False
user_score = 0

print("Press q to end the session or s to skip a card")
while not quit_flag:
    for card in flashcards:
        while True:
            print(card.getquestion())
            answer = input().strip().lower()
            
            if answer == card.getanswer().strip().lower():
                user_score += card.getscore()
                print("Correct! Your current score is:", user_score)
                break  # move to next card
            
            elif answer == 'q':
                quit_flag = True
                break
            
            elif answer == 's':
                print("Skipped! The answer was", card.getanswer())
                print("Current score is:", user_score)
                break
            
            else:
                card.attempts += 1
                card.score = max(card.score - 1, 0)
                print("Wrong answer. Try again, or type 's' to skip, 'q' to quit.")
        
        if quit_flag:
            break

    
print("That's the end!! Your final score is ", user_score)
        