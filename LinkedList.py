import unittest
import collections

class Node:
    def __init__(self, data, next = None):
        self.element = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head

    #O(n)
    def insert(self, next):
        node = self.head
        while node.next:
            node = node.next

        node.next = next

    #O(n)
    def remove(self, element):
        node = self.head
        prev = None

        while node:
            if node.element == element:
                if prev:
                    prev.next = node.next
                else:
                    self.head = self.head.next

            prev = node
            node = node.next

    #O(n)
    def get(self, element):
        node = self.head
        while node:
            if node.element == element:
                return node
            node = node.next
        return None

class Test(unittest.TestCase):
    def test_add_node(self):
        head = Node('a', Node('b', Node('c')));
        ll = LinkedList(head);
        ll.insert(Node('d'));
        self.assertEqual(head.element, 'a');
        self.assertEqual(head.next.element, 'b');
        self.assertEqual(head.next.next.element, 'c');
        self.assertEqual(head.next.next.next.element, 'd');

    def test_remove_node(self):
        head = Node('a', Node('b', Node('c')));
        ll = LinkedList(head);
        ll.remove('c');
        self.assertEqual(head.element, 'a');
        self.assertEqual(head.next.element, 'b');

    def test_get_node(self):
        head = Node('a', Node('b', Node('c')));
        ll = LinkedList(head);

        node = ll.get('c');
        self.assertEqual(node.element, 'c');

        node = ll.get('d');
        self.assertEqual(node, None);

if __name__ == "__main__":
    unittest.main()
