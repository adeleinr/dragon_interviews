import unittest


def is_schedule_conflict(appointments:list):
    if len(list) == 1:
        return True
    appointments.sort()
    for i in range(appointments):
        for j in range(i+1, appointments):
            if appointments[j][0] <= appointments[i][1]:
                return False
    return True


class Test(unittest.TestCase):
    testcases = [
        ([[1, 5], [3, 7], [2, 6], [10, 15], [5, 6], [4, 100]], False),
        ([[1, 5], [7, 10]], True),
    ]

    def check_is_schedule_conflict(self):
        for testcase in self.testcases:
            assert is_schedule_conflict(testcase[0]) == testcase[1]


unittest.main()