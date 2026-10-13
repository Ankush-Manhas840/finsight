"""Load annual-report PDFs and split them into chunks with {company, year, page} metadata."""


def load_pdfs(raw_dir):
    """Return a list of documents, one per page, with metadata."""
    # TODO (Nov 10): PyPDFLoader first. Nov 22: switch to Docling so tables survive.
    raise NotImplementedError


def chunk(documents):
    """Split documents into chunks. Nov 23: keep each table whole with its heading."""
    # TODO (Nov 10)
    raise NotImplementedError
