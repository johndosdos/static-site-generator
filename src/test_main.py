import unittest
from main import *


class TestMain(unittest.TestCase):
    def test_testnodes_list(self):
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


if __name__ == "__main__":
    unittest.main()
