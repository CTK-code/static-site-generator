import unittest

from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Header"
        actual = extract_title(markdown)
        expected = "Header"
        self.assertEqual(expected, actual)

    def test_extract_title_no_header(self):
        markdown = "## Header"
        with self.assertRaises(Exception):
            extract_title(markdown)
