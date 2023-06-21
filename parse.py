import time
def parser(input_string):
    tokens = input_string.lower().split()
    tokens.append("EOS")

    non_terminals = ['statement', 'kondisi', 'aksi', 'variabel', 'operator', 'hitungan']
    terminals = ['if', ':', 'a', 'b', 'c',  '==', '!=' , '>', '<',  '>=', '<=', '+', '-', '*', '/', '%', '=']

    parse_table = {}

    parse_table[('statement', 'if')] = ['if', 'kondisi', ':', 'aksi']
    parse_table[('statement', ':')] = ['error']
    parse_table[('statement', 'a')] = ['error']
    parse_table[('statement', 'b')] = ['error']
    parse_table[('statement', 'c')] = ['error']
    parse_table[('statement', '==')] = ['error']
    parse_table[('statement', '!=')] = ['error']
    parse_table[('statement', '>')] = ['error']
    parse_table[('statement', '<')] = ['error']
    parse_table[('statement', '>=')] = ['error']
    parse_table[('statement', '<=')] = ['error']
    parse_table[('statement', '+')] = ['error']
    parse_table[('statement', '-')] = ['error']
    parse_table[('statement', '/')] = ['error']
    parse_table[('statement', '*')] = ['error']
    parse_table[('statement', '%')] = ['error']
    parse_table[('statement', '=')] = ['error']
    parse_table[('statement', 'EOS')] = ['error']

    parse_table[('kondisi', 'if')] = ['error']
    parse_table[('kondisi', ':')] = ['error']
    parse_table[('kondisi', 'a')] = ['variabel', 'operator', 'variabel']
    parse_table[('kondisi', 'b')] = ['variabel', 'operator', 'variabel']
    parse_table[('kondisi', 'c')] = ['variabel', 'operator', 'variabel']
    parse_table[('kondisi', '==')] = ['error']
    parse_table[('kondisi', '!=')] = ['error']
    parse_table[('kondisi', '>')] = ['error']
    parse_table[('kondisi', '<')] = ['error']
    parse_table[('kondisi', '>=')] = ['error']
    parse_table[('kondisi', '<=')] = ['error']
    parse_table[('kondisi', '+')] = ['error']
    parse_table[('kondisi', '-')] = ['error']
    parse_table[('kondisi', '/')] = ['error']
    parse_table[('kondisi', '*')] = ['error']
    parse_table[('kondisi', '%')] = ['error']
    parse_table[('kondisi', '=')] = ['error']
    parse_table[('kondisi', 'EOS')] = ['error']

    parse_table[('aksi', 'if')] = ['error']
    parse_table[('aksi', ':')] = ['error']
    parse_table[('aksi', 'a')] = ['variabel', '=', 'variabel', 'hitungan', 'variabel']
    parse_table[('aksi', 'b')] = ['variabel', '=', 'variabel', 'hitungan', 'variabel']
    parse_table[('aksi', 'c')] = ['variabel', '=', 'variabel', 'hitungan', 'variabel']
    parse_table[('aksi', '==')] = ['error']
    parse_table[('aksi', '!=')] = ['error']
    parse_table[('aksi', '>')] = ['error']
    parse_table[('aksi', '<')] = ['error']
    parse_table[('aksi', '>=')] = ['error']
    parse_table[('aksi', '<=')] = ['error']
    parse_table[('aksi', '+')] = ['error']
    parse_table[('aksi', '-')] = ['error']
    parse_table[('aksi', '/')] = ['error']
    parse_table[('aksi', '*')] = ['error']
    parse_table[('aksi', '%')] = ['error']
    parse_table[('aksi', '=')] = ['error']
    parse_table[('aksi', 'EOS')] = ['error']

    parse_table[('variabel', 'if')] = ['error']
    parse_table[('variabel', ':')] = ['error']
    parse_table[('variabel', 'a')] = ['a']
    parse_table[('variabel', 'b')] = ['b']
    parse_table[('variabel', 'c')] = ['c']
    parse_table[('variabel', '==')] = ['error']
    parse_table[('variabel', '!=')] = ['error']
    parse_table[('variabel', '>')] = ['error']
    parse_table[('variabel', '<')] = ['error']
    parse_table[('variabel', '>=')] = ['error']
    parse_table[('variabel', '<=')] = ['error']
    parse_table[('variabel', '+')] = ['error']
    parse_table[('variabel', '-')] = ['error']
    parse_table[('variabel', '/')] = ['error']
    parse_table[('variabel', '*')] = ['error']
    parse_table[('variabel', '%')] = ['error']
    parse_table[('variabel', '=')] = ['error']
    parse_table[('variabel', 'EOS')] = ['error']

    parse_table[('operator', 'if')] = ['error']
    parse_table[('operator', ':')] = ['error']
    parse_table[('operator', 'a')] = ['error']
    parse_table[('operator', 'b')] = ['error']
    parse_table[('operator', 'c')] = ['error']
    parse_table[('operator', '==')] = ['==']
    parse_table[('operator', '!=')] = ['!=']
    parse_table[('operator', '>')] = ['>']
    parse_table[('operator', '<')] = ['<']
    parse_table[('operator', '>=')] = ['>=']
    parse_table[('operator', '<=')] = ['<=']
    parse_table[('operator', '+')] = ['error']
    parse_table[('operator', '-')] = ['error']
    parse_table[('operator', '/')] = ['error']
    parse_table[('operator', '*')] = ['error']
    parse_table[('operator', '%')] = ['error']
    parse_table[('operator', '=')] = ['error']
    parse_table[('operator', 'EOS')] = ['error']

    parse_table[('hitungan', 'if')] = ['error']
    parse_table[('hitungan', ':')] = ['error']
    parse_table[('hitungan', 'a')] = ['error']
    parse_table[('hitungan', 'b')] = ['error']
    parse_table[('hitungan', 'c')] = ['error']
    parse_table[('hitungan', '==')] = ['error']
    parse_table[('hitungan', '!=')] = ['error']
    parse_table[('hitungan', '>')] = ['error']
    parse_table[('hitungan', '<')] = ['error']
    parse_table[('hitungan', '>=')] = ['error']
    parse_table[('hitungan', '<=')] = ['error']
    parse_table[('hitungan', '+')] = ['+']
    parse_table[('hitungan', '-')] = ['-']
    parse_table[('hitungan', '/')] = ['/']
    parse_table[('hitungan', '*')] = ['*']
    parse_table[('hitungan', '%')] = ['%']
    parse_table[('hitungan', '=')] = ['error']
    parse_table[('hitungan', 'EOS')] = ['error']

    stack = ['#', 'statement']
    index_token = 0
    symbol = tokens[index_token]

    while len(stack) > 0:
        time.sleep(0.5)
        top = stack[len(stack) - 1]
        print('TOP    =', top)
        print('SYMBOL =', symbol)
        if symbol in terminals or symbol in non_terminals:
            if top in terminals:
                print('TOP adalah symbol terminal')
                if top == symbol:
                    stack.pop()
                    index_token += 1
                    symbol = tokens[index_token]
                    if symbol == "EOS":
                        print('isi stack:', stack)
                        stack.pop()
                        
                else:
                    print('ERROR')
                    break
            elif top in non_terminals:
                print('TOP adalah symbol non-terminal')
                if parse_table[(top, symbol)][0] != 'error':
                    stack.pop()
                    symbol_to_be_pushed = parse_table[(top, symbol)]
                    for i in range(len(symbol_to_be_pushed)-1, -1, -1):
                        stack.append(symbol_to_be_pushed[i])
                else:
                    print('ERROR')
                    break
            else:
                print('ERROR')
                break
        else:
            print('ERROR')
            break
        print('isi stack:', stack)
        print()
    print()
    
    if symbol == 'EOS' and len(stack) == 0:
        result = '\n-------------------------------\nDITERIMA KARENA SESUAI GRAMMAR\n-------------------------------'
    else:
        result = '\n-------------------------------------------\nTIDAK DITERIMA KARENA TIDAK SESUAI GRAMMAR\n-------------------------------------------'


    return result
