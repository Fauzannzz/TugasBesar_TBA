import string
import re
import time

#initialization
def lexical_analyzer(input_string):
    alphabet_list = re.findall(r'(\w+|[<>=+*/-]+|:)',input_string)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12']

    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
            transition_table[(state, '#')] = 'error'
            transition_table[(state, ' ')] = 'error'

    #Transition Tables
    transition_table[('q0', ' ')] = 'q0'
    transition_table[('q0', 'i')] = 'q1'

    transition_table[('q1', 'f')] = 'q2'

    transition_table[('q2', ' ')] = 'q2'
    transition_table[('q2', 'a')] = 'q3'
    transition_table[('q2', 'b')] = 'q3'
    transition_table[('q2', 'c')] = 'q3'

    transition_table[('q3', ' ')] = 'q3'
    transition_table[('q3', '!')] = 'q4'
    transition_table[('q3', '=')] = 'q4'
    transition_table[('q3', '>')] = 'q4'
    transition_table[('q3', '<')] = 'q4'

    transition_table[('q4', ' ')] = 'q4'
    transition_table[('q4', '=')] = 'q4'
    transition_table[('q4', 'a')] = 'q5'
    transition_table[('q4', 'b')] = 'q5'
    transition_table[('q4', 'c')] = 'q5'

    transition_table[('q5', ' ')] = 'q5'
    transition_table[('q5', ':')] = 'q6'

    transition_table[('q6', ' ')] = 'q6'
    transition_table[('q6', 'a')] = 'q7'
    transition_table[('q6', 'b')] = 'q7'
    transition_table[('q6', 'c')] = 'q7'

    transition_table[('q7', ' ')] = 'q7'
    transition_table[('q7', '=')] = 'q8'

    transition_table[('q8', ' ')] = 'q8'
    transition_table[('q8', 'a')] = 'q9'
    transition_table[('q8', 'b')] = 'q9'
    transition_table[('q8', 'c')] = 'q9'

    transition_table[('q9', ' ')] = 'q9'
    transition_table[('q9', '+')] = 'q10'
    transition_table[('q9', '-')] = 'q10'
    transition_table[('q9', '/')] = 'q10'
    transition_table[('q9', '*')] = 'q10'
    transition_table[('q9', '%')] = 'q10'

    transition_table[('q10', ' ')] = 'q10'
    transition_table[('q10', 'a')] = 'q11'
    transition_table[('q10', 'b')] = 'q11'
    transition_table[('q10', 'c')] = 'q11'

    transition_table[('q11', ' ')] = 'q12'
    transition_table[('q11', '#')] = 'accept'

    transition_table[('q12', ' ')] = 'q12'
    transition_table[('q12', '#')] = 'accept'

    #Lexical Analysis
    i = 0
    idx_char = 0
    state = 'q0'
    current_token = ''
    result = None  # Inisialisasi result dengan None
    for current_char in (input_string.lower()+'#'):
        time.sleep(0.5)
        current_token += current_char
        state = transition_table[(state, current_char)]
        if len(current_token) > 1:
            print("Token valid: ", current_token[i], )
            i += 1
        if state == 'q11':
            print('Current token: ', current_token, ', VALID')
            current_token = ''
        if state == 'error':
            print('Token error: ', current_token[i])
            break
        idx_char = idx_char + 1

    #Conclusion
    if state == 'accept':
        result = '----------------------\nSEMUA TOKEN VALID\n----------------------'
    else:
        result = '----------------------------\nADA TOKEN YANG TIDAK VALID\n----------------------------'

    return result
