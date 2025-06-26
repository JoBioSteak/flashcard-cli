class flashcard:
    def _init_(self, questionP,answerP,scoreP):
        self.question = questionP
        self.answer = answerP
        self.score = scoreP
    
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
        with open('flashcard.csv') as file:
            
    
    except IOError:
        print("File was not found")
        