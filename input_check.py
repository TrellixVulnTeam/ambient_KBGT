# Legal input 
legal_letters = ('c', 'd', 'e', 'f', 'g', 'a', 'b')
legal_symbols = ('#', 'x', 'b')
legal_numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# Input and check
def getNote(question):
    answer = input(question).lower()
    i = 0
    if len(answer) <= 4 and len(answer) != 0: 
        while i in range(len(answer)):
            if i == 0 and answer[0] in legal_letters:
                i += 1
            elif i in range(1, 3) and answer[i] in legal_symbols:
                i += 1
            elif answer[i] in legal_numbers:
                i += 1
            else:
                print('Oops, there is an error... ')
                answer = input(question).lower()
    else:
        if len(answer) > 4:
            print('Oops, the input is too long...')
            answer = input(question).lower()
        else:
            print('Oops, please type in an input...')
            answer = input(question).lower()
    return answer

# Chord input and check
def getChord(question):
    raw_answer = input(question).lower()
    filter_answer = raw_answer.split()
    return filter_answer

# Interval calculator 3 input and check
def getNotes(question):
    raw_answer = input(question).lower()
    filter_answer = raw_answer.split()
    return filter_answer