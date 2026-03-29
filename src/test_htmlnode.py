import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a new paragraph.", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "This is a new paragraph.", None, {"href": "https://www.google.com"})
        node3 = HTMLNode("b", None, [node, node2], None)

if __name__ == "__main__":
    unittest.main()