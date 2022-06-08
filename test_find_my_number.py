from find_my_number import *
'''
# ======= No possible moves.
possible_moves_lookup1 = {
    "H": ["C"],
    "1": ["B"],
    "C": [],
    "B": []
}

def test_no_possible_moves_lookup1_returns_no_sequences():
    sequences = main(possible_moves_lookup1)
    
    assert len(sequences) == 0

# ======= No possible moves because only vowels.
possible_moves_lookup2 = {
    "H": ["A"],
    "A": ["H"]
}

def test_no_possible_moves_with_vowel_lookup2_returns_no_sequences():
    sequences = main(possible_moves_lookup2)
    
    assert len(sequences) == 0

# ======= 2 keys with each other as single possible move, no vowels.
possible_moves_lookup3 = {
    "H": ["1"],
    "1": ["H"]
}

def test_returns_two_sequences():
    sequences = main(possible_moves_lookup3)
    
    assert len(sequences) == 2

def test_returns_sequences_of_length_10():
    sequences = main(possible_moves_lookup3)

    count = 0

    for sequence in sequences:
        if len(sequence) != 10:
            count += 1
    
    assert count == 0

def test_returns_single_sequence_for_starting_key_H():
    sequences = main(possible_moves_lookup3)

    count = 0

    for sequence in sequences:
        if sequence[0] == "H":
            count += 1
        
    assert count == 1

def test_returns_alternating_sequence_for_starting_key_H():
    sequences = main(possible_moves_lookup3)
    assert ["H", "1", "H", "1", "H", "1", "H", "1", "H", "1"] in sequences

def test_returns_single_sequence_for_starting_key_1():
    sequences = main(possible_moves_lookup3)

    count = 0

    for sequence in sequences:
        if sequence[0] == "1":
            count += 1
        
    assert count == 1

def test_returns_alternating_sequence_for_starting_key_1():
    sequences = main(possible_moves_lookup3)
    assert ["1", "H", "1", "H", "1", "H", "1", "H", "1", "H"] in sequences

# ======= GOT STUCK.

harder_possible_moves_lookup = {
    "H": ["1", "B"],
    "B": ["H"],
    "1": []
}

def test_simplest_possible_moves_lookup_returns_two_sequences():
    sequences = main(harder_possible_moves_lookup)
    
    assert len(sequences) == 2
    
'''

# Testing count

harder_possible_moves_lookup = {
    "H": ["1", "B"],
    "B": ["H"],
    "1": []
}

def test_count_number_of_valid_sequences():
    valid_sequence_count = main(harder_possible_moves_lookup)
    assert valid_sequence_count == 3