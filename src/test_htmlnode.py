import unittest

from htmlnode import HTMLNode

class Test_HTMLNode(unittest.TestCase):
    def test_props_empty(self):
        h_node = HTMLNode()
        self.assertEqual(h_node.props_to_html(),"")

    def test_props_single(self):
        h_node = HTMLNode(props={
            "href":"https://www.google.com"
        })
        self.assertEqual(h_node.props_to_html(),' href="https://www.google.com"')

    def test_props_multiple(self):
        h_node = HTMLNode(props={
            "href":"https://www.google.com",
            "test":"quilt",
            "test2":"quilty"
        })
        self.assertEqual(h_node.props_to_html(),' href="https://www.google.com" test="quilt" test2="quilty"')