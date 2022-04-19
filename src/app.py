from tkinter import *
import CodeIt

class arg():
    key=None
    out=None
    inp=None
    mode=None
    scr=None

def start(a):
    types = {
        'caesar' : CodeIt.Caesar,
        'vigenere': CodeIt.Vigenere,
        'vernam':CodeIt.Vernam
    }

    scr = types[a.scr]
    print(a.scr, a.inp, a.out, a.mode, a.key)
    with open(a.inp, 'r') as inp:
        text = inp.read()
    if a.key:
        with open(a.key, 'r') as key_f:
            key = key_f.read()
    else:
        key = None
    Temp = scr(text, key)
    if (a.mode=='c'):
        with open(a.out, 'w') as out:
            out.write(Temp.code())
        if a.key==None:
            with open('/'.join(a.out.split('/')[0:-1])+'/'+'key.txt', 'w') as key:
                key.write(str(Temp.key))
    if (a.mode=='d'):
        with open(a.out, 'w') as out:
            out.write(Temp.decode())
    if (a.mode=='h'):
        with open(a.out, 'w') as out:
            out.write(str(Temp.intel_hack()))
        if a.key==None:
            with open('/'.join(a.out.split('/')[0:-1])+'/'+'key.txt', 'w') as key:
                key.write(str(Temp.key))

window = Tk()

inpu = StringVar()

outpu = StringVar()

keyp = StringVar()
ar = arg()

def code():
    change()
    ar.mode = 'c'
    ar.inp = inpu.get()
    ar.out = outpu.get()
    ar.key = keyp.get()
    start(ar)


def decode():
    change()
    ar.mode = 'd'
    ar.inp = inpu.get()
    ar.out = outpu.get()
    ar.key = keyp.get()
    start(ar)


def hack():
    change()
    ar.mode = 'h'
    ar.inp = inpu.get()
    ar.out = outpu.get()
    ar.key = keyp.get()
    start(ar)


def change():
    if var.get() == 0:
        ar.scr='caesar'
    elif var.get() == 1:
        ar.scr='vigenere'
    elif var.get() == 2:
        ar.scr='vernam'


var = IntVar()
var.set(0)
caesar = Radiobutton(text="Caesar",
                     variable=var, value=0)
vegenere = Radiobutton(text="Vigenere",
                       variable=var, value=1)
vernam = Radiobutton(text="Vernam",
                     variable=var, value=2)

window.title("CodeIt")
window.geometry('380x110')
inl = Label(text="input")
oul = Label(text="output")
kl = Label(text="key")
btn_code = Button(window, text=' Code ', command=code)
btn_decode = Button(window, text='Decode', command=decode)
btn_hack = Button(window, text=' Hack ', command=hack)
in_file = Entry(window, textvariable=inpu)
out_file = Entry(window, textvariable=outpu)
key_file = Entry(window, textvariable=keyp)
btn_hack.grid(column=4, row=2)
btn_code.grid(column=4, row=0)
btn_decode.grid(column=4, row=1)
in_file.grid(column=1, row=0)
out_file.grid(column=1, row=1)
key_file.grid(column=1, row=2)
caesar.grid(column=2, row=0)
vernam.grid(column=2, row=2)
vegenere.grid(column=2, row=1)
inl.grid(column=0, row=0)
oul.grid(column=0, row=1)
kl.grid(column=0, row=2)
window.mainloop()
