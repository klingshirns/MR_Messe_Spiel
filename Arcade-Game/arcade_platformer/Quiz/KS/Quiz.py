from tkinter import *
import json

# ----------------------------------
# Controller
# ----------------------------------

class Controller():
    def __init__(self, tk):
        self.tk = tk
        self.model = Model(self)
        self.view = View(self)

    def quitButtonPressed(self):
        self.tk.destroy()
    
    def answerButtonPressed(self, id):
        self.model.checkAnswer(id)

    def increaseQuestionNumber(self):
        pass

#----------------------------------
# View
#----------------------------------

class View():

    def __init__(self, Controller):
        
        self.controller = Controller
        self.frame = Frame()
        self.frame.grid(row=0, column=0)

        self.show()

        
    def show(self):
        pass
        #--------------------------
        # Question
        #--------------------------
        Label(self.frame, text="Frage", ).grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        #--------------------------
        # Answers + Buttons
        #--------------------------
        Label(self.frame,text="Answer 1").grid(row = 1, column = 0 , padx=10, pady=10, sticky='w')

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

        self.loadJSON()

    def loadJSON(self):

        file = open ("Data/quiz.json")
        quiz_data = json.load(file)
        file.close

        self.quiz_Data = quiz_data

    def checkAnswer(self, id_answered):

        if id_answered != (0 or 1 or 2):
            pass

        else:
            bool_answer = self.quiz_Data['general'][0]['answers'][id_answered]['truth']

            if bool_answer == True:

                print("correct")

            else:
                print("false")


#----------------------------------
# Main
#----------------------------------
def main():
    tk = Tk()
    frame = Frame(tk)
    tk.title('Quiz')
    Controller(tk)
    tk.mainloop()

if __name__ == "__main__":
    main()

