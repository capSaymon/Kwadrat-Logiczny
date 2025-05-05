import shutil
import os
import sys

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from llama_embeddings import LlamaEmbeddings
from hyde_values import DATA_PATH, CHROMA_PATH


class Run_chroma():
    def __init__(self):
        self.generate_data_store()


    def generate_data_store(self):
        documents = self.load_documents()
        chunks = self.split_text(documents)
        self.save_to_chroma(chunks)


    def load_documents(self):
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

    def save_to_chroma(self, chunks: list[Document]):
        if os.path.exists(CHROMA_PATH):
            shutil.rmtree(CHROMA_PATH)

        llama_embeddings = LlamaEmbeddings()

        db = Chroma.from_documents(chunks, llama_embeddings, persist_directory=CHROMA_PATH)
        db.persist()
        print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")