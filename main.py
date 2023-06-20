from lexical_analyzer import lexical_analyzer
from parse import parser

input_string = input("Masukkan string input: ")

tokens = lexical_analyzer(input_string)
token_string = ' '.join(tokens)

print("Token-token hasil analisis leksikal:")
print(token_string)
print()

result = parser(token_string)

print("Hasil parsing:")
print(result)
