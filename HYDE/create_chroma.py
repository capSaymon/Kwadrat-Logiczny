from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from HYDE.llama_embeddings import LlamaEmbeddings
import openai 
from dotenv import load_dotenv
import os
import shutil

DATA_PATH = r'G:\Kwadrat Logiczny\Kwadrat-Logiczny\HYDE\DATA'
CHROMA_PATH = r'G:\Kwadrat Logiczny\Kwadrat-Logiczny\HYDE\chroma'

def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md", loader_cls=TextLoader)
    documents = loader.load()
    return documents

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[5]
    document.page_content
    document.metadata

    return chunks

def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    llama_embeddings = LlamaEmbeddings(model_path=r"G:\Kwadrat Logiczny\nomic-embed-text-v1.5.Q5_K_M.gguf")

    db = Chroma.from_documents(
        chunks, llama_embeddings, persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
    main()