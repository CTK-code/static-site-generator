import unittest

from block_markdown import block_to_block_type, markdown_to_block


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_block(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        actual = markdown_to_block(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
        ]

        self.assertListEqual(expected, actual)

    def test_markdown_to_block_empty(self):
        markdown = ""
        actual = markdown_to_block(markdown)
        expected = [""]
        self.assertListEqual(expected, actual)

    def test_block_to_block_type_code(self):
        block = "``` CODE!!! ```"
        actual = block_to_block_type(block)
        expected = "code"
        self.assertEqual(expected, actual)

    def test_block_to_block_type_unodered_list(self):
        block = """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        actual = block_to_block_type(block)
        expected = "unordered_list"
        self.assertEqual(expected, actual)

    def test_block_to_block_type_odered_list(self):
        block = """1. This is the first list item in a list block
2. This is a list item
3. This is another list item"""
        actual = block_to_block_type(block)
        expected = "ordered_list"
        self.assertEqual(expected, actual)

    def test_block_to_block_type_heading(self):
        block = "# CODE!!!"
        actual = block_to_block_type(block)
        expected = "heading"
        self.assertEqual(expected, actual)

    def test_block_to_block_type_quote(self):
        block = """> This is the first list item in a list block
> This is a list item
> This is another list item"""
        actual = block_to_block_type(block)
        expected = "quote"
        self.assertEqual(expected, actual)
