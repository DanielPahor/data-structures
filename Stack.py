import unittest
import collections

class Stack:
    def __init__(self):
        self.data = [];

    #O(1)
    def push(self, item):
        self.data.append(item)

    #O(1)
    def pop(self):
        if not self.data:
            return None
        else:
            return self.data.pop()

    #O(1)
    def peek(self):
        if not self.data:
            return None
        else:
            return self.data[-1]

class Test(unittest.TestCase):
    def test_push(self):
        stack = Stack()

        stack.push('a')
        self.assertEqual(stack.data[0], 'a')

        stack.push('b')
        self.assertEqual(stack.data[1], 'b')

    def test_pop(self):
        stack = Stack()

        stack.push('a')
        element = stack.pop()

        self.assertTrue(element, 'a')
        self.assertIsNone(stack.pop())

    def test_peek(self):
        stack = Stack()

        stack.push('a')
        self.assertEqual(stack.peek(), 'a')

if __name__ == "__main__":
    unittest.main()
