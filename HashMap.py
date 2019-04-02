import unittest

class HashMap:
    def __init__(self):
        self.internal = [None]*100

    # O(n)
    def insert(self, item):
       index = self.getHash(item[0])

       if self.internal[index]:
            self.internal[index].append(item)
       else:
            self.internal[index] = [item]

    # O(n)
    def get(self, target):
        index = self.getHash(target)
        if self.internal[index]:
            entries = self.internal[index]
            matches = [entry for entry in entries if entry[0] == target]
            return matches[0]
        else:
            return None

    # note: this hash method is not good enough, but for the sake of a small demo
    # to help me understand how this data structure works, it will suffice :)
    def getHash(self, str):
        return hash(str) % len(self.internal)

class Test(unittest.TestCase):
    def test_simple(self):
        myHashMap = HashMap()
        myHashMap.insert(('Daniel', '22'))
        self.assertEqual(myHashMap.get('Daniel'), ('Daniel', '22'))

    def test_multiple(self):
        myHashMap = HashMap()
        Daniel, Alina, Milan, Jehan, Peppy = ('Daniel', '22'), ('Alina', '24'), ('Milan', '59'), ('Jehan', '55'), ('Peppy', '4')
        myHashMap.insert(Daniel)
        myHashMap.insert(Alina)
        myHashMap.insert(Milan)
        myHashMap.insert(Jehan)
        myHashMap.insert(Peppy)
        self.assertEqual(myHashMap.get('Daniel'), Daniel)
        self.assertEqual(myHashMap.get('Alina'), Alina)
        self.assertEqual(myHashMap.get('Milan'), Milan)
        self.assertEqual(myHashMap.get('Jehan'), Jehan)
        self.assertEqual(myHashMap.get('Peppy'), Peppy)

    def test_empty(self):
        myHashMap = HashMap()
        self.assertEqual(myHashMap.get('Daniel'), None)

if __name__ == "__main__":
    unittest.main()
