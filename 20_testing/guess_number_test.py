import unittest
import guess_number


class TestGuessNumber(unittest.TestCase):
    def test_input(self):
        result = guess_number.run_guess(5, 5)
        self.assertTrue(result)

    def test_input2(self):
        result = guess_number.run_guess(5, 1)
        self.assertFalse(result)

    def test_input3(self):
        result = guess_number.run_guess(15, 1)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
