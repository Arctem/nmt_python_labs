"""
This file is basic example of a unit test for the labs.
The TestClass keeps a list of filenames which refer to sample input and
corresponding output files.

The test_ex1 function tries to pass the contents of each lab99_ex1_*.in to the
function in the "doubler.py" file; output should match that in lab99_ex1_.*out.

Use ``python3 lab99_tests.py -v`` to run tests.
"""


# ideas:
# tarball the tests, have students decompress the files
# make sure students know how to run the tests
# have .tex read test cases and insert them into the exercises
# change exercises to require filename as argument to main (use default args)
#   and have strict return type requirements
#   can also redirect stdout; or offer students the option

# have the TestCase class make sure filenames are valid

import unittest
import doubler

def get_output(fname):
    return fname + ".expected_output"

def get_input(fname):
    return fname + ".expected_input"

class TestLab99(unittest.TestCase):
    ex1_test_fnames = ["lab99_ex1_easy", "lab99_ex1_hard", "lab99_ex1_odd"]

    def test_ex1(self):
        # run subtests, one for each test input
        for test in TestLab99.ex1_test_fnames:
            # know which test file caused the code for the exercise to fail
            with self.subTest(i=test):
                with open(get_output(test)) as f:
                    # test the function!
                    self.assertEqual(doubler.d(get_input(test)),
                                     f.read().split()[0])

if __name__ == '__main__':
    unittest.main()
