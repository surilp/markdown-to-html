from src.converter import MarkdownToHTMLConverter


def markdown_to_html():
    while True:
        print('Type in or paste markdown')
        print('Type in "convert" to get html')
        print('Type in "quit" to exit')
        print('-----------Start of User Input(Markdown) ------------------')
        markdowns = get_user_input()
        if not markdowns:
            print('Thank you for using the converter')
            break
        print('-----------End of User Input(Markdown) --------------------')
        print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        html = MarkdownToHTMLConverter.convert_multi_string_markdown(markdowns)
        print('-----------Start of Output(HTML) ------------------')
        print(html)
        print('-----------End of Output(HTML) ------------------')


def get_user_input():
    markdowns = []
    markdown = input()
    while markdown.lower() != 'convert':
        if markdown.lower() == 'quit':
            return None
        markdowns.append(markdown)
        markdown = input()
    return markdowns


if __name__ == "__main__":
    markdown_to_html()
