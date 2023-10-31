from jupiter import LetterCompiler

import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
       # self.assertEqual(LetterCompiler(___), ___)
        self.assertEqual(LetterCompiler(testcase), expected)
"""Yikes! SystemExit: True means an error occurred, as expected. The reason is that unittest.main( )
looks at sys.argv. In Jupyter, by default, the first parameter of sys.argv is what started the Jupyter kernel
which is not the case when executing it from the command line. This default parameter is passed into unittest.main( )
as an attribute when you don't explicitly pass it attributes and is therefore what causes the error about the kernel
connection file not being a valid attribute. Passing an explicit list to unittest.main( ) prevents it from looking
at sys.argv.

Let's pass it the list ['first-arg-is-ignored'] for example. In addition, we will pass it the parameter
exit = False to prevent unittest.main( ) from shutting down the kernel process.
Run the following cell with the argv and exit parameters passed into unittest.main( ) to rerun your automatic test.
unittest.main(argv = ['first-arg-is-ignored'], exit = False)
"""


class TestCompiler2(unittest.TestCase):

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    # EDGE CASES HERE
    def test_three(self):
        testcase = ""
        expected = ""
        self.assertEqual(LetterCompiler(testcase), expected)

# unittest.main()

unittest.main(argv=['first-arg-is-ignored'], exit=False)
