import unittest

'''
This test assumes your functions are named as follows:
    littlepiggy: Take in a single word and convert that single word to piglatin.
    bigpiggy: Take in a full sentence and convert it one word at a time to piglatin.

    validate: Take in a credit card number as a string and return True if valid, False if no.

Besides possibly changing the names of the functions you should make no other changes to this file.
'''

class PigLatinTest(unittest.TestCase):
    def test_single(self):
        import piglatin
        test_cases = [('glove', 'oveglay'),
            ('egg', 'eggway'),
            ('happy', 'appyhay'),
            ('inbox', 'inboxway')]

        for inword, outword in test_cases:
            with self.subTest(i=inword):
                self.assertEqual(piglatin.littlepiggy(inword),
                    outword)

    def test_sentence(self):
        import piglatin
        test_cases = [('Hello, how are you?', 'elloHay owhay areway ouyay')]

        for inword, outword in test_cases:
            with self.subTest(i = inword):
                self.assertEqual(piglatin.bigpiggy(inword),
                    outword)

class LuhnsTest(unittest.TestCase):
    def test_cc(self):
        import luhns
        test_cases = [("38520000023237", True),
                      ("49927398716", True),
                      ("49927398717", False),
                      ("1234567812345670", False),
                      ("1234567812345678", True)]
        for ccnum, valid in test_cases:
            with self.subTest(i=ccnum):
                self.assertEqual(luhns.validate(ccnum), valid)

if __name__ == '__main__':
    unittest.main()