from src.conf import P_START, P_END, HEADER_IDENTIFIER, LINK_IDENTIFIER


class MarkdownToHTMLConverter:

    @staticmethod
    def convert_multi_string_markdown(markdowns):
        result = []
        markdowns = markdowns.split('\n')
        n = len(markdowns)
        for idx, markdown in enumerate(markdowns):
            if idx + 1 < n and markdowns[idx] != '' and markdowns[idx + 1] != '':
                output = MarkdownToHTMLConverter.convert(markdown, tags=[P_START, ''])
            elif idx > 0 and markdowns[idx-1] != '' and markdowns[idx] != '':
                output = MarkdownToHTMLConverter.convert(markdown, tags=['', P_END])
            else:
                output = MarkdownToHTMLConverter.convert(markdown)
            result.append(output)
        return result

    @staticmethod
    def convert(markdown, tags=[P_START, P_END]):
        n = len(markdown)
        start = 0
        return MarkdownToHTMLConverter._converter(markdown, start, n,tags)

    @staticmethod
    def _converter(string, start, end, tags=[P_START, P_END]):
        if start >= end:
            return ''
        if string[start] == HEADER_IDENTIFIER:
            return MarkdownToHTMLConverter._header_logic(string, start, end)
        elif string[start] == LINK_IDENTIFIER:
            return MarkdownToHTMLConverter._link_logic(string, start, end)
        else:
            return MarkdownToHTMLConverter._paragraph_logic(string, start, end, tags=tags)


    @staticmethod
    def _header_logic(string, start, end):
        result = []
        temp = []
        while start < end and string[start] == HEADER_IDENTIFIER:
            temp.append(HEADER_IDENTIFIER)
            start += 1
        if start < end and string[start] == ' ':  # logic for header if hear Markdown syntax is followed, else p tag
            cnt = len(temp)
            result.append(f'<h{cnt}>')
            remaining, start = MarkdownToHTMLConverter._until_special_character(string, start + 1, end)
            result.append(remaining)
            return ''.join(result) + MarkdownToHTMLConverter._converter(string, start, end) + f'</h{cnt}>'
        else:  # if header syntax is not correct, it will be paragraph tag
            return MarkdownToHTMLConverter._paragraph_logic(string, start, end, pre=temp, tags=[P_START, P_END])

    @staticmethod
    def _until_special_character(string, start, end):
        result = []
        while start < end and string[start] not in [LINK_IDENTIFIER, HEADER_IDENTIFIER]:
            result.append(string[start])
            start += 1
        return ''.join(result), start

    @staticmethod
    def _paragraph_logic(string, start, end, pre=None, tags=[P_START, P_END]):
        p_start, p_end = tags
        result = [p_start]
        if pre:
            result.append(''.join(pre))
        remaining, start = MarkdownToHTMLConverter._until_special_character(string, start, end)
        result.append(remaining)
        return ''.join(result) + MarkdownToHTMLConverter._converter(string, start, end, tags=tags) + p_end

    @staticmethod
    def _link_logic(string, start, end):
        title = []
        link = []
        while start < end and string[start] != ']':
            title.append(string[start])
            start += 1
        if start < end:
            title.append(string[start])
            start += 1
        else:
            return P_START + ''.join(title) + P_END
        if start < end:
            if string[start] == '(':
                link.append('(')
                start += 1
            else:
                return P_START + ''.join(title) + string[start:] + P_END
        while start < end and string[start] != ')':
            link.append(string[start])
            start += 1
        if start < end:
            link.append(')')
            start += 1
            return '<a href="' + ''.join(link[1:-1]) + '">' + ''.join(
                title[1:-1]) + '</a>' + MarkdownToHTMLConverter._converter(string, start, end, tags=['', ''])
        else:
            return P_START + ''.join(title) + ''.join(link) + P_END
