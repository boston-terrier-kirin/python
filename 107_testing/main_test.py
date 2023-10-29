import unittest
import main


# https://docs.python.org/ja/3/library/unittest.html#assert-methods
class TestMain(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_do_stuff(self):
        param = 10
        result = main.do_stuff(param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        param = "testtest"
        result = main.do_stuff(param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        param = None
        result = main.do_stuff(param)
        self.assertEqual(result, 0)

    def test_do_stuff4(self):
        param = ""
        result = main.do_stuff(param)
        self.assertEqual(result, 0)

    def test_do_stuff5(self):
        param = 0
        result = main.do_stuff(param)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
