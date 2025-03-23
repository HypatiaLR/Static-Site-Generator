import re

from textnode import TextType, TextNode

def split_node_delimiter(old_node, delimiter, text_type):
    if old_node.text_type != TextType.TEXT:
        return [old_node]
    split_nodes = []
    text_split_on_delimiter = old_node.text.split(delimiter)
    if len(text_split_on_delimiter) % 2 == 0:
        raise Exception("invalid Markdown syntax")
    for i in range(0, len(text_split_on_delimiter)):
        node = TextNode(text_split_on_delimiter[i], TextType.TEXT)
        if i % 2 != 0:
            node.text_type = text_type
        split_nodes.append(node)
    return split_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(split_node_delimiter(node, delimiter, text_type))
        else:
            new_nodes.extend([node])
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    ret_nodes = []
    for node in old_nodes:
        image_pairs = extract_markdown_images(node.text)
        text = node.text

        for image_pair in image_pairs:
            selections = text.split(f"![{image_pair[0]}]({image_pair[1]})", 1)
            if not selections[0] == "":
                ret_nodes.append(TextNode(selections[0], node.text_type))
            ret_nodes.append(TextNode(image_pair[0],TextType.IMAGE,image_pair[1]))
            text = selections[1]

        if text != "":
            ret_nodes.append(TextNode(text,node.text_type, node.url))

    return ret_nodes

def split_nodes_link(old_nodes):
    ret_nodes = []
    for node in old_nodes:
        link_pairs = extract_markdown_links(node.text)
        text = node.text

        for link_pair in link_pairs:
            selections = text.split(f"[{link_pair[0]}]({link_pair[1]})", 1)
            if not selections[0] == "":
                ret_nodes.append(TextNode(selections[0], node.text_type))
            ret_nodes.append(TextNode(link_pair[0],TextType.LINK,link_pair[1]))
            text = selections[1]

        if text != "":
            ret_nodes.append(TextNode(text, node.text_type, node.url))

    return ret_nodes

def text_to_textnodes(text):
    base_node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([base_node],"**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes