# Markdown to html converter by Zeke.

# 1. Read text from file
# 2. Break said text up into sections
#    * header 1/2/3
#    * Paragraph
#    * List
#    * Link
#    * Image
# 3. Generate html for each type.

# ** header **
# A single line which begins with '#', '##', or '###'.

# ** paragraph **
# A section of text not belonging to any other category and surrounded
# by blank lines.

# ** list **
# A sequence of one or more lines beginning with a '*' surrounded by
# blank lines

# ** link || image **
# Annotation to text that can appear in a paragraph.

# Breaks input text into blocks that can then be identified as one of
# the above categories.
def tokenize(text):
    return text.split('\n\n')

def parse(blocks):
    parsed_blocks = []
    for block in blocks:
        # remove leading and trailing whitespace.
        block = block.strip()
        
        assert len(block) != 0, 'empty block in parse'

        pivot = block[0]
        if pivot == '#':
            parsed_blocks.append(parse_header(block))
        elif pivot == '*':
            parsed_blocks.append(parse_list(block))
        else:
            parsed_blocks.append( ('<p>', block) )

    return parsed_blocks

def parse_header(block):
    assert block.count('\n') == 0, 'newline in header block\n->\n{}\n<-'.format(block)

    header_size = 1

    if block.startswith('###'):
        header_size = 3
    elif block.startswith('##'):
        header_size = 2

    return ( '<h{}>'.format(header_size), block[header_size:] )

def parse_list(block):
    list_items = block.split('*')
    # remote empty strings. These happen if there are empty list items
    # or if the first character of the block is a '*'
    list_items = filter(lambda s: len(s) != 0, list_items)
    list_items = [i.strip() for i in list_items]

    return ( '<ul>', list(list_items) )

def render(blocks):
    assert all((lambda t: len(t) == 2)(i) for i in blocks), "malformed input to render"

    result = ""
    for header, body in blocks:
        if header.startswith("<h") or header == '<p>':
            result += header + body + "</{}>".format(header[1:len(header)-1])
        elif header == "<ul>":
            result += '<ul>' + "\n".join(['<li>' + item + '</li>' for item in body]) + '</ul>'
        else:
            assert False, "invalid header type"

    return result

def transform_text(blocks):
    RE_LINK = re.compile(r'''\(\s*(?:(<[^<>]*>)\s*(?:('[^']*'|"[^"]*")\s*)?\))?''', re.DOTALL | re.UNICODE)
    

import fileinput
markdown = ""

for line in fileinput.input():
    markdown += line

print(render(parse(tokenize(markdown))))

