# ----------------------------------
# Imports
# ----------------------------------
from tkinter import *
import json

# ----------------------------------
# Controller
# ----------------------------------
class MyController():
    def __init__(self, parent):
        self.parent = parent
        self.model = MyModel(self)
        self.view = MyView(self)

    def quitButtonPressed(self):
        self.parent.destroy()        

    def AnswerBtPress(self, no):
        self.model.checkAnswer(no)

    def increaseQuNo(self):
        if self.model.CurQuNo < self.model.getNumberOfQu():
            self.model.CurQuNo = self.model.CurQuNo + 1

    def decreaseQuNo(self):
        if self.model.CurQuNo > self.model.getNumberOfQu():
            self.model.CurQuNo = self.model.CurQuNo - 1

# ----------------------------------
# View
# ----------------------------------
class MyView():
    def __init__(self, ctrl):
        self.ctrl = ctrl
        self.frame=Frame()
        self.frame.grid(row = 0,column=0)
        
        self.qSet = self.ctrl.model.getQuSet(0)
        self.show()

    def show(self):

        #-------------------------------------------
        #
        #-------------------------------------------
        Label(self.frame
            ,text=self.qSet['frage']
            ).grid(row = 0, column = 0 , padx=10, pady=10, sticky='w')
        
        #-------------------------------------------
        #
        #-------------------------------------------
        Label(self.frame
            ,text=self.qSet['antworten'][0]['antwort']
            ).grid(row = 1, column = 0 , padx=10, pady=10, sticky='w')
        Button(self.frame
            ,text=" "
            ,command = lambda: self.ctrl.AnswerBtPress(1)
            ).grid(row = 1, column = 2, padx=10, pady=10)

        #-------------------------------------------
        #
        #-------------------------------------------
        Label(self.frame
            ,text=self.qSet['antworten'][1]['antwort']
            ).grid(row = 2, column = 0, padx=10, pady=10, sticky='w')
        Button(self.frame
            ,text=" "
            ,command = lambda: self.ctrl.AnswerBtPress(2)
            ).grid(row = 2, column = 2, padx=10, pady=10)

        #-------------------------------------------
        #
        #-------------------------------------------
        Label(self.frame
            ,text=self.qSet['antworten'][2]['antwort']
            ).grid(row = 3, column = 0, padx=10, pady=10, sticky='w')
        Button(self.frame
            ,text=" "
            ,command = lambda: self.ctrl.AnswerBtPress(3)
            ).grid(row = 3, column = 2, padx=10, pady=10)

        #-------------------------------------------
        #
        #-------------------------------------------
        Button(self.frame
            ,text = 'EXIT'
            ,command = self.ctrl.quitButtonPressed).grid(row = 5, column = 0, sticky='w')

        #-------------------------------------------
        #
        #-------------------------------------------
        Button(self.frame
            ,text = '<< BEFORE'
            ,command = self.ctrl.decreaseQuNo).grid(row = 5, column = 1)

        #-------------------------------------------
        #
        #-------------------------------------------
        Button(self.frame
            ,text = 'NEXT >>'
            ,command = self.ctrl.increaseQuNo).grid(row = 5, column = 2, sticky='w')

# ----------------------------------
# Model
# ----------------------------------
class MyModel():
    def __init__(self,ctrl):
        self.ctrl = ctrl 
        self.Data = None
        self.qSet = None
        self.CurQuNo = 0

        self.loadJSON('./Data/Fragen.json')
        self.getNumberOfQu()

    def loadJSON(self, fileP):
        with open(fileP, 'r') as f:
             self.Data = json.load(f)

    def checkAnswer(self, no):
        print(no)

    def getQuSet(self,qNo):
        return self.Data['Quiz'][qNo]

    def getNumberOfQu(self):
        return len(self.Data['Quiz'])

# ----------------------------------
# Main
# ----------------------------------
def main():
    root = Tk()
    frame = Frame(root)
    root.title('Quiz')
    app = MyController(root)
    root.mainloop()

if __name__ == '__main__':
    main()
