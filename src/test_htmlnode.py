import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            tag="a",
            value="node value",
            children=[],
            props={"href": "https://www.google.com"},
        )
        props_repr = node.__repr__()
        expected = (
            "HTMLNode(tag='a' value='node value'"
            "children='[]' props='{'href': 'https://www.google.com'}')"
        )
        self.assertEqual(expected, props_repr)

    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            value="node value",
            children=[],
            props={"href": "https://www.google.com"},
        )
        props_html = node.props_to_html()
        expected = ' href="https://www.google.com"'
        self.assertEqual(expected, props_html)

    def test_props_to_html_no_props(self):
        node = HTMLNode(
            tag="a",
            value="node value",
            children=[],
        )
        props_html = node.props_to_html()
        expected = ""
        self.assertEqual(expected, props_html)


if __name__ == "__main__":
    unittest.main()
