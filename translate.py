# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def translatesymbol(symbol):
    d = {u"A": "A", u"a": "a",
         u"B": "B", u"b": "b",
         u"C": "C", u"c": "c",
         u"D": "D", u"d": "d",
         u"E": "E", u"e": "e",
         u"F": "F", u"f": "f",
         u"G": "G", u"g": "g",
         u"H": "H", u"h": "h",
         u"I": "I", u"i": "i",
         u"J": "J", u"j": "j",
         u"K": "K", u"k": "k",
         u"L": "L", u"l": "l",
         u"M": "M", u"m": "m",
         u"N": "N", u"n": "n",
         u"O": "O", u"o": "o",
         u"P": "P", u"p": "p",
         u"Q": "Q", u"q": "q",
         u"R": "R", u"r": "r",
         u"S": "S", u"s": "s",
         u"T": "T", u"t": "t",
         u"U": "U", u"u": "u",
         u"V": "V", u"v": "v",
         u"W": "W", u"w": "w",
         u"X": "X", u"x": "x",
         u"Y": "Y", u"y": "y",
         u"Z": "z", u"z": "z",
         u"А": "A", u"а": "a",
         u"Б": "B", u"б": "b",
         u"В": "V", u"в": "v",
         u"Г": "G", u"г": "g",
         u"Д": "D", u"д": "d",
         u"Е": "E", u"е": "e",
         u"Ё": "Yo", u"ё": "yo",
         u"Ж": "Zh", u"ж": "zh",
         u"З": "Z", u"з": "z",
         u"И": "I", u"и": "i",
         u"К": "K", u"к": "k",
         u"Л": "L", u"л": "l",
         u"М": "M", u"м": "m",
         u"Н": "N", u"н": "n",
         u"О": "O", u"о": "o",
         u"П": "p", u"п": "p",
         u"Р": "R", u"р": "r",
         u"С": "S", u"с": "s",
         u"Т": "T", u"т": "t",
         u"У": "U", u"у": "u",
         u"Ф": "F", u"ф": "f",
         u"Х": "Kh", u"х": "kh",
         u"Ц": "Ts", u"ц": "ts",
         u"Ч": "Ch", u"ч": "ch",
         u"Ш": "Sh", u"ш": "sh",
         u"Щ": "Sch", u"щ": "sch",
         u"Ъ": "'", u"ъ": "'",
         u"Ы": "I", u"ы": "i",
         u"Ь": "", u"ь": "",
         u"Э": "E", u"э": "e",
         u"Ю": "Yu", u"ю": "yu",
         u"Я": "Ya", u"я": "ya",
         u"Й": "I", u"й": "i",
         " ": "-"}
    try:
        key = d[symbol]
        return key
    except KeyError:
        return ''


def translate(a):
    a = a.strip()  # Удаление пробельных символов в начеле и конце строки
    transtext = ''
    for i in a:
        transtext = transtext + translatesymbol(i)
    return transtext.lower()  # Преобразование в нижний регистр и возврат строки