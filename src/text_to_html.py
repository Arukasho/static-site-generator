from textnode import TextType, TextNode
from leafnode import LeafNode

# class LeafNode(HTMLNode):
# def __init__(self, tag:str, value:str, props:dict=None):

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {f'"href": "{text_node.url}"'})
    elif text_node.text_type == TextType.IMAGES:
        return LeafNode("img", "", {f'"src": "{text_node.url}"', f'"alt": "{text_node.text}"'})