from textnode import TextNode
from htmlnode import *


def textnode_to_htmlnode(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text, None)

    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text, None)

    if text_node.text_type == "italic":
        return LeafNode("i", text_node.text, None)

    if text_node.text_type == "code":
        return LeafNode("code", text_node.text, None)

    if text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": ""})

    raise Exception("Invalid TextNode text_type")


def main():
    node1 = TextNode("hello world", "link", "google.com")
    node2 = TextNode("hello world", "bold", "google.com")

    html_node1 = textnode_to_htmlnode(node1)
    print(html_node1.to_html())


main()
