import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test2(self):
        node = TextNode("check 1", "italic")
        node2 = TextNode("hello world", "bold", "www.google.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
