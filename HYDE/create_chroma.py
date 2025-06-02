import shutil
import os

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from llama_embeddings import LlamaEmbeddings
from hyde_values import DATA_PATH, CHROMA_PATH

def main():
    loader = DirectoryLoader(DATA_PATH, glob="*.md", loader_cls=lambda path: TextLoader(path, encoding="utf-8"))
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100, length_function=len, add_start_index=True)
    chunks = text_splitter.split_documents(documents)

    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    llama_embeddings = LlamaEmbeddings()
    db = Chroma.from_documents(chunks, llama_embeddings, persist_directory=CHROMA_PATH)
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == '__main__':
    main()