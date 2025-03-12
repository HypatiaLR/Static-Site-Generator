import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode

class Test_TextNode_Conv(unittest.TestCase):
    def test_invalid(self):
        t_node = TextNode("wrongy_text", 23)
        self.assertRaises(ValueError, text_node_to_html_node, t_node)

    def test_text(self):
        t_node = TextNode("basicy_text",TextType.TEXT)
        l_node = text_node_to_html_node(t_node)
        self.assertEqual(l_node.to_html(), "basicy_text")

    def test_bold(self):
        t_node = TextNode("boldy_text",TextType.BOLD)
        l_node = text_node_to_html_node(t_node)
        self.assertEqual(l_node.to_html(), "<b>boldy_text</b>")

    def test_italic(self):
        t_node = TextNode("slanty_text",TextType.ITALIC)
        l_node = text_node_to_html_node(t_node)
        self.assertEqual(l_node.to_html(), "<i>slanty_text</i>")

    def test_code(self):
        t_node = TextNode("cody_text",TextType.CODE)
        l_node = text_node_to_html_node(t_node)
        self.assertEqual(l_node.to_html(), "<code>cody_text</code>")

    def test_link_no_url(self):
        t_node = TextNode("linky_text",TextType.LINK)
        self.assertRaises(ValueError, text_node_to_html_node, t_node)

    def test_link_empty_url(self):
        t_node = TextNode("linky_text",TextType.LINK, "")
        self.assertRaises(ValueError, text_node_to_html_node, t_node)

    def test_link_no_anchor(self):
        t_node = TextNode("",TextType.LINK, "https://www.google.com")
        self.assertRaises(ValueError, text_node_to_html_node, t_node)

    def test_link_good(self):
        t_node = TextNode("linky_text",TextType.LINK, "https://www.google.com")
        l_node = text_node_to_html_node(t_node)
        self.assertEqual(l_node.to_html(),'<a href="https://www.google.com">linky_text</a>')

    def test_link_no_url(self):
        t_node = TextNode("linky_text",TextType.IMAGE)
        self.assertRaises(ValueError, text_node_to_html_node, t_node)

    def test_link_empty_url(self):
        t_node = TextNode("linky_text",TextType.IMAGE, "")
        self.assertRaises(ValueError, text_node_to_html_node, t_node)

    def test_link_good(self):
        t_node = TextNode("imagey_text",TextType.IMAGE, "https://www.google.com")
        l_node = text_node_to_html_node(t_node)
        self.assertEqual(l_node.to_html(),'<img src="https://www.google.com" alt="imagey_text">')