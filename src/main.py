from textnode import TextNode
from htmlnode import *
import re


def extract_markdown_links(text):
    pattern = re.compile(r"\[(.*?)\]\((.*?)\)")
    matches = pattern.findall(text)

    return matches


def extract_markdown_images(text):
    pattern = re.compile(r"!\[(.*?)\]\((.*?)\)")
    matches = pattern.findall(text)

    return matches


def split_nodes_image(old_nodes):
    img_textnodes_list = []

    for node in old_nodes:
        string_list = re.split(r"(!\[.*?\]\(.*?\))", node.text)

        for idx, string in enumerate(string_list):
            if idx % 2 == 1:
                split_md_image = extract_markdown_images(string)
                img_textnodes_list.append(
                    TextNode(split_md_image[0][0], "image", split_md_image[0][1])
                )

            elif string != "":
                img_textnodes_list.append(TextNode(string, "text"))

    return img_textnodes_list


def split_nodes_link(old_nodes):
    link_textnodes_list = []

    for node in old_nodes:
        string_list = re.split(r"(\[.*?\]\(.*?\))", node.text)

        for idx, string in enumerate(string_list):
            if idx % 2 == 1:
                split_md_link = extract_markdown_links(string)
                link_textnodes_list.append(
                    TextNode(split_md_link[0][0], "link", split_md_link[0][1])
                )

            elif string != "":
                link_textnodes_list.append(TextNode(string, "text"))

    return link_textnodes_list


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
    text = "This is a text containing a link: [google](https://www.google.com/)"
    link_textnode = TextNode(text, "link")
    link_textnodes_list = split_nodes_link([link_textnode])


main()
