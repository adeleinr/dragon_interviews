"""
// Asked by EarnIn
// At an event a celebrity is defined as someone everyone knows and they don’t know anyone else
// There can be a max of 1 celebrity (or could be none).
// To find out if someone is a celebrity you can ask them if they know another person

// Example

// A-> B = True
// B-> A = False

// A-> C = True
// C-> A = True


// B-> C = False
// C-> B = True

[0] how many I know
[1] how many know me
A [2]  [1]
B [0]  [2]
C [2]  [1]


// B is a celebrity
// If C-> B = False, then there is NO celebrity b/c B isn't known by everyone
// If B-> A = True, then there ALSO is NO celebrity b/c B can't know anyone
"""
from collections import defaultdict


def find_celebrity(contacts_list):
    # { 'A': (2,1)]}
    celebrity_map = defaultdict()
    for contact in contacts_list:
        person_a, person_b, know_each_other = contact
        if know_each_other:
            if person_a in celebrity_map:
                how_many_i_know, how_many_know_me = celebrity_map[person_a]
                celebrity_map[person_a] = (how_many_i_know + 1, how_many_know_me)
            if person_b in celebrity_map:
                how_many_i_know, how_many_know_me = celebrity_map[person_b]
                celebrity_map[person_b] = (how_many_i_know, how_many_know_me + 1)
            else:
                celebrity_map[person_a] = (1, 0)
                celebrity_map[person_b] = (0, 1)

    for person, data in celebrity_map.items():
        if data[0] == 0 and data[1] == len(celebrity_map) - 1:
            return person

    return None


"""
print(find_celebrity([
    ( "A", "B", True),
    ("B", "A", False),
    ("A", "C", True),
    ("C", "A", True), 
    ("B", "C", False),
    ("C", "B", True)])
)
"""
import unittest


class TestCelebrityFinder(unittest.TestCase):
    celebrity_testcases = [
        ([("A", "B", True),
          ("B", "A", False),
          ("A", "C", True),
          ("C", "A", True),
          ("B", "C", False),
          ("C", "B", True)], "B"),

        ([("A", "B", True),
          ("B", "A", False),
          ("A", "C", True),
          ("C", "A", True),
          ("B", "C", True),
          ("C", "B", True)], None),
    ]

    def test_celebrity_finder(self):
        for testcase, expected in self.celebrity_testcases:
            assert (find_celebrity(testcase) == expected), f"failed on input {testcase}"


unittest.main()