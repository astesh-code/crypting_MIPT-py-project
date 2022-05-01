### interfaces and module adapter ###

import src.CodeIt as CodeIt

def code(args, Temp):
    """launch module as coder"""
    with open(args.out, 'w') as out:
        out.write(Temp.code())
    if args.key == None:
        with open('/'.join(args.out.split('/')[0:-1])+'/'+'key.txt', 'w') as key:
            key.write(str(Temp.key))
            print(
                f"Key written to {'/'.join(args.out.split('/')[0:-1])+'/'+'key.txt'}")

def decode(args, Temp):
    """launch module as decoder"""
    with open(args.out, 'w') as out:
        out.write(Temp.decode())

def hack(args, Temp):
    """lauch module in hacking mode"""
    with open(args.out, 'w') as out:
        out.write(str(Temp.intel_hack()))
    if args.key == None:
        with open('/'.join(args.out.split('/')[0:-1])+'/'+'key.txt', 'w') as key:
            key.write(str(Temp.key))
            print(
                f"Key written to {'/'.join(args.out.split('/')[0:-1])+'/'+'key.txt'}")

def use(args):
    """collect luanching data and transfer it"""
    types = {
        'caesar': CodeIt.Caesar,
        'vigenere': CodeIt.Vigenere,
        'vernam': CodeIt.Vernam
    }
    scr = types[args.scr]
    with open(args.inp, 'r') as inp:
        text = inp.read()
    if args.key:
        with open(args.key, 'r') as key_f:
            key = key_f.read()
    else:
        key = None
    Temp = scr(text, key)
    if (args.mode == 'c'):
        code(args, Temp)
    if (args.mode == 'd'):
        decode(args, Temp)
    if (args.mode == 'h'):
        hack(args, Temp)
