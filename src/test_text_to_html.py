import unittest

from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node
from htmlnode import HTMLNode


class TestTexttoHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

        node = TextNode("This is a text node", TextType.IMAGES)
        html_node = text_node_to_html_node(node)
        print(html_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")

        node = TextNode("This is a text node", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        print(html_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()