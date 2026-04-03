from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif delimiter not in node.text:
            raise Exception(f"No delimiter found for text type {text_type}. Invalid markdown syntax.")
        else:
            splitted = node.text.split(delimiter)
            if len(splitted) < 3:
                raise Exception("No matching delimiter found. Invalid markdown syntax.")
            else:
                new_nodes.append(TextNode(splitted[0],node.text_type))
                new_nodes.append(TextNode(splitted[1],text_type))
                new_nodes.append(TextNode(splitted[2],node.text_type))

    print(new_nodes)
    return new_nodes
