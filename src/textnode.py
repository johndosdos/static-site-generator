class TextNode:
    def __init__(self, text, text_type, url=None):
        """
        Initialize the class with the provided text, text_type, and optional url.

        Parameters:
            text (str): The text to be stored.
            text_type (str): The type of text.
            url (str, optional): The URL associated with the text. Defaults to None.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type}, {self.url})'
