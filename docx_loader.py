from docx import Document


def load_docx(filename):
    document = Document(filename)

    paragraphs = []

    for paragraph in document.paragraphs:
        paragraphs.append(paragraph.text)

    return "\n".join(paragraphs)