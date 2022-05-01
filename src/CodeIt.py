### main code module ###

from abc import ABC
from collections import Counter
from random import randint
from src.Globals import Globals

def key_map(in_fun):
    """check if key exist and generate it"""
    def g_args(self, key=None):
        if self.key == None:
            self.key = self.__gen_key__()
        if key == None:
            key = self.key
        return in_fun(self, key)
    g_args.__name__ = in_fun.__name__
    g_args.__doc__ = in_fun.__doc__
    g_args.__module__ = in_fun.__module__
    return g_args

class SimpleCode(ABC):
    """base class for Caesar and Vigenere"""
    text = None
    key = None
    uncoded = True

    def __init__(self, text, key=None):
        """create new code unit"""
        self.text = text
        self.key = key
        self.__eng_freq__ = Globals.eng_freq
        self.__rus_freq__ = Globals.rus_freq
        self.__lang__ = Globals.lang

    def __def_alph__(self, letter) -> str:
        """define alphabet of letter"""
        for alph in self.__lang__.values():
            if letter in alph[0]:
                return alph[0]
            if letter in alph[1]:
                return alph[1]
        else:
            return None

    def __gen_key__():
        """generate new key"""
        pass

    def __change_let__():
        """add code to letter"""
        pass

    def code():
        """code text"""
        pass

    def decode():
        """decode text"""
        pass

class Caesar(SimpleCode):
    """Caesar code and decode class"""

    def __gen_key__(self) -> int:
        return randint(0, Globals.max_key_caesar)

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
        key = int(key)
        return ''.join([self.__change_let__(l, key) for l in self.text])

    @key_map
    def decode(self, key=None) -> str:
        self.uncoded = False
        key = int(key)
        return ''.join([self.__change_let__(l, key) for l in self.text])

    def show_all(self) -> list:
        """all available permutations output"""
        for lan in self.__lang__.values():
            if list(filter(str.isalpha, list(self.text)))[0].lower() in lan[0]:
                lf = lan[2]
        return [(self.decode(i), lf) for i in range(len(lf))]

    def intel_hack(self) -> str:
        """hack Caesar code with freq analysis"""
        def metric(string, lang) -> int:
            """Metric for permutation. Less metric - more correct key"""
            count = Counter(string)
            freq = sum([abs(lang[l]-(count[l]/len(string))*100)
                       for l in lang.keys()])
            return freq

        for lan in self.__lang__.values():
            if list(filter(str.isalpha, list(self.text)))[0].lower() in lan[0]:
                lf = lan[2]
        metrics = [metric(self.decode(i), lf) for i in range(len(lf))]
        self.key = metrics.index(min(metrics))
        return self.decode()

class Vigenere(SimpleCode):
    """Vigenere code and decode class"""
    def __gen_key__(self) -> str:
        lis = [chr(randint(ord('a'), ord('z')))
               for i in range(randint(Globals.min_key_vigenere, Globals.max_key_vigenere))]
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
        pack = list(zip(self.text, key*(len(self.text)//len(key)+1)))
        return ''.join([self.__change_let__(pair) for pair in pack])

class Vernam():
    """Vernam code and decode class"""
    def __init__(self, text, key=None):
        """Create new Vernam code unit"""
        self.text = text
        self.key = key
        if key and key[0].isalpha():
            self.key = ' '.join(str(ord(l)) for l in self.key)

    def __gen_key__(self) -> str:
        """generate new key"""
        lis = [str(randint(0, Globals.max_key_vigenere)) for i in range(len(self.text))]
        return ' '.join(lis)

    @key_map
    def code(self, key=None) -> str:
        """code text"""
        pairs = list(zip(self.text, key.split()))
        return ' '.join([str(ord(pair[0]) ^ int(pair[1])) for pair in pairs])

    @key_map
    def decode(self, key=None) -> str:
        """decode text"""
        pairs = list(zip(self.text.split(), key.split()))
        return ''.join([chr(int(pair[0]) ^ int(pair[1])) for pair in pairs])
