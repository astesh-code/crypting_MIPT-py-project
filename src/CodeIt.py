from abc import ABC
from random import randint
from collections import Counter
from keymapper import key_map


class SimpleCode(ABC):
    text = None
    key = None
    uncoded = True

    def __init__(self, text, key=None):
        self.text = text
        self.key = key
        with open('lang.txt', 'r') as file:
            exec(file.read())

    def __def_alph__(self, letter) -> str:
        for alph in self.__lang__.values():
            if letter in alph[0]:
                return alph[0]
            if letter in alph[1]:
                return alph[1]
        else:
            return None

    def __gen_key__():
        pass

    def __change_let__():
        pass

    def code():
        pass

    def decode():
        pass
    '''
    __eng_freq__ = {
        'a': 8.17, 'b': 1.4, 'c': 2.78, 'd': 4.25, 'e': 12.7, 'f': 2.23, 'g': 2.02, 'h': 6.09,
        'i': 6.97, 'j':  0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o':  7.51, 'p':  1.93,
        'q': 0.10, 'r': 5.99, 's': 6.33, 't':  9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
        'y': 1.97, 'z': 0.07
    }

    __rus_freq__ = {
        'о': 9.28, 'а': 8.66, 'е': 8.10, 'и': 7.45, 'н': 6.35, 'т': 6.30, 'р': 5.53, 'с': 5.45,
        'л': 4.32, 'в': 4.19, 'к': 3.47, 'п': 3.35, 'м': 3.29, 'у': 2.90, 'д': 2.56, 'я': 2.22,
        'ы': 2.11, 'ь': 1.90, 'з': 1.81, 'б': 1.51, 'г': 1.41, 'й': 1.31, 'ч': 1.27, 'ю': 1.03,
        'х': 0.92, 'ж': 0.78, 'ш': 0.77, 'ц': 0.52, 'щ': 0.49, 'ф': 0.40, 'э': 0.17, 'ъ': 0.04,
        'ё': 0.04
    }

    __lang__ = {
        'Numbers': ('0123456789', '0123456789'),
        'English': ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', __eng_freq__),
        'Russian': ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', __rus_freq__)
    }'''


class Caesar(SimpleCode):

    def __gen_key__(self) -> int:
        return randint(0, 100)

    def __change_let__(self, l, key) -> str:
        alph = self.__def_alph__(l)
        if alph:
            key = (not self.uncoded)*(len(alph)-2*key)+key
            return alph[(alph.find(l)+key) % len(alph)]
        else:
            return l

    @key_map
    def code(self, key=None) -> str:
        self.uncoded = True
        key=int(key)
        return ''.join([self.__change_let__(l, key) for l in self.text])

    @key_map
    def decode(self, key=None) -> str:
        self.uncoded = False
        key=int(key)
        return ''.join([self.__change_let__(l, key) for l in self.text])

    def show_all(self)->list:
        for lan in self.__lang__.values():
            if list(filter(str.isalpha, list(self.text)))[0].lower() in lan[0]:
                lf = lan[2]
        return [(self.decode(i), lf) for i in range(len(lf))]

    def intel_hack(self) -> str:

        def metric(string, lang) -> int:
            count = Counter(string)
            freq = sum([abs(lang[l]-(count[l]/len(string))*100) for l in lang.keys()])
            return freq

        for lan in self.__lang__.values():
            if list(filter(str.isalpha, list(self.text)))[0].lower() in lan[0]:
                lf = lan[2]
        metrics = [metric(self.decode(i), lf) for i in range(len(lf))]
        self.key = metrics.index(min(metrics))
        return self.decode()
()


class Vigenere(SimpleCode):
    def __gen_key__(self) -> str:
        lis = [chr(randint(ord('a'), ord('z')))
               for i in range(randint(5, 120))]
        return ''.join(lis)

    def __change_let__(self, pair) -> str:
        l, k = pair[0], pair[1]
        l_al = self.__def_alph__(l)
        k_al = self.__def_alph__(k)
        if l_al:
            key = self.uncoded*(len(l_al)-2*k_al.find(k)-2)+1+k_al.find(k)
            if self.uncoded:
                return l_al[(l_al.find(l)+key) % len(l_al)]
            else:
                return l_al[(l_al.find(l)+key) % len(l_al)]
        else:
            return l

    @key_map
    def code(self, key=None) -> str:
        self.uncoded = True
        pack = list(zip(self.text, key*(len(self.text)//len(key)+1)))
        return ''.join([self.__change_let__(pair) for pair in pack])

    @key_map
    def decode(self, key=None) -> str:
        self.uncoded = False
        pack = list(zip(self.text, self.key*(len(self.text)//len(self.key)+1)))
        return ''.join([self.__change_let__(pair) for pair in pack])

class Vernam():
    
    def __init__(self, text, key=None):
        self.text = text
        self.key = key
        if key and key[0].isalpha():
            self.key = ' '.join(str(ord(l)) for l in self.key)
    
    def __gen_key__(self) -> str:
        lis = [str(randint(0, 111206)) for i in range(len(self.text))]
        return ' '.join(lis)

    @key_map
    def code(self, key=None) -> str:
        pairs = list(zip(self.text, key.split()))
        return ' '.join([str(ord(pair[0]) ^ int(pair[1])) for pair in pairs])

    @key_map
    def decode(self, key=None) -> str:
        pairs = list(zip(self.text.split(), key.split()))
        return ''.join([chr(int(pair[0]) ^ int(pair[1])) for pair in pairs])