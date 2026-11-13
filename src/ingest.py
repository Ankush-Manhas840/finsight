from pathlib import Path
from pypdf import PdfReader


def load_pdfs(raw_dir):
    """Return a list of pages. Each page is a dictionary with its text and where it came from."""
    pages = []
    for pdf_path in sorted(Path(raw_dir).glob("*.pdf")):
        company, year = pdf_path.stem.split("_")
        reader = PdfReader(pdf_path)
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            if text.strip():
                pages.append({"text": text, "company": company, "year": year, "page": page_number})
    return pages


def chunk(pages, chunk_size=800, chunk_overlap=100):
    """Cut every page into pieces of about chunk_size characters that overlap a little."""
    chunks = []
    step = chunk_size - chunk_overlap
    for page in pages:
        text = page["text"]
        for start in range(0, len(text), step):
            piece = text[start:start + chunk_size]
            chunks.append({**page, "text": piece})
    return chunks


if __name__ == "__main__":
    import json
    pages = load_pdfs("data/raw")
    chunks = chunk(pages)
    with open("data/processed/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f)
    print("saved", len(chunks), "chunks")