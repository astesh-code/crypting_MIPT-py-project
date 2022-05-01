class Globals():
    """Dictionaries and other language data"""
    ### frequencies for english language
    eng_freq = {
        'a': 8.17, 'b': 1.4, 'c': 2.78, 'd': 4.25, 'e': 12.7, 'f': 2.23, 'g': 2.02, 'h': 6.09,
        'i': 6.97, 'j':  0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o':  7.51, 'p':  1.93,
        'q': 0.10, 'r': 5.99, 's': 6.33, 't':  9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
        'y': 1.97, 'z': 0.07
    }
    ### -//- for russian
    rus_freq = {
        'о': 9.28, 'а': 8.66, 'е': 8.10, 'и': 7.45, 'н': 6.35, 'т': 6.30, 'р': 5.53, 'с': 5.45,
        'л': 4.32, 'в': 4.19, 'к': 3.47, 'п': 3.35, 'м': 3.29, 'у': 2.90, 'д': 2.56, 'я': 2.22,
        'ы': 2.11, 'ь': 1.90, 'з': 1.81, 'б': 1.51, 'г': 1.41, 'й': 1.31, 'ч': 1.27, 'ю': 1.03,
        'х': 0.92, 'ж': 0.78, 'ш': 0.77, 'ц': 0.52, 'щ': 0.49, 'ф': 0.40, 'э': 0.17, 'ъ': 0.04,
        'ё': 0.04
    }
    ### comman dictionary block
    lang = {
        'Numbers': ('0123456789', '0123456789'),
        'English': ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', eng_freq),
        'Russian': ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', rus_freq)
    }
    
    ### border values for key generating
    max_key_caesar = 100
    max_key_vigenere = 120
    min_key_vigenere = 10
    max_key_vernam = 111206

    ### help messages for console launch
    description='CodeIt0 0.0.2 (c) 2022 by astesh'
    epilog='Example: %(prog)s --mode caesar --type 1 --input input.txt --output out.txt -key key.txt. \
    Key argument are necessary to decode all chiphres. To chiphre files it can be given or generated and written to key.txt'

    h_mode='Mode: code - c or decode - d, h only for Caesar hacking'
    h_scr='Way of coding: caesar, vigenere, vernam'
    h_inp='Input txt file'
    h_out='Output txt file'
    h_key='File with a key. Optional argument for coding, obligatory for decoding'