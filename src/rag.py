import sys
import chromadb
from sentence_transformers import SentenceTransformer
from src.llm import get_llm

DB_PATH = "data/processed/chroma"
model = SentenceTransformer("all-MiniLM-L6-v2")


def find_pieces(question, k=5):
    """The librarian: find the 5 cards closest in meaning to the question."""
    collection = chromadb.PersistentClient(path=DB_PATH).get_collection("reports")
    result = collection.query(query_embeddings=model.encode([question]).tolist(), n_results=k)
    return list(zip(result["documents"][0], result["metadatas"][0]))


def answer(question):
    """The student: answer only from those cards, and cite them."""
    pieces = find_pieces(question)
    context = ""
    for text, label in pieces:
        context += f"[{label['company']} {label['year']} page {label['page']}]\n{text}\n\n"
    prompt = (
        "Answer the question using ONLY the report pieces below. "
        "After every number, write its source in brackets, like [maruti FY2025 page 175]. "
        "If the pieces do not contain the answer, say: Not found in the reports.\n\n"
        f"Report pieces:\n{context}\nQuestion: {question}"
    )
    client = get_llm()
    response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=prompt)
    return response.text


if __name__ == "__main__":
    question = " ".join(sys.argv[1:])
    print(answer(question))