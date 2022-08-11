"""
https://www.codewars.com
Roman Numerals Decoder
"""
def solution(roman):
    result = 0
    romanDictMinus = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    romanDictPlus = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for key, value in romanDictMinus.items():
         if key in roman:
            result += int(value)
            roman = roman[:roman.index(key)] + roman[roman.index(key)+2:]
    for key, value in romanDictPlus.items():
        if key in roman:
            result += int(value) * roman.count(key)
            while key in roman:
                roman = roman[:roman.index(key)] + roman[roman.index(key)+2:]
    return result
