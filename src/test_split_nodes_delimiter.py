import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_split_node(self):
        node = [TextNode("This is text with a `code block` word", TextType.TEXT), ]
        new_nodes = split_nodes_delimiter(node, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                                        TextNode("This is text with a ", TextType.TEXT),
                                        TextNode("code block", TextType.CODE),
                                        TextNode(" word", TextType.TEXT),
                                    ]
                        )
        
    def test_split_node(self):
        node = [
            TextNode("This is text with a **bolded** word", TextType.TEXT),
            TextNode("A man", TextType.BOLD) 
            ]
        new_nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
                                        TextNode("This is text with a ", TextType.TEXT),
                                        TextNode("bolded", TextType.BOLD),
                                        TextNode(" word", TextType.TEXT),
                                        TextNode("A man", TextType.BOLD),
                                    ]
                        )

if __name__ == "__main__":
    unittest.main()