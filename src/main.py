from textnode import TextNode
from htmlnode import *
import re


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
        if re.search(r"(!\[.*?\]\(.*?\))", node.text):
            string_list = re.split(r"(!\[.*?\]\(.*?\))", node.text)

            for idx, string in enumerate(string_list):
                if idx % 2 == 1:
                    split_md_image = extract_markdown_images(string)
                    img_textnodes_list.append(
                        TextNode(split_md_image[0][0], "image", split_md_image[0][1])
                    )

                elif string != "":
                    img_textnodes_list.append(TextNode(string, "text"))

        else:
            img_textnodes_list.append(node)

    return img_textnodes_list


def split_nodes_link(old_nodes):
    link_textnodes_list = []

    for node in old_nodes:
        if re.search(r"(\[.*?\]\(.*?\))", node.text):
            string_list = re.split(r"(\[.*?\]\(.*?\))", node.text)

            for idx, string in enumerate(string_list):
                if idx % 2 == 1:
                    split_md_link = extract_markdown_links(string)
                    link_textnodes_list.append(
                        TextNode(split_md_link[0][0], "link", split_md_link[0][1])
                    )

                elif string != "":
                    link_textnodes_list.append(TextNode(string, "text"))

        else:
            link_textnodes_list.append(node)

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


def markdown_to_blocks(markdown):
    if not markdown:
        return []

    block_list = []
    blocks = re.split(r"\n\n", markdown)

    for block in blocks:
        if re.search(r"\S", block):
            block_list.append(block.strip(" \n"))

    return block_list


def block_to_block_type(markdown):
    HEADING_1 = r"^\#\s"
    HEADING_2 = r"^\#{2}\s"
    HEADING_3 = r"^\#{3}\s"
    HEADING_4 = r"^\#{4}\s"
    HEADING_5 = r"^\#{5}\s"
    HEADING_6 = r"^\#{6}\s"
    CODE = r"^\`{3}[\s\S]*?\`{3}$"
    QUOTE = r"\>\s"
    UNORDERED_LIST = r"[\*|\-]\s"
    ORDERED_LIST = r"\d.\s"

    if re.match(HEADING_1, markdown):
        return "h1"

    if re.match(HEADING_2, markdown):
        return "h2"

    if re.match(HEADING_3, markdown):
        return "h3"

    if re.match(HEADING_4, markdown):
        return "h4"

    if re.match(HEADING_5, markdown):
        return "h5"

    if re.match(HEADING_6, markdown):
        return "h6"

    if re.search(CODE, markdown):
        return "code"

    if re.match(QUOTE, markdown):
        return "blockquote"

    if re.match(UNORDERED_LIST, markdown):
        return "ul"

    if re.match(ORDERED_LIST, markdown):
        return "ol"

    return "p"


def text_to_textnodes(text):
    node_list = [TextNode(text, "text")]
    node_list = split_nodes_delimiter(node_list, "**", "bold")
    node_list = split_nodes_delimiter(node_list, "*", "italic")
    node_list = split_nodes_delimiter(node_list, "`", "code")
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)

    return node_list


def main():
    heading_block = "# This is a heading"
    code_block = """```
code

block

```"""
    quote_block = "> This is a quote block"
    ul_block = """* This
* is an
* unordered list"""
    ol_block = """1. This
2. is an
3. ordered list"""
    paragraph_block = "This is a normal block"
    inline_block = "*Hello*"

    result = block_to_block_type(code_block)
    return result


main()
