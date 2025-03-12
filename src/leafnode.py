from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("node must have a value")
        if self.tag == None:
            return self.value
        props = self.props_to_html()
        if self.tag == "img":
            return f"<{self.tag}{props}>"
        html = f"<{self.tag}{props}>{self.value}</{self.tag}>"
        return html