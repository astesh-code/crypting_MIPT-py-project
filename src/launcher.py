### сявзь интерфейсов и модуля

import src.CodeIt as CodeIt

### запускает модуль в режиме кодирования
def code(args, Temp):
    with open(args.out, 'w') as out:
        out.write(Temp.code())
    if args.key == None:
        with open('/'.join(args.out.split('/')[0:-1])+'/'+'key.txt', 'w') as key:
            key.write(str(Temp.key))
            print(
                f"Key written to {'/'.join(args.out.split('/')[0:-1])+'/'+'key.txt'}")

### запускает модуль в режиме декодирования
def decode(args, Temp):
    with open(args.out, 'w') as out:
        out.write(Temp.decode())

### запускает модуль в режиме взлома цезаря
def hack(args, Temp):
    with open(args.out, 'w') as out:
        out.write(str(Temp.intel_hack()))
    if args.key == None:
        with open('/'.join(args.out.split('/')[0:-1])+'/'+'key.txt', 'w') as key:
            key.write(str(Temp.key))
            print(
                f"Key written to {'/'.join(args.out.split('/')[0:-1])+'/'+'key.txt'}")

### функция собирающая данные запуска и передающая их дальше
def use(args):
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
