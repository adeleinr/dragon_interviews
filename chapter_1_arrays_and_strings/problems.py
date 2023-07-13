import math
import unittest
from collections import Counter


def has_unique_chars(string: str) -> bool:
    char_map = [False]*128
    for char in string:
        if char_map[ord(char)]:
            return False
        else:
            char_map[ord(char)] = True
    return True


def has_unique_chars_pythonic(string: str) -> bool:
    return len(set(string)) == len(string)


def is_permutation(string1: str, string2: str) -> bool:
    return len(string1) == len(string2) and set(string1) == set(string2)


def urlify(string: str):
    return "%20".join(string.split())


def is_palindrome(string: str) -> bool:
    head_index = 0
    tail_index = len(string) - 1
    while head_index <= tail_index:
        if string[head_index] != string[tail_index]:
            return False
        head_index += 1
        tail_index -= 1
    return True


def is_palidrome_permutation(string):
    map = [0] * 128
    for s in "".join(string.split()):
        map[ord(s)] += 1
    odd_count = 0
    print (map)
    for entry in map:
        if entry % 2 > 0:
            odd_count += 1
            if odd_count > 1:
                return False
    return True


def one_away(string1: str, string2: str):
    if len(string1) > len(string2):
        starting_index = string2.find(string1)
        if starting_index < 0:
            return False
        ending_index = starting_index + len(string1) - 1
        different_indices = ending_index


def string_compression(string: str) -> str:
    counter = Counter(string)
    result = "".join([char+str(count) for char, count in counter.items()])
    return string if len(result) > len(string) else result


def length_of_longest_string_long(string: str) -> int:
    words = string.split()
    if not words:
        return 0
    longest_length = len(words[0])
    for word in words[1:]:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length


def length_of_longest_string(string: str) -> int:
    result = len(max(string.split(), key=len))
    return result

def reverse_a_string(str):
    char_arr = list(str)
    tail = len(char_arr) - 1
    for head in range(len(char_arr)//2):
        char_arr[head], char_arr[tail] = char_arr[tail], char_arr[head]
        tail -= 1
    return "".join(char_arr)


class Test(unittest.TestCase):
    unique_chars_test_cases = [
        ("laa", False),
        ("la", True),
    ]
    permutation_test_cases = [
        (("la", "al"), True),
        (("abc", "bc"), False),
    ]
    urlify_test_cases = [
        ("la cosa nuestra", "la%20cosa%20nuestra"),
        ("la  cosa nuestra", "la%20cosa%20nuestra"),
    ]
    permutation_of_palindrom_test_cases = [
        ("tact coa", True),
        ("atco cta", True),
        ("abc", False),
    ]
    one_away_test_cases = [
        (("pale", "ale"), True),
        (("pale", "al"), True),
    ]
    string_compression_test_cases = [
        ("abaccccd", "a2b1c4d1"),
        ("abc", "abc"),
    ]
    is_palindrome_testcases = [
        ("radar", True),
        ("raton", False),
        ("radtar", False),
    ]

    longest_string_testcases = [
        ("la casa de mi amigo", 5),
    ]

    reverse_string_testcases = [
        ("hello", "olleh"),
        ("hell", "lleh"),
    ]

    def test_has_unique_chars(self):
        for input, expected in self.unique_chars_test_cases:
            assert(has_unique_chars(input) == expected)

    def test_has_unique_chars_pythonic(self):
        for input, expected in self.unique_chars_test_cases:
            assert(has_unique_chars_pythonic(input) == expected)

    def test_is_permutation(self):
        for input, expected in self.permutation_test_cases:
            assert(is_permutation(input[0], input[1]) == expected)

    def test_urlify(self):
        for input, expected in self.urlify_test_cases:
            assert(urlify(input) == expected), f"failed for value: {input}"

    def test_is_palindrome_permutation(self):
        for input, expected in self.permutation_of_palindrom_test_cases:
            assert(is_palidrome_permutation(input) == expected), f"failed for value: {input}"

    """"
    def test_one_away(self):
        for input, expected in self.one_away_test_cases:
            assert(one_away(input[0], input[1]) == expected), f"failed on value: {input}"
    """
    def test_string_compression(self):
        for input, expected in self.string_compression_test_cases:
            assert(string_compression(input) == expected), f"failed for value {input}"

    def test_is_palindrome(self):
        for input, expected in self.is_palindrome_testcases:
            assert(is_palindrome(input) == expected), f"failed on input {input}"

    def test_find_longest_string(self):
        for input, expected in self.longest_string_testcases:
            assert(length_of_longest_string(input) == expected)

    def test_reverse_str(self):
        for input, expected in self.reverse_string_testcases:
            assert(reverse_a_string(input) == expected)

unittest.main()
