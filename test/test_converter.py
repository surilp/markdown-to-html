from unittest import TestCase
from src.converter import MarkdownToHTMLConverter as html_converter


class MarkdownToHTMLConverterTest(TestCase):

    def test_header_1_logic(self):
        markdown = "# Heading 1"
        expected = "<h1>Heading 1</h1>"
        actual = html_converter._header_logic(markdown, 0, len(markdown))
        self.assertEqual(expected, actual)

    def test_header_1_in_correct_syntax_logic(self):
        markdown = "#Heading 1"
        expected = "<p>#Heading 1</p>"
        actual = html_converter._header_logic(markdown, 0, len(markdown))
        self.assertEqual(expected, actual)

    def test_header_2_logic(self):
        markdown = "## Heading 2"
        expected = "<h2>Heading 2</h2>"
        actual = html_converter._header_logic(markdown, 0, len(markdown))
        self.assertEqual(expected, actual)

    def test_header_3_logic(self):
        markdown = "### Heading 3"
        expected = "<h3>Heading 3</h3>"
        actual = html_converter._header_logic(markdown, 0, len(markdown))
        self.assertEqual(expected, actual)

    def test_header_4_logic(self):
        markdown = "#### Heading 4"
        expected = "<h4>Heading 4</h4>"
        actual = html_converter._header_logic(markdown, 0, len(markdown))
        self.assertEqual(expected, actual)

    def test_header_5_logic(self):
        markdown = "##### Heading 5"
        expected = "<h5>Heading 5</h5>"
        actual = html_converter._header_logic(markdown, 0, len(markdown))
        self.assertEqual(expected, actual)

    def test_header_6_logic(self):
        markdown = "###### Heading 6"
        expected = "<h6>Heading 6</h6>"
        actual = html_converter._header_logic(markdown, 0, len(markdown))
        self.assertEqual(expected, actual)

    def test_paragraph_logic(self):
        markdown = "Unformatted text"
        expected = "<p>Unformatted text</p>"
        actual = html_converter._paragraph_logic(markdown, 0, len(markdown))
        self.assertEqual(expected, actual)

    def test_link_logic(self):
        markdown = "[Link text](https://www.example.com)"
        expected = '<a href="https://www.example.com">Link text</a>'
        actual = html_converter._link_logic(markdown, 0, len(markdown))
        self.assertEqual(expected, actual)

    def test_blank_line(self):
        markdown = ""
        expected = ""
        actual = html_converter.convert(markdown)
        self.assertEqual(expected, actual)

    def test_multi_string_markdown_1(self):
        markdowns = \
            '''# Sample Document

Hello!

This is sample markdown for the [Mailchimp](https://www.mailchimp.com) homework assignment.'''
        expected = \
            '''<h1>Sample Document</h1>

<p>Hello!</p>

<p>This is sample markdown for the <a href="https://www.mailchimp.com">Mailchimp</a> homework assignment.</p>'''
        actual = '\n'.join(html_converter.convert_multi_string_markdown(markdowns))
        self.assertEqual(expected, actual)

    def test_multi_string_markdown_2(self):
        markdowns = \
            '''# Header one

Hello there

How are you?
What's going on?

## Another Header

This is a paragraph [with an inline link](http://google.com). Neat, eh?

## This is a header [with a link](http://yahoo.com)'''
        expected = \
            '''<h1>Header one</h1>

<p>Hello there</p>

<p>How are you?
What's going on?</p>

<h2>Another Header</h2>

<p>This is a paragraph <a href="http://google.com">with an inline link</a>. Neat, eh?</p>

<h2>This is a header <a href="http://yahoo.com">with a link</a></h2>'''
        actual = '\n'.join(html_converter.convert_multi_string_markdown(markdowns))
        self.assertEqual(expected, actual)