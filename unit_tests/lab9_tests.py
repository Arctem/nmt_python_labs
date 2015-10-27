import unittest
import luhns

class TestLab9(unittest.TestCase):
    tests = [{i: "38520000023237", o: True}, ]

    def test_ex1(self):
        # run subtests, one for each test input
        for test in TestLab99.tests:
            # know which test file caused the code for the exercise to fail
            with self.subTest(i=test):
                # test the function!
                self.assertEqual(luhns.validate(test.i, test.o))

if __name__ == '__main__':
    unittest.main()
