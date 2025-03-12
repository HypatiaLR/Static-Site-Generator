import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class Test_ParentNode(unittest.TestCase):

    # empty/none tests
    def test_empty(self):
        h_node = ParentNode(None,None)
        self.assertRaises(ValueError, h_node.to_html)

    def test_none_tag(self):
        h_node = ParentNode(None,[LeafNode("test")])
        self.assertRaises(ValueError, h_node.to_html)
    
    def test_none_children(self):
        h_node = ParentNode("div",None)
        self.assertRaises(ValueError, h_node.to_html)

    def test_empty_tag(self):
        h_node = ParentNode("", [LeafNode("test")])
        self.assertRaises(ValueError, h_node.to_html)

    # single layer test
    def test_single_layer(self):
        h_node = ParentNode("p", [
            LeafNode("test_text", "b"),
            LeafNode(" more_text"),
            LeafNode(" slanty_text", "i"),
            LeafNode(" spanny_text", "span")
        ] )
        self.assertEqual(h_node.to_html(),'<p><b>test_text</b> more_text<i> slanty_text</i><span> spanny_text</span></p>')    

    # two layer test
    def test_two_layers(self):
        h_node = ParentNode("div", [
            LeafNode("test_text"),
            ParentNode("p",[
                LeafNode(" slanty_text", "i"),
                LeafNode(" spanny_text", "span")
            ]),
            LeafNode("exity_text", "a")
        ],{
            "href":"https://www.google.com",
            "test":"quilt",
            "test2":"quilty"
        })
        self.assertEqual(h_node.to_html(),'<div href="https://www.google.com" test="quilt" test2="quilty">test_text<p><i> slanty_text</i><span> spanny_text</span></p><a>exity_text</a></div>')

    def test_three_layers(self):
        h_node = ParentNode("div", [
            LeafNode("test_text"),
            ParentNode("p",[
                LeafNode(" slanty_text", "i"),
                LeafNode(" spanny_text", "span"),
                ParentNode("b",[
                    LeafNode(" slanty_text", "i"),
                    LeafNode(" spanny_text", "span")
                ])
            ]),
            LeafNode("exity_text", "a")
        ],{
            "href":"https://www.google.com",
            "test":"quilt",
            "test2":"quilty"
        })
        self.assertEqual(h_node.to_html(),'<div href="https://www.google.com" test="quilt" test2="quilty">test_text<p><i> slanty_text</i><span> spanny_text</span><b><i> slanty_text</i><span> spanny_text</span></b></p><a>exity_text</a></div>')