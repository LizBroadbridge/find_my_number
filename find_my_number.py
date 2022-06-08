#  A     B     C    D     E
#  F     G     H    I     J
#  K     L     M    N     O
#        1     2    3

#  0     1     2     3    4
#  5     6     7     8    9
#  10   11    12    13   14
#       15    16    17

# Given keypad has 18 keys which will be in index.
# The sequence will have a maximum of 10 keys.
# The first key press can be any key.
# Each subsequent keypress can be a knight move from the last key.
# There can be up most 2 VOWELS in the sequence.
# Here is no wrapping allowed on a knight move
# Assuming that you can't jump over empty spaces. E.g. F --> 1 isn't a valid move.



from sre_constants import NOT_LITERAL


default_possible_moves_lookup = {
    "A": ["H", "L"],
    "B": ["I", "K", "M"],
    "C": ["F", "J", "L", "N"],
    "D": ["G", "M", "O"],
    "E": ["H", "N"],
    "F": ["C", "M", "1"],
    "G": ["D", "N", "2"],
    "H": ["A", "E", "K", "O", "1", "3"],
    "I": ["B", "L", "2"],
    "J": ["C", "M", "3"],
    "K": ["B", "H", "2"],
    "L": ["A", "C", "I", "3"],
    "M": ["B", "D", "F", "J"],
    "N": ["C", "E", "G", "1"],
    "O": ["D", "H", "2"],
    "1": ["F", "H", "N"],
    "2": ["G", "I", "K", "O"],
    "3": ["H", "J", "L"]
}



VOWELS = {"A", "E", "I", "O", "U"}

def is_vowel(letter):
    return letter in VOWELS

valid_sequences = {}

def check(possible_moves_lookup, key, remaining, vowel_limit):
    if remaining == 1:
        return {key}

    else:
        result = set()
        for possible_move in possible_moves_lookup[key]:
            # check if possible_move exists in valid_sequences
            if possible_move in valid_sequences:
            # if does, take each sequence and:
                for unfinished_sequence in valid_sequences[possible_move]:
            #   prepend with key
                    prepended_sequence = key + unfinished_sequence
            #   trim so that length == remaining
                    finished_sequence = prepended_sequence[0:remaining]
            #   check vowel count, result.add if okay
                    vowel_count = 0
                    for char in finished_sequence:
                        if is_vowel(char):
                            vowel_count += 1
                    if vowel_count < vowel_limit:
                        result.add(finished_sequence)
            # if possible_move does not exist in valid_sequences, perform below:
            else:
                for unfinished_sequence in check(possible_moves_lookup, possible_move, remaining - 1, vowel_limit):
                    finished_sequence = key + unfinished_sequence
                    vowel_count = 0
                    for char in finished_sequence:
                        if is_vowel(char):
                            vowel_count += 1
                    if vowel_count < vowel_limit:
                        result.add(finished_sequence)
        return result

REMAINING = 10
VOWEL_LIMIT = 3

def main(possible_moves_lookup):
    valid_sequence_count = 0

    for starting_key in possible_moves_lookup:
        valid_sequences_for_starting_key = check(possible_moves_lookup, starting_key, REMAINING, VOWEL_LIMIT)

        valid_sequences[starting_key] = valid_sequences_for_starting_key
        
        for _ in valid_sequences_for_starting_key:
            valid_sequence_count += 1

    #print(valid_sequences)
    print(valid_sequence_count)
    return valid_sequence_count
    

valid_sequence_count = main(default_possible_moves_lookup)


# Change keypad values 



'''
VOWELS = {"A", "E", "I", "O", "U"}
visited = set()

def is_consonant(letter):
    return letter not in VOWELS


def is_vowel(letter):
    return letter in VOWELS


def get_next_possible_moves(vowel_count, possible_moves_lookup, key):
    possible_moves = possible_moves_lookup[key]

    if vowel_count >= 2:
        possible_moves = list(filter(is_consonant, possible_moves))

    return possible_moves


def find_sequence(possible_moves_lookup, key):
    sequence = []
    vowel_count = 0

    while len(sequence) < 10:
        sequence.append(key)

        if is_vowel(key):
            vowel_count += 1

        possible_moves = get_next_possible_moves(
            vowel_count, possible_moves_lookup, key)

        if len(possible_moves) == 0:
            break

        key = possible_moves[0]

    return sequence


def main(possible_moves_lookup):
    result = []

    for starting_key in possible_moves_lookup:
        sequence = find_sequence(possible_moves_lookup, starting_key)
        if len(sequence) == 10:
            result.append(sequence)

    return result

'''







"""
def valid_sequences(key, keys_left, vowel_count):
    if keys_left == 0:
        return []

    if is_vowel(key):
        vowel_count += 1

    possible_moves = possible_moves_lookup[key]

    if vowel_count == 2:
        possible_moves = filter(is_constant, possible_moves)

    if possible_moves.length == 1:
        return [possible_moves[0]]

    sequences = []
    for key in possible_moves:
        sequences.append(valid_sequences(key, keys_left - 1, vowel_count))

    return sequences












sequences = []

for key in possible_moves_lookup:
    sequences.append(valid_sequences(key, 10, 0))


            key1 = possible_moves[1]
            vowel_count1 = vowel_count
            sequence1 = sequence.copy()

            while len(sequence1) < 10:
                
                sequence1.append(key1)

                if is_vowel(key1):
                    vowel_count1 += 1

                possible_moves1 = possible_moves_lookup[key1]

                if vowel_count1 >= 2:
                    possible_moves1 = list(filter(is_consonant, possible_moves1))

                if len(possible_moves1) == 0:
                    break

                key1 = possible_moves1[1]

            if len(sequence1) == 10:
                sequences.append(sequence1)

            key1 = possible_moves[1]
"""
