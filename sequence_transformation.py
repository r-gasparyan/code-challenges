def split_letters(letters):
    # create tuple [start;end;letter] for every sequence of letters
    diapasons = []
    i = 0
    while i < len(letters):
        start = i
        # pass through same letter
        while (i < len(letters)) and (letters[start] == letters[i]):
            i = i + 1

        end = i - 1
        # diapasons.append([start, end, letters[start]])
        diapasons.append(Diapason(start, end, letters[start]))
    return diapasons

def fit(digit, letter):
    if digit == '1':
        return letter == 'A' or letter == 'B'
    else:
        return letter == 'A'

class Position():
    def __init__(self, digit):
        self.digit = digit
        self.diapason = None

    def empty(self):
        return self.diapason is None

    def assign_diapason(self, diapason):
        self.diapason = diapason

    def __str__(self):
        dp = '[]' if self.diapason is None else self.diapason
        return '\"{}\" {}'.format(self.digit, dp)

    def __repr__(self):
        return str(self)


class Diapason():
    def __init__(self, start, end, letter):
        self.start = start
        self.end = end
        self.letter = letter

    def __repr__(self):
        return '[ {}:{} {}]'.format(self.start, self.end, self.letter)
        # return '{}{}'.format(len(self), self.letter)

    def __len__(self):
        return self.end - self.start + 1


def check(digits, letters):
    diapasons = split_letters(letters)

    digit_positions = [ Position(digits[i]) for i in xrange(len(digits))]
    #print digit_positions
    #print diapasons
    j = 0
    for i in xrange(len(digits)):
        # A and B for 1; A for 0
        if j < len(diapasons) and fit(digits[i], diapasons[j].letter):
            digit_positions[i].assign_diapason(diapasons[j])
            j = j + 1

    #print 'digit positions', digit_positions

    # try to fill empty positions
    for i in xrange(len(digit_positions)-1):
        if digit_positions[i].diapason is not None and \
                len(digit_positions[i].diapason) > 1 and \
                digit_positions[i+1].empty() and \
                fit(digit_positions[i+1].digit, digit_positions[i].diapason.letter):

            # move all letters except one
            cur_position = digit_positions[i]
            new_diapason = Diapason(cur_position.diapason.start + 1, cur_position.diapason.end, cur_position.diapason.letter)
            #print new_diapason
            cur_position.diapason.end = cur_position.diapason.start

            digit_positions[i+1].assign_diapason(new_diapason)

    #print digit_positions

    res = any(pos.empty() for pos in digit_positions)
    #print 'Result: ', not res
    return not res
    
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test.strip():
        digits, letters =  test.split()
        if check(digits, letters):
            print 'Yes'
        else:
            print 'No'
test_cases.close()
