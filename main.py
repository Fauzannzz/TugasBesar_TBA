from lexical_analyzer import lexical_analyzer
from parse import parser

input_string = input("Masukkan string input: ")

"""
contoh input valid :

if b > c : a = b + c
if B < A : C = A % B
if c == a : b = c / a

"""

print('============================== LEXICAL ANALYZER PROGRAM ==============================\n')
res_tokens = lexical_analyzer(input_string)
print(res_tokens, "\n")

print('============================== PARSE PROGRAM ==============================\n')
res_parsing = parser(input_string)
print("HASIL: ", res_parsing)
