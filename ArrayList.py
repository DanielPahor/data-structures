import unittest

class ArrayList:
    def __init__(self):
        self.internal = [None] * 4
        self.index  = -1

    # O(n)
    # amortized O(1)
    def add(self, item):
       self.index += 1

       if self.index > len(self.internal)-1:
           temp = self.internal
           self.internal = [None] * len(self.internal) * 2

           for i, val in enumerate(temp):
               self.internal[i] = val

           self.internal[self.index] = item
       else:
           self.internal[self.index] = item

    # O(1)
    def get(self, index):
       return self.internal[index]

class Test(unittest.TestCase):
    def test_simple(self):
        myArrayList = ArrayList()
        myArrayList.add(0)
        myArrayList.add(1)
        myArrayList.add(2)
        myArrayList.add(3)
        myArrayList.add(4)

        self.assertEqual(len(myArrayList.internal), 8)
        self.assertEqual(myArrayList.get(4), 4)

if __name__ == "__main__":
    unittest.main()
