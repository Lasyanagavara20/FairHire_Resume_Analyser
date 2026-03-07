import fitz
import docx

def extract_text(file):

    filename = file.filename

    if filename.endswith(".pdf"):
        return extract_pdf(file)

    elif filename.endswith(".docx"):
        return extract_docx(file)

    else:
        return "Unsupported file format"


def extract_pdf(file):

    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text


def extract_docx(file):

    doc = docx.Document(file)
    text = ""

    for para in doc.paragraphs:
        text += para.text

    return text