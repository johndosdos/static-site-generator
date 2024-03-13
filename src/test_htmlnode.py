import unittest

from htmlnode import HTMLNode, LeafNode


class Test(unittest.TestCase):
    def test(self):
        print("\n================TEST START================")
        leafnode = LeafNode("p", "hello world", {"id": "container", "class": "one"})
        self.assertEqual(
            leafnode.to_html(), '<p id="container" class="one">hello world</p>'
        )
        print(leafnode.to_html())
        print("\n================TEST END================")


if __name__ == "__main__":
    unittest.main()
