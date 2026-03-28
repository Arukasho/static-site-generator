import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.jumanji.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.jumanji.com")
        node2 = TextNode("Big big and biiiigggg", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.jumanji.com")
        node2 = TextNode("Big big and biiiigggg", TextType.CODE, None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()