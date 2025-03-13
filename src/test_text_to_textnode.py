import unittest

from textnode import TextNode, TextType
from text_to_textnode import split_nodes_delimiter, split_node_delimiter

class test_TextToTextNode(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(split_nodes_delimiter([],"**",TextType.BOLD),[])

    def test_single_text_node(self):
        t_node_list = [
            TextNode("this is a text node full of only text", TextType.TEXT)
            ]
        self.assertEqual(split_nodes_delimiter(t_node_list,"**",TextType.BOLD), t_node_list)

    def test_single_text_node_split_once(self):
        t_node_list = [
            TextNode("this is a text node with some **bold** text", TextType.TEXT)
            ]
        e_node_list = [
            TextNode("this is a text node with some ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(t_node_list,"**",TextType.BOLD), e_node_list)

    def test_incorrect_markup(self):
        t_node_list = [
            TextNode("this is a text node with some **bold** text**", TextType.TEXT)
            ]
        self.assertRaises(Exception, split_nodes_delimiter, t_node_list,"**",TextType.BOLD)

    def test_single_text_node_split_more(self):
        t_node_list = [
            TextNode("this **is** a **text** node **with** lots of **bold** text", TextType.TEXT)
            ]
        e_node_list = [
            TextNode("this ", TextType.TEXT),
            TextNode("is", TextType.BOLD),
            TextNode(" a ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" node ", TextType.TEXT),
            TextNode("with", TextType.BOLD),
            TextNode(" lots of ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(t_node_list,"**",TextType.BOLD), e_node_list)

    def test_multiple_text_node_split_more(self):
        t_node_list = [
            TextNode("this **is** a **text** node **with** lots of **bold** text", TextType.TEXT),
            TextNode("this is a text node with some **bold** text", TextType.TEXT),
            TextNode("this is a text node full of only text", TextType.TEXT),
            TextNode("this is a text node with some **bold** text", TextType.ITALIC)
            ]
        e_node_list = [
            TextNode("this ", TextType.TEXT),
            TextNode("is", TextType.BOLD),
            TextNode(" a ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" node ", TextType.TEXT),
            TextNode("with", TextType.BOLD),
            TextNode(" lots of ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("this is a text node with some ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("this is a text node full of only text", TextType.TEXT),
            TextNode("this is a text node with some **bold** text", TextType.ITALIC)
        ]
        self.assertEqual(split_nodes_delimiter(t_node_list,"**",TextType.BOLD), e_node_list)