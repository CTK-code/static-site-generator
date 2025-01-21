import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(tag="a", value="node value")
        expected = "<a>node value</a>"
        self.assertEqual(expected, node.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(value="node value")
        expected = "node value"
        self.assertEqual(expected, node.to_html())

    def test_to_html_props(self):
        node = LeafNode(
            tag="a", value="node value", props={"href": "https://www.google.com"}
        )
        expected = '<a href="https://www.google.com">node value</a>'
        self.assertEqual(expected, node.to_html())

    def test_repr(self):
        node = LeafNode(
            tag="a", value="node value", props={"href": "https://www.google.com"}
        )
        expected = (
            "LeafNode(tag='a' value='node value'"
            " props='{'href': 'https://www.google.com'}')"
        )
        self.assertEqual(expected, node.__repr__())


if __name__ == "__main__":
    unittest.main()
