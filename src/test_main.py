import unittest
from main import *


class TestMain(unittest.TestCase):
    def test(self):
        expected_list = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ]

        actual_list = main()

        self.assertEqual(expected_list, actual_list)

    """ def test2(self):
        expected_list = [
            TextNode("Lorem ipsum dolor sit amet", "bold"),
            TextNode(", consectetur adipiscing elit, ", "text"),
            TextNode("sed do eiusmod", "italic"),
            TextNode("", "text"),
            TextNode("tempor", "italic"),
            TextNode("incididunt ut labore et dolore ", "text"),
            TextNode("magna aliqua", "bold"),
            TextNode(". Ut enim ad minim veniam, ", "text"),
            TextNode("quis nostrud exercitation", "code"),
            TextNode(" ullamco laboris ", "text"),
            TextNode("nisi", "code"),
            TextNode(" ut aliquip ex ea commodo ", "text"),
            TextNode("consequat", "italic"),
            TextNode(". Duis ", "text"),
            TextNode("aute", "image", "google.com"),
            TextNode(" irure dolor in reprehenderit in ", "text"),
            TextNode("voluptate", "link", "hey.com"),
            TextNode(" velit esse cillum dolore ", "text"),
            TextNode("eu fugiat nulla pariatur", "bold"),
            TextNode(". Excepteur sint occaecat cupidatat non proident, ", "text"),
            TextNode("sunt in", "italic"),
            TextNode(" culpa qui officia deserunt mollit anim ", "text"),
            TextNode("id est laborum.", "bold"),
        ]

        actual_list = main()

        self.assertEqual(expected_list, actual_list) """


if __name__ == "__main__":
    unittest.main()
