import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("NOT THE SAME", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_exception(self):
        node = TextNode("Regular Text", 99)
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_text_node_to_html_node_text(self):
        node = TextNode("Regular Text", TextType.TEXT)
        result = text_node_to_html_node(node)
        expected = LeafNode(value="Regular Text")
        self.assertEqual(result, expected)

    def test_text_node_to_html_node_bold(self):
        node = TextNode("Bold Text", TextType.BOLD)
        result = text_node_to_html_node(node)
        expected = LeafNode(value="Bold Text", tag="b")
        self.assertEqual(result, expected)

    def test_text_node_to_html_node_italic(self):
        node = TextNode("Italic Text", TextType.ITALIC)
        result = text_node_to_html_node(node)
        expected = LeafNode(value="Italic Text", tag="i")
        self.assertEqual(result, expected)

    def test_text_node_to_html_node_code(self):
        node = TextNode("Code Text", TextType.CODE)
        result = text_node_to_html_node(node)
        expected = LeafNode(value="Code Text", tag="code")
        self.assertEqual(result, expected)

    def test_text_node_to_html_node_link(self):
        node = TextNode("Link Text", TextType.LINK, url="https://google.com")
        result = text_node_to_html_node(node)
        expected = LeafNode(
            value="Link Text", tag="a", props={"href": "https://google.com"}
        )
        self.assertEqual(result, expected)

    def test_text_node_to_html_node_image(self):
        node = TextNode("Image Text", TextType.IMAGE, url="https://pic.link")
        result = text_node_to_html_node(node)
        expected = LeafNode(
            tag="img", props={"src": "https://pic.link", "alt": "Image Text"}
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
