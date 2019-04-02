import unittest

class StringBuilder:
    def __init__(self):
        self.internal = []

    #O(1)
    def append(self, str):
        self.internal.append(str)

    #O(n)
    def getString(self):
        return ''.join(self.internal)

class Test(unittest.TestCase):
    def test_simple(self):
        myStringBuilder = StringBuilder()
        myStringBuilder.append('hello')
        myStringBuilder.append(' ')
        myStringBuilder.append('world')
        self.assertEqual(myStringBuilder.getString(), 'hello world')

if __name__ == "__main__":
    unittest.main()
