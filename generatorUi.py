#third-party imports
import pyperclip
from tkinter import *
from tkinter import ttk

#local imports
import generator

class optionButtons(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # one checkbutton per argument

        #### variable definitions
        self.useSymbols = BooleanVar(self)
        self.useNumbers = BooleanVar(self)
        self.useLowercase = BooleanVar(self)

        #### button definitions ####
        symbolButton = Checkbutton(self, text = "Use symbols?", variable=self.useSymbols, onvalue=True, offvalue=False)
        numberButton = Checkbutton(self, text = "Use numbers?", variable = self.useNumbers, onvalue=True,offvalue=False)
        lowercaseButton = Checkbutton(self, text = "Use uppercase letters?", variable = self.useLowercase, onvalue=False, offvalue=True)

        #### widget placement ####
        symbolButton.grid(row = 0, column = 0)
        numberButton.grid(row = 0, column = 1)
        lowercaseButton.grid(row = 0, column = 2)

class generatorWindow(Tk):
    def __init__(self):
        super().__init__(className="Wan's Password Generator")

        #### variable definitions ####
        self.password = StringVar(self, "Click \"Generate Password\" to generate a password")
        self.dictionary = generator.readFile("dictionary.txt")

        #### widget definitions ####
        passwordTextBox = ttk.Label(self, textvariable=self.password)
        self.options = optionButtons(self)
        generatePasswordButton = ttk.Button(self, text="Generate password", command= lambda: self.generate())
        copyButton = ttk.Button(self, text="Copy password", command=self.copy())

        #### widget placement
        passwordTextBox.grid(column=0, row=0, columnspan=2)
        generatePasswordButton.grid(column=0, row=1)
        copyButton.grid(column=1, row = 1)
        self.options.grid(column = 0, row = 2, columnspan=2)

    def generate(self):
        self.password.set(generator.generatePassphrase(wordCount=4, wordList = self.dictionary, lowercase=self.options.useLowercase.get(), symbols=self.options.useSymbols.get(), numbers=self.options.useNumbers.get()))

    def copy(self):
        pyperclip.copy(self.password.get())

if __name__ == "__main__":
    #TODO: auto-find dictionary options
    root = generatorWindow()
    root.mainloop()