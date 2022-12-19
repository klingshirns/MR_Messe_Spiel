from tkinter import *
import json

# ----------------------------------
# Controller
# ----------------------------------

class Controller():
    def __init__(self, root):
        self.root = root
        self.model = Model(self)
        self.view = View(self)

    def quitButtonPressed(self):
        self.root.destroy()
    
    def answerButtonPressed(self, id):
        self.model.checkAnswer(id)
        self.model.changeLabels()



#----------------------------------
# View
#----------------------------------

class View():

    def __init__(self, Controller):
        
        self.controller = Controller
        self.frame = Frame()
        self.frame.grid(row=0, column=0)
        self.questionString = self.controller.model.getQuestionString()

        self.show()

    def show(self):
        #--------------------------
        # Question
        #--------------------------
        self.question_label = Label(self.frame, text=self.questionString).grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        #--------------------------
        # Answers + Buttons
        #--------------------------
        self.question_label = Label(self.frame,text="Answer 1").grid(row = 1, column = 0 , padx=10, pady=10, sticky='w')

        Button(self.frame,text="a", command=lambda: self.controller.answerButtonPressed(0)).grid(row = 1, column = 2, padx=10, pady=10)

        #-------------------------
        Label(self.frame,text="Answer 2").grid(row = 2, column = 0 , padx=10, pady=10, sticky='w')

        Button(self.frame,text="b", command=lambda: self.controller.answerButtonPressed(1)).grid(row = 2, column = 2, padx=10, pady=10)

        #-------------------------
        Label(self.frame,text="Answer 3").grid(row = 3, column = 0 , padx=10, pady=10, sticky='w')

        Button(self.frame,text="c", command=lambda: self.controller.answerButtonPressed(2)).grid(row = 3, column = 2, padx=10, pady=10)

        
        #-------------------------
        # Buttons
        #-------------------------

        Button(self.frame, text="Exit", command=self.controller.quitButtonPressed).grid(row=5, column=0, sticky="w")


#----------------------------------
# Model
#----------------------------------

class Model():

    def __init__(self, Controller):
        self.quiz_Data = None
        self.currentQuNo = 0
        self.controller = Controller

        self.loadJSON()

    def loadJSON(self):

        file = open ("Data/quiz.json")
        quiz_data = json.load(file)
        file.close

        self.quiz_Data = quiz_data

    def checkAnswer(self, id_answered):

        myList = [0,1,2]

        if id_answered in myList:

            bool_answer = self.quiz_Data['general'][self.currentQuNo]['answers'][id_answered]['truth']

            if bool_answer == True:
                print("correct")
                # Richtig! Show true information
            else:
                print("false")
                # Falsch! Show true information

        self.increaseQuestionNumber()

    def getNumberOfQuestions(self):
        return len(self.quiz_Data['general'])

    def increaseQuestionNumber(self):
        # Get the Number of Questions listed in the JSON File
        numberOfQuestions = self.getNumberOfQuestions() 
        #Index starts at zero, but this return Value at one
        numberOfQuestions -= 1 

        if self.currentQuNo < numberOfQuestions:
            self.currentQuNo += 1
            print(self.currentQuNo)

        else:
            print("End of Quiz")
            self.controller.root.destroy()

    def getQuestionString(self):
        return str(self.quiz_Data['general'][self.currentQuNo]['Question'])

    def changeLabels(self):
        pass
        
#----------------------------------
# Main
#----------------------------------
def main():
    root = Tk()
    Frame(root)
    root.title('Quiz')
    Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()