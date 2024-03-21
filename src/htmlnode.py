class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initializes the class with the given tag, value, children, and props.

        Parameters:
            tag (optional): The tag for the element.
            value (optional): The value associated with the element.
            children (optional): The children elements.
            props (optional): The properties of the element.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        html_out = ""

        for key, value in self.props.items():
            html_out += f' {key}="{value}"'

        return html_out

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value and self.tag != "img":
            raise ValueError

        if not self.tag:
            return self.value

        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        html_out = self.props_to_html()

        return f"<{self.tag}{html_out}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag argument is empty")

        if not self.children:
            raise ValueError("Children argument is empty")

        html_out = ""
        for child in self.children:
            html_out += child.to_html()

        return f"<{self.tag}>{html_out}</{self.tag}>"
