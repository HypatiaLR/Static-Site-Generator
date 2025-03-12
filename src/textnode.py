from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return text_to_leaf(text_node)
        case TextType.BOLD:
            return bold_to_leaf(text_node)
        case TextType.ITALIC:
            return italics_to_leaf(text_node)
        case TextType.CODE:
            return code_to_leaf(text_node)
        case TextType.LINK:
            return link_to_leaf(text_node)
        case TextType.IMAGE:
            return img_to_leaf(text_node)
        case _:
            raise ValueError
        
def text_to_leaf(text_node):
    html_node = LeafNode(text_node.text)
    return html_node

def bold_to_leaf(text_node):
    html_node = LeafNode(text_node.text, "b")
    return html_node

def italics_to_leaf(text_node):
    html_node = LeafNode(text_node.text, "i")
    return html_node

def code_to_leaf(text_node):
    html_node = LeafNode(text_node.text, "code")
    return html_node

def link_to_leaf(text_node):
    if text_node.url == None or text_node.url == "":
        raise ValueError
    if text_node.text == "":
        raise ValueError
    
    html_node = LeafNode(text_node.text, "a", {
        "href":text_node.url
    })
    return html_node

def img_to_leaf(text_node):
    if text_node.url == None or text_node.url == "":
        raise ValueError

    html_node = LeafNode("", "img", {
        "src":text_node.url,
        "alt":text_node.text
    })
    return html_node