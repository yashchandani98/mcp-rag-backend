from app.rag_store import DOCUMENTS
from app.rag_store import embed, index
from app.docs import DOCS
from app.llm_client import generate_answer

class Tools:
    docs = DOCS

    def search_docs(self, query: str, top_k: int = 2):
        # results = [
        #     {"id": k, "content": v}
        #
        #     for k,v in self.docs.items()
        #
        #     if(query.lower() in k.lower() or query.lower() in v.lower())
        # ]

        query_embedding = embed([query])

        distances, indices = index.search(query_embedding, top_k)

        results = []

        for indx in indices[0]:
            results.append({
                "content": DOCUMENTS[indx],
            })

        return results


    def get_doc(self, doc_id: str):
        return self.docs.get(doc_id, "Document not found")

    def answer_with_context(self, query: str, top_k: int = 2):
        # ✅ Retrieval ONLY via rag_store
        docs = embed(query, top_k)

        context = "\n".join(doc["content"] for doc in docs)

        prompt = f"""
    Answer the question using ONLY the context below.
    If the answer is not present, say "I don't know".

    Context:
    {context}

    Question:
    {query}
    """

        answer = generate_answer(prompt)

        return {
            "answer": answer,
            "context_used": docs
        }