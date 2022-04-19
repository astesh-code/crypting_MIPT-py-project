from argparse import ArgumentParser
import CodeIt

parser = ArgumentParser(
    description='CodeIt0 0.0.1 (c) 2022 by astesh',
    epilog='Example: %(prog)s --mode caesar --type 1 --input input.txt --output out.txt -key key.txt. \
    Key argument are necessary to decode all chiphres. To chiphre files it can be given or generated and written to key.txt'
)
parser.add_argument(
    '-m', '--mode',
    dest='mode',
    required=True,
    help='Mode: code - c or decode - d, h only for Caesar hacking',
)
parser.add_argument(
    '-t', '--type',
    dest='scr',
    required=True,
    help='Way of coding: caesar, vigenere, vernam'
)
parser.add_argument(
    '-i', '--input',
    dest='inp',
    required=True,
    help='Input txt file',
)
parser.add_argument(
    '-o', '--output',
    dest='out',
    required=True,
    help='Output txt file',
)
parser.add_argument(
    '-k', '--key',
    dest='key',
    required=False,
    default=None,
    help='File with a key. Optional argument for coding, obligatory for decoding',
)

types = {
    'caesar': CodeIt.Caesar,
    'vigenere': CodeIt.Vigenere,
    'vernam': CodeIt.Vernam
}

args = parser.parse_args()
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
    with open(args.out, 'w') as out:
        out.write(Temp.code())
    if args.key == None:
        with open('/'.join(args.out.split('/')[0:-1])+'/'+'key.txt', 'w') as key:
            key.write(str(Temp.key))
            print(
                f"Key written to {'/'.join(args.out.split('/')[0:-1])+'/'+'key.txt'}")
if (args.mode == 'd'):
    with open(args.out, 'w') as out:
        out.write(Temp.decode())
if (args.mode == 'h'):
    with open(args.out, 'w') as out:
        out.write(str(Temp.intel_hack()))
    if args.key == None:
        with open('/'.join(args.out.split('/')[0:-1])+'/'+'key.txt', 'w') as key:
            key.write(str(Temp.key))
            print(
                f"Key written to {'/'.join(args.out.split('/')[0:-1])+'/'+'key.txt'}")
