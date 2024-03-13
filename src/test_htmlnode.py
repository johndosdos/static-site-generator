import unittest

from htmlnode import *


class Test(unittest.TestCase):
    def test(self):
        print("\n================TEST START================")
        parentnode = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
            ],
        )

        print(parentnode.to_html())

        print("\n================TEST END================")


if __name__ == "__main__":
    unittest.main()
