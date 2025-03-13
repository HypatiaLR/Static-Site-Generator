from textnode import TextType, TextNode

def split_node_delimiter(old_node, delimiter, text_type):
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

