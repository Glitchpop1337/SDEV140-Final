# This is a start window, which is used to open the second, main script on demand.
from tkinter import * # import all tkinter
import pygame # import pygame (a python game dev module which I used to play the audio)
from subprocess import call # import to call to the main.py script

root = Tk() # creating the window
root.title("D&D 5E Simplified Character creator.") # assigning the title
root.geometry("640x360") # assigning the window default size
pygame.mixer.init() # initializing pygame mixer

bg = PhotoImage(file="background.png") # assigning a background image
imgLabel = Label(root, image=bg) # creating a label for image
imgLabel.place(x=0, y=0, relwidth=1, relheight=1) # placing label
# set of 3 labels to display the main message
introLabel = Label(text="Hello and welcome!"
                   , font=('Times', 15))
introLabel.pack()
introLabel2 = Label(text="This application will help you"
                              " easily make a simplified version of a D&D 5E Character",
                   font=('Times', 15))
introLabel2.pack()
introLabel3 = Label(text="(limited races and classes)!"
                   ,font=('Times', 15))
introLabel3.pack()


class Buttons: # making a class for buttons

    def __init__(self, master): # init the class
        frame = Frame(master)
        frame.pack()
        # start button that calls to the open_main function on press
        self.startButton = Button(frame, text="Start", font=('Times', 25), height=2, width=5, command=self.open_main)
        self.startButton.pack()
        # music play button that calls to the play function
        self.bardStartButton = Button(frame, text="Tell the bard to play some tunes!", font=('Times', 10), command=self.play)
        self.bardStartButton.pack()
        # music stop button that calls to the stop function
        self.shutUpBardButton = Button(frame, text="In case the bard gets too annoying. (stops music)",
                                  font=('Times', 10), command=self.stop)
        self.shutUpBardButton.pack()
    # play function using pygame mixer to load and play an mp.3 file
    def play(self):
        pygame.mixer.music.load("AroundTheFire.mp3") # loading the file
        pygame.mixer.music.play(loops=30) # play the file set it to loop 30 times
    # stop function using pygame mixer
    def stop(self):
        pygame.mixer.music.stop() # stops the mp3 file playback
    # function to call to main.py script
    def open_main(self):
        call(["python", "main.py"])

b = Buttons(root) # calling the class

root.mainloop() # tkinter main loop