import json
import chromadb
from sentence_transformers import SentenceTransformer

DB_PATH = "data/processed/chroma"
model = SentenceTransformer("all-MiniLM-L6-v2")


def build_store(chunks):
    """Turn every piece into numbers and save it in the database, 1000 at a time."""
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection("reports", metadata={"hnsw:space": "cosine"})
    batch = 1000
    for start in range(0, len(chunks), batch):
        part = chunks[start:start + batch]
        texts = [c["text"] for c in part]
        collection.add(
            ids=[str(start + i) for i in range(len(part))],
            documents=texts,
            embeddings=model.encode(texts).tolist(),
            metadatas=[{"company": c["company"], "year": c["year"], "page": c["page"]} for c in part],
        )
        print("stored", start + len(part), "of", len(chunks))


def search(question, k=5):
    """Return the k pieces closest in meaning to the question."""
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_collection("reports")
    result = collection.query(query_embeddings=model.encode([question]).tolist(), n_results=k)
    for text, label, distance in zip(result["documents"][0], result["metadatas"][0], result["distances"][0]):
        print(label, round(1 - distance, 2), text[:80].replace("\n", " "))


if __name__ == "__main__":
    with open("data/processed/chunks.json", encoding="utf-8") as f:
        chunks = json.load(f)
    build_store(chunks)
    search("total borrowings")