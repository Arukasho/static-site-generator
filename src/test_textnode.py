import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        node3 = TextNode("This is a text node", TextType.BOLD, "www.jumanji.com")
        node4 = TextNode("This is a text node", TextType.BOLD)
        node5 = TextNode("This is a text node", TextType.BOLD, "www.jumanji.com")
        node6 = TextNode("Big big and biiiigggg", TextType.BOLD)
        node7 = TextNode("This is a text node", TextType.BOLD, "www.jumanji.com")
        node8 = TextNode("Big big and biiiigggg", TextType.CODE, None)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node5, node6)
        self.assertNotEqual(node7, node8)

if __name__ == "__main__":
    unittest.main()