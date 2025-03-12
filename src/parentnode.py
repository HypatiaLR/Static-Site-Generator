from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("parent node must have a tag")
        if self.children == None or len(self.children) == 0:
            raise ValueError("parent node must have at least one child")
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"
        return html

