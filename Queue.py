import unittest
import collections

# max capacity 100
class Queue:
    def __init__(self):
        self.data = []

    #O(1)
    def enqueue(self, item):
        self.data.append(item)

    #O(n) in this implementation
    #O(1) for an optimal implementation
    def dequeue(self):
        if not self.data:
            return None
        else:
            return self.data.pop(0)

class Test(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()

        queue.enqueue('a')
        self.assertEqual(queue.data[0], 'a')

        queue.enqueue('b')
        self.assertEqual(queue.data[1], 'b')

    def test_dequeue(self):
        queue = Queue()

        queue.enqueue('a')
        queue.enqueue('b')

        self.assertEqual(queue.dequeue(), 'a')

if __name__ == "__main__":
    unittest.main()
