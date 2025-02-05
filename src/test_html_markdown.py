import unittest

from html_markdown import (
    markdown_to_code,
    markdown_to_code_node,
    markdown_to_header_node,
    markdown_to_html_nodes,
    markdown_to_paragraph_node,
    markdown_to_quote_node,
    markdown_to_unordered_list,
    markdown_to_ordered_list,
    markdown_to_list_nodes,
)
from htmlnode import ParentNode, LeafNode


class TestMarkdownHTMLNode(unittest.TestCase):
    def test_markdown_to_html_nodes(self):
        block = (
            "This is just a paragraph\n\n"
            + "> Quote 1\n> Quote 2\n\n"
            + "* List Item 1\n* List Item 2\n\n"
            + "## Header2!\n\n"
            + "```CODE BLOCK```\n\n"
        )
        actual = markdown_to_html_nodes(block)
        paragrah_expected = ParentNode(
            "p", [LeafNode(None, "This is just a paragraph")]
        )
        quote_expected = ParentNode(
            "blockquote",
            children=[
                ParentNode("p", [LeafNode(None, "Quote 1")]),
                ParentNode("p", [LeafNode(None, "Quote 2")]),
            ],
        )
        list_expected = ParentNode(
            "ul",
            children=[
                ParentNode("li", [LeafNode(None, "List Item 1")]),
                ParentNode("li", [LeafNode(None, "List Item 2")]),
            ],
        )
        header_expected = ParentNode("h2", [LeafNode(None, "Header2!")])
        code_expected = ParentNode(
            "pre", children=[ParentNode("code", [LeafNode(None, "CODE BLOCK")])]
        )
        expected = ParentNode(
            "div",
            children=[
                paragrah_expected,
                quote_expected,
                list_expected,
                header_expected,
                code_expected,
            ],
        )
        self.assertEqual(expected, actual)

    def test_markdown_to_list_nodes(self):
        block = """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        actual = markdown_to_list_nodes(block, "ul")
        expected = ParentNode(
            "ul",
            children=[
                ParentNode(
                    "li",
                    [LeafNode(None, "This is the first list item in a list block")],
                ),
                ParentNode("li", [LeafNode(None, "This is a list item")]),
                ParentNode("li", [LeafNode(None, "This is another list item")]),
            ],
        )
        self.assertEqual(expected, actual)

    def test_markdown_to_header_node(self):
        block = "#### Header!"
        actual = markdown_to_header_node(block)
        expected = ParentNode("h4", [LeafNode(None, "Header!")])
        self.assertEqual(expected, actual)

    def test_markdown_to_code_node(self):
        block = "``` This is a code block ```"
        actual = markdown_to_code_node(block)
        expected = ParentNode(
            "pre",
            children=[ParentNode("code", [LeafNode(None, " This is a code block ")])],
        )
        self.assertEqual(expected, actual)

    def test_markdown_paragraph_node(self):
        block = "This is just a paragraph"
        actual = markdown_to_paragraph_node(block)
        expected = ParentNode("p", [LeafNode(None, "This is just a paragraph")])
        self.assertEqual(expected, actual)

    def test_markdown_to_quote_node(self):
        block = "> Quote 1\n> Quote 2"
        actual = markdown_to_quote_node(block)
        expected = ParentNode(
            "blockquote",
            children=[
                ParentNode("p", [LeafNode(None, "Quote 1")]),
                ParentNode("p", [LeafNode(None, "Quote 2")]),
            ],
        )
        self.assertEqual(expected, actual)


class TestHtmlMarkdown(unittest.TestCase):
    def test_markdown_to_unordered_list(self):
        block = """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        actual = markdown_to_unordered_list(block)
        expected = "<ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul>"
        self.assertEqual(expected, actual)

    def test_markdown_to_unordered_list_dash(self):
        block = """- This is the first list item in a list block
- This is a list item
- This is another list item"""
        actual = markdown_to_unordered_list(block)
        expected = "<ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul>"
        self.assertEqual(expected, actual)

    def test_markdown_to_ordered_list(self):
        block = """1. This is the first list item in a list block
2. This is a list item
3. This is another list item"""
        actual = markdown_to_ordered_list(block)
        expected = "<ol><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ol>"
        self.assertEqual(expected, actual)

    def test_markdown_to_code(self):
        block = "``` This is a code block ```"
        actual = markdown_to_code(block)
        expected = "<pre><code> This is a code block </code></pre>"
        self.assertEqual(expected, actual)
