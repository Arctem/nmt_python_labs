import unittest
import luhns

class TestLab9(unittest.TestCase):
    tests = [{"i": "38520000023237", "o": True},
             {"i": "49927398716", "o": True},
             {"i": "49927398717", "o": False},
             {"i": "1234567812345670", "o": False},
             {"i": "1234567812345678", "o": True}]

    def test_ex1(self):
        # run subtests, one for each test input
        for test in TestLab9.tests:
            # know which test file caused the code for the exercise to fail
            with self.subTest(i=test):
                # test the function!
                self.assertEqual(luhns.validate(test["i"]), test["o"])

if __name__ == '__main__':
    unittest.main()
