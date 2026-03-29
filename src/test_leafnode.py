import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode(None, "Jajajajaja")
        node3 = LeafNode("h1", "The Robust Elevator Strikes Again", {"href": "https://www.google.com"})
        node4 = LeafNode(None, "The Robust Elevator Strikes Again", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), "Jajajajaja")
        self.assertEqual(node3.to_html(), '<h1 href="https://www.google.com">The Robust Elevator Strikes Again</h1>')
        self.assertEqual(node4.to_html(), "The Robust Elevator Strikes Again")

if __name__ == "__main__":
    unittest.main()