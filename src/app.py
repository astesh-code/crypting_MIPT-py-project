### work via GUI ###

import tkinter as tk
import src.launcher as launcher

class Arg():
    """set of launch parameters"""
    key = None
    out = None
    inp = None
    mode = None
    scr = None

class App():
    """GUI main class"""
    def __init__(self):
        """create new app window"""
        self.window = tk.Tk()
        self.inpu = tk.StringVar()
        self.outpu = tk.StringVar()
        self.keyp = tk.StringVar()
        self.ar = Arg()
        self.code_type = tk.IntVar()
        self.window.title("CodeIt")
        self.window.geometry('380x110')
        self.interface()

    def code(self):
        """launch module as coder"""
        self.change()
        self.ar.mode = 'c'
        self.ar.inp = self.inpu.get()
        self.ar.out = self.outpu.get()
        self.ar.key = self.keyp.get()
        launcher.use(self.ar)

    def decode(self):
        """launch module as decoder"""
        self.change()
        self.ar.mode = 'd'
        self.ar.inp = self.inpu.get()
        self.ar.out = self.outpu.get()
        self.ar.key = self.keyp.get()
        launcher.use(self.ar)

    def hack(self):
        """lauch module in hacking mode"""
        self.change()
        self.ar.mode = 'h'
        self.ar.inp = self.inpu.get()
        self.ar.out = self.outpu.get()
        self.ar.key = self.keyp.get()
        launcher.use(self.ar)

    def change(self):
        """change code script by click"""
        if self.code_type.get() == 0:
            self.ar.scr = 'caesar'
        elif self.code_type.get() == 1:
            self.ar.scr = 'vigenere'
        elif self.code_type.get() == 2:
            self.ar.scr = 'vernam'

    def grid_create(self):
        """GUI grid creating"""
        col = 0
        self.inl.grid(column=col, row=0)
        self.oul.grid(column=col, row=1)
        self.kl.grid(column=col, row=2)
        col+=1
        self.in_file.grid(column=col, row=0)
        self.out_file.grid(column=col, row=1)
        self.key_file.grid(column=col, row=2)
        col+=1
        self.caesar.grid(column=col, row=0)
        self.vernam.grid(column=col, row=2)
        self.vegenere.grid(column=col, row=1)
        col+=1
        self.btn_hack.grid(column=col, row=2)
        self.btn_code.grid(column=col, row=0)
        self.btn_decode.grid(column=col, row=1)

    def interface(self):
        """GUI init function"""
        self.code_type.set(0)
        self.caesar = tk.Radiobutton(text="Caesar",
                                     variable=self.code_type, value=0)
        self.vegenere = tk.Radiobutton(text="Vigenere",
                                       variable=self.code_type, value=1)
        self.vernam = tk.Radiobutton(text="Vernam",
                                     variable=self.code_type, value=2)
        self.inl = tk.Label(self.window, text="input")
        self.oul = tk.Label(self.window, text="output")
        self.kl = tk.Label(self.window, text="key")
        self.btn_code = tk.Button(
            self.window, text=' Code ', command=self.code)
        self.btn_decode = tk.Button(
            self.window, text='Decode', command=self.decode)
        self.btn_hack = tk.Button(
            self.window, text=' Hack ', command=self.hack)
        self.in_file = tk.Entry(self.window, textvariable=self.inpu)
        self.out_file = tk.Entry(self.window, textvariable=self.outpu)
        self.key_file = tk.Entry(self.window, textvariable=self.keyp)
        self.grid_create()
        self.window.mainloop()

