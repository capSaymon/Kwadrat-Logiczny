import argparse
import os
import sys
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from llama_embeddings import LlamaEmbeddings

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LLAMA.send_prompt import Prompt

CHROMA_PATH = r'G:\Kwadrat Logiczny\Kwadrat-Logiczny\HYDE\chroma'

PROMPT_TEMPLATE = """
Odpowiedz na pytanie bazując na tych kontekstach:

{context}

---

Odpoweidz bazując na podanych kontekstach tego jedngo zdania: {question}
"""


def main():
    query_text = "A: Zdanie A: Wszystkie samoloty stoją na płycie lotniska. Znajdź reszte zdań."

    llama_embeddings = LlamaEmbeddings(model_path=r"G:\Kwadrat Logiczny\nomic-embed-text-v1.5.Q5_K_M.gguf")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=llama_embeddings)

    results = db.similarity_search_with_relevance_scores(query_text, k=2)
    if len(results) == 0 or results[0][1] > 1:
        print(f"Brak podobnych zdań.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    print("Generuj prompt:\n")
    print(prompt)
    print("\nWysyłanie promptu\n")

    outcome = Prompt(prompt).send()

    print("\nWynik:\n")
    print(outcome)

if __name__ == "__main__":
    main()