

def paragraph(content):
    content = content.replace('\r', '')
    paragraphs = content.split('\n')
    return paragraphs
    