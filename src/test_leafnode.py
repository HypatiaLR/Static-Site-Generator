import unittest

from leafnode import LeafNode

class Test_LeafNode(unittest.TestCase):
    def test_empty(self):
        h_node = LeafNode(None)
        self.assertRaises(ValueError, h_node.to_html)

    def test_props_no_tag(self):
        h_node = LeafNode("testing words are tested",props={
            "href":"https://www.google.com"
        })
        self.assertEqual(h_node.to_html(),'testing words are tested')

    def test_tag_props(self):
        h_node = LeafNode("testing words are tested", "p", props={
            "href":"https://www.google.com"
        })
        self.assertEqual(h_node.to_html(),'<p href="https://www.google.com">testing words are tested</p>')    

    def test_tag_multiple_props(self):
        h_node = LeafNode("testing words are tested", "h1", props={
            "href":"https://www.google.com",
            "test":"quilt",
            "test2":"quilty"
        })
        self.assertEqual(h_node.to_html(),'<h1 href="https://www.google.com" test="quilt" test2="quilty">testing words are tested</h1>')