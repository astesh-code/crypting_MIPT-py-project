### основной модуль реализующий шифрование ###

from abc import ABC
from collections import Counter
from random import randint
from src.Globals import Globals

### декоратор, определяющий задан ли ключ и генерирующий его
def key_map(in_fun):
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

### базовый класс для шифра Цезаря и шифра Виженера
class SimpleCode(ABC):
    text = None
    key = None
    uncoded = True

    def __init__(self, text, key=None):
        self.text = text
        self.key = key
        self.__eng_freq__ = Globals.ENG_FREQ
        self.__rus_freq__ = Globals.RUS_FREQ
        self.__lang__ = Globals.LANG

    ### определение, к какому алфавиту принадлежит буква
    def __def_alph__(self, letter) -> str:
        for alph in self.__lang__.values():
            if letter in alph[0]:
                return alph[0]
            if letter in alph[1]:
                return alph[1]
        else:
            return None

    ### сгенерировать ключ, если не задан
    def __gen_key__():
        pass

    ### прибавить ключ к юукве
    def __change_let__():
        pass

    ### кодирование
    def code():
        pass

    ### декодирование
    def decode():
        pass

### шифр Цезаря
class Caesar(SimpleCode):

    def __gen_key__(self) -> int:
        return randint(0, Globals.MAX_KEY_CAESAR)

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

    ### доп функция для вывода всех возмозжных перестановок
    def show_all(self) -> list:
        for lan in self.__lang__.values():
            if list(filter(str.isalpha, list(self.text)))[0].lower() in lan[0]:
                lf = lan[2]
        return [(self.decode(i), lf) for i in range(len(lf))]

    ### взлом Цезаря методом частотного анализа
    def intel_hack(self) -> str:

        ### подсчет метрики для перестановки. Меньше метрика - правильней ключ
        def metric(string, lang) -> int:
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

### Шифр Виженера
class Vigenere(SimpleCode):

    def __gen_key__(self) -> str:
        lis = [chr(randint(ord('a'), ord('z')))
               for i in range(randint(Globals.MIN_KEY_VIGENERE, Globals.MAX_KEY_VIGENERE))]
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

###  Шифр Вернама
class Vernam():

    def __init__(self, text, key=None):
        self.text = text
        self.key = key
        if key and key[0].isalpha():
            self.key = ' '.join(str(ord(l)) for l in self.key)

    ### сгенерировать ключ, если не задан
    def __gen_key__(self) -> str:
        lis = [str(randint(0, Globals.MAX_KEY_VIGENERE)) for i in range(len(self.text))]
        return ' '.join(lis)

    ### кодирование
    @key_map
    def code(self, key=None) -> str:
        pairs = list(zip(self.text, key.split()))
        return ' '.join([str(ord(pair[0]) ^ int(pair[1])) for pair in pairs])

    ### декодирование
    @key_map
    def decode(self, key=None) -> str:
        pairs = list(zip(self.text.split(), key.split()))
        return ''.join([chr(int(pair[0]) ^ int(pair[1])) for pair in pairs])
