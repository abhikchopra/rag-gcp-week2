import pdfplumber

def extract_text(pdf_path):
    """
    Extracts full text from a PDF file.
    """
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            page_text = page.extract_text()

            if page_text:
                # add page marker for traceability
                text += f"\n[PAGE {page_num}] \n" + page_text

    return text


def chunk_text(text, chunk_size=300, overlap=50):
    """
    Splits long text into overlapping chunks.
    This helps embeddings capture meaning better.
    """

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap  # overlap prevents loss of context

    return chunks