import unittest

from htmlnode import HTMLNode


class Test(unittest.TestCase):
    def test1(self):
        children = []
        node = HTMLNode("a", "hello", None, {"href": "www.google.com"})
        children.append(node)
        node3 = HTMLNode("a", "world", None, {"href": "www.bing.com"})
        children.append(node3)
        node2 = HTMLNode("p", "this is a test", children, None)
        print(node2)

    def test2(self):
        node = HTMLNode("a", "hello", None, {"href": "www.google.com"})
        self.assertEqual(node.props_to_html(), f' href="www.google.com"')

        print(node)


if __name__ == "__main__":
    unittest.main()
