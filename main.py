from lexical_analyzer import lexical_analyzer
from parse import parser

input_string = input("Masukkan string input: ")

tokens = lexical_analyzer(input_string)
token_string = ' '.join(tokens)

print("Token-token hasil analisis leksikal:")
print(token_string)
print()

hasil_parsing = parser(input_string)

print("Hasil parsing:")
print(hasil_parsing)
