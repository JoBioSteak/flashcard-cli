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


        