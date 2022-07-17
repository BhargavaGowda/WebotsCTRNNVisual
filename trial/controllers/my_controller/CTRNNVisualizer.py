import threading
import tkinter as tk
import tkinter.ttk as ttk
import PyCTRNN

class BrainVision:

    def __init__(self, brain:PyCTRNN.CTRNN):
        self.brain = brain
        
        self.neuronList = []
        t1 = threading.Thread(target=self.setUp)
        t1.start()
        


    def setUp(self):
        self.brainWindow = tk.Tk()
        mainBrainFrame = tk.Frame(master=self.brainWindow, width=200,height=200,bg="grey")
        mainBrainFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        mainBrainFrame.columnconfigure(0, weight=1, minsize=75)
        mainBrainFrame.columnconfigure(1, weight=1, minsize=75)
        mainBrainFrame.columnconfigure(2, weight=1, minsize=75)

        for i in range(self.brain.size):
            frame = tk.Frame(master=mainBrainFrame,relief=tk.RAISED,borderwidth=2,bg="red")
            label = tk.Label(master=frame,text=self.brain.getPotentials()[i])
            frame.grid(row=i//3, column=i%3, padx=5, pady=5)
            label.pack(padx=5,pady=5)
            self.neuronList.append([label,frame])

        self.brainWindow.mainloop()            

    def updateNeurons(self):
        for i in range(len(self.neuronList)):
            self.neuronList[i][0]["text"] = 1#round(self.brain.getPotentials()[i])

            


        


