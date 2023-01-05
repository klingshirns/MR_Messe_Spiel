from tkinter import *
from tkinter.ttk import *
import json

# ----------------------------------
# Controller
# ----------------------------------

class Controller():
    def __init__(self, root):
        self.root = root
        self.model = Model(self)
        self.view = View(self)
        self.quiz_end = False
    
    def answerButtonPressed(self, id):
        result_condition_bool = self.model.checkAnswer(id)

        self.view.clearFrame()
        self.view.loadResultView(result_condition_bool)

    def question_view(self):
        self.view.clearFrame()
        self.view.setLabelText()
        self.view.loadView()

    def endOfQuiz(self, score, maxScore):
        self.view.clearFrame()
        self.view.loadEndOfQuiz(score, maxScore)

    def quitButtonPressed(self):
        self.root.destroy()


#----------------------------------
# View
#----------------------------------

class View():

    def __init__(self, Controller):
        
        self.controller = Controller
        self.frame = Frame()
        self.style = Style()
        self.frame.grid(row=0, column=0)

        self.controller.root.geometry('600x275')

        #------------------------------------------
        #Variables for Questions and Answers (need to be changed)

        self.Question_text = StringVar()
        self.Aw1_text = StringVar()
        self.Aw2_text = StringVar()
        self.Aw3_text = StringVar()

        self.result_text = StringVar()

        self.result_info_text = StringVar()

        #-----------------------------------------
        # Style Buttons and Labels
        self.styleWidgets()

        #------------------------------------------
        # Load all the Buttons, Labels, ...
        self.loadView()

        #----------------------------------------------------------------------
        # Set the Label texts, e.g. Questions, Answers for the first time
        self.setLabelText()



    def loadView(self):

        #-------------------------
        #Configure Grid
        #-------------------------

        self.frame.columnconfigure(0, minsize=150)
        self.frame.columnconfigure(1, minsize=450)

        #--------------------------
        # Question
        #--------------------------

        self.question_label = Label(self.frame, textvariable=self.Question_text, style='Qu.TLabel').grid(row=0, column= 0, columnspan=2)
        
        #--------------------------
        # Answers + Buttons
        #--------------------------

        Button(self.frame,text="a", command=lambda: self.controller.answerButtonPressed(0), style='Aw.TButton').grid(row=1, column=0, sticky= 'w', padx=10, pady=15)
        Label(self.frame,textvariable= self.Aw1_text, style= 'Aw.TLabel').grid(row = 1, column=1, sticky='w')


        #-------------------------
        Button(self.frame,text="b", command=lambda: self.controller.answerButtonPressed(1), style='Aw.TButton').grid(row = 2, column=0, sticky= 'w', padx=10, pady=15)
        Label(self.frame,textvariable= self.Aw2_text, style= 'Aw.TLabel').grid(row = 2, column=1, sticky= 'w')

        #-------------------------
        Button(self.frame,text="c", command=lambda: self.controller.answerButtonPressed(2), style='Aw.TButton').grid(row = 3, column=0, sticky= 'w', padx=10, pady=15)
        Label(self.frame,textvariable= self.Aw3_text, style= 'Aw.TLabel').grid(row = 3, column=1, sticky = 'w')

    
    def loadResultView(self, result_condition_bool):

        self.styleWidgets()

        if result_condition_bool:
            Label(self.frame, text = 'Richtig', style = 'ResultTrue.TLabel').grid(row=0, padx= 250, pady= 20)
        else:
            Label(self.frame, text = 'Falsch', style = 'ResultFalse.TLabel').grid(row=0, padx= 250, pady= 20)

        Label(self.frame, textvariable = self.result_info_text, style = 'ResultInfo.TLabel', wraplength= 400).grid(row = 1)

        Button(self.frame, text="Weiter", command=self.controller.model.increaseQuestionNumber).grid(row=2, sticky= 'e', padx= 10, pady= 40)

    

    def loadEndOfQuiz(self, intScore, intMaxScore):

        self.styleWidgets()

        score = str(intScore)
        maxScore = str(intMaxScore)

        scoreDisplay = "Du hast von " + maxScore + " möglichen Punkten " + score + " Punkte erreicht"
        
        Label(self.frame, text="Quiz Ende!", style = 'End.TLabel').grid(row=0, padx= 220, pady=20)
        Label(self.frame, text=scoreDisplay, style = 'Score.TLabel') .grid(row=1, pady=20)

        Button(self.frame, text="OK", command=self.controller.quitButtonPressed).grid(row=2, sticky= 'e')

    def clearFrame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    #----------------------------
    # Function to change the label texts

    def setLabelText(self):

        # Current Question Number
        currentQuNo = self.controller.model.currentQuNo

        # All Quiz information from JSON
        quiz_Data = self.controller.model.quiz_Data

        # Set Question text
        self.Question_text.set(quiz_Data['general'][currentQuNo]['Question'].encode('utf-8'))

        # Set Answer texts
        self.Aw1_text.set(quiz_Data['general'][currentQuNo]['answers'][0]['Answer'])
        self.Aw2_text.set(quiz_Data['general'][currentQuNo]['answers'][1]['Answer'])
        self.Aw3_text.set(quiz_Data['general'][currentQuNo]['answers'][2]['Answer'])

        # Set Result Info Text
        self.result_info_text.set(quiz_Data['general'][currentQuNo]["answer_info"])

    def styleWidgets(self):
        
        #---------------------------
        # Question label
        self.style.configure('Qu.TLabel', font = ('Arial', 14, 'bold'), foreground='black', padding=20)

        #---------------------------
        # Answer Buttons
        self.style.configure('Aw.TButton', font = ('Arial', 12), foreground = 'black')
        self.style.map('Aw.TButton',
                        background=[ ('!active','Black'),('active', 'blue')]
                        )

        #--------------------------
        # Answer Labels
        self.style.configure('Aw.TLabel', font = ('Arial', 12, 'bold'))

        #--------------------------
        # Label End Of Quiz
        self.style.configure('End.TLabel', font=("Arial", 22), foreground='royal blue')
        self.style.configure('Score.TLabel', font= ('Arial', 14), foreground = 'black')

        #-----------------------------
        # Result Label
        self.style.configure('ResultFalse.TLabel', font = ('Arial', 22), foreground='red') 
        self.style.configure('ResultTrue.TLabel', font = ('Arial', 22), foreground='green') 

        #-----------------------------
        # Result Info Text
        self.style.configure('ResultInfo.TLabel', font = ('Arial', 16), foreground = 'black')
        

#----------------------------------
# Model
#----------------------------------

class Model():

    def __init__(self, Controller):
        self.quiz_Data = None
        self.currentQuNo = 0
        self.controller = Controller
        self.score = 0
        self.maxScore = 0

        self.loadJSON()
        self.getNumberOfQuestions()

    def loadJSON(self):

        file = open ("../json/Quiz.json")
        quiz_data = json.load(file)
        file.close

        self.quiz_Data = quiz_data

    def checkAnswer(self, id_answered):

        myList = [0,1,2]

        if id_answered in myList:

            bool_answer = self.quiz_Data['general'][self.currentQuNo]['answers'][id_answered]['truth']

            if bool_answer == True:
                
                self.score += 1
                return True
            else:
                return False

        

    def getNumberOfQuestions(self):
        
        numberOfQuestions = len(self.quiz_Data['general'])

        self.maxScore = numberOfQuestions

        return numberOfQuestions

    def increaseQuestionNumber(self):
        # Get the Number of Questions listed in the JSON File
        numberOfQuestions = self.getNumberOfQuestions() 
        #Index starts at zero, but this return Value at one
        numberOfQuestions -= 1 

        if self.currentQuNo < numberOfQuestions:
            self.currentQuNo += 1
            
            self.controller.question_view()

        else:
            self.controller.endOfQuiz(self.score, self.maxScore)



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