from textnode import TextNode
from htmlnode import *
import re


def extract_markdown_links(text):
    pattern = re.compile(r"\[(.*?)\]\((.*?)\)")
    matches = pattern.findall(text)

    title_url_list = [match for match in matches]
    return title_url_list


def extract_markdown_images(text):
    pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")
    matches = pattern.findall(text)

    alttext_imgurl_list = [match for match in matches]
    return alttext_imgurl_list


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    A function that splits nodes based on a delimiter, processes the text, and returns a list of split nodes.

    Parameters:
        old_nodes (list): A list of nodes to split.
        delimiter (str): The delimiter to split the nodes at.
        text_type (str): The type of text for the new nodes.

    Returns:
        list_split_nodes (list): A list of processed split nodes.
    """
    list_split_nodes = []

    for node in old_nodes:

        if node.text_type == "text":
            split_node_text = node.text.split(delimiter)

            for i, text in enumerate(split_node_text):
                # the word with delimiter will always have an odd index after the split,
                # provided that the delimiter is a pair.
                if i % 2 == 1:
                    list_split_nodes.append(TextNode(text, text_type))

                elif text != "":
                    list_split_nodes.append(TextNode(text, node.text_type))

        else:
            list_split_nodes.append(node)

    return list_split_nodes


def textnode_to_htmlnode(text_node):
    """
    Generate an HTML representation of a text node based on its text_type.

    Parameters:
        text_node (TextNode): The text node to be converted to HTML.

    Returns:
        LeafNode: An HTML representation of the text node.
    """
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
    node3 = TextNode("this is a `code block`", "text")

    # html_node1 = textnode_to_htmlnode(node1)
    # print(html_node1.to_html())

    # new_node = split_nodes_delimiter([node3], "`", "code")
    # print(new_node)

    image_text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
    extracted_alttext_imgurl = extract_markdown_images(image_text)
    print(extracted_alttext_imgurl)

    link_text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    extracted_title_url = extract_markdown_links(link_text)
    print(extracted_title_url)


main()
