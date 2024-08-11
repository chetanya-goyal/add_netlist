from pathlib import Path
from typing import List, Tuple, Union
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import Chroma
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

class RAGdb:
    """
    A class to create and manage a vector database for the RAG data using ChromaDB.

    Attributes:
        chroma_client (Client): The ChromaDB client used for managing the vector database.
        collection_name (str): The name of the collection used in ChromaDB.
        collection (Collection): The vector database
    """

    def __init__(self, rag_data_dir: Union[str, Path]):
        """Initializes the RAGdb instance with a ChromaDB collection"""
        # error checking
        rag_data_dir = Path(rag_data_dir).resolve()
        if not rag_data_dir.is_dir():
            raise FileNotFoundError(f"could not find RAG data directory {rag_data_dir}")
        # load RAG data
        self.documents = DirectoryLoader(str(rag_data_dir), glob="*.md").load()
        self.doctitles = self._get_doc_titles()
        # create vector db and set collection_metadata to configure the distance similarity metric
        # the default similarity metric is l2 norm
        embeddings_model_name = "sentence-transformers/all-MiniLM-L6-v2"
        embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
        #collection_metadata = {"hnsw:space": "cosine"}
        collection_metadata = {"hnsw:space": "l2"} 
        
        self.titledb = Chroma.from_texts(
            texts=self.doctitles, embedding=embeddings,collection_metadata=collection_metadata
        )
        # self.vectordb = Chroma.from_documents(
        #     documents=self.documents, embedding=embeddings, collection_metadata=collection_metadata
        # )
    
    def _get_doc_titles(self) -> List[str]:
        titles = []
        for doc in self.documents:
            first_line = doc.page_content.split('\n')[0]
            # print(first_line)
            titles.append(first_line)
        return titles
    
    def query(self, query_text: str, k: int = 1) -> list:
        """
        Queries the vector database to find the top-k most similar vectors to the given query text.
        Args:
            query_text (str): The text to query.
            k (int): number of documents to query
        Returns:
            List: The list of at most top-k most similar docs. (always returns a list even if k=1)
                    NOTE: if similarity is below a threshold, it will ignore documents
                    NOTE: if final list is length 0, it will return a list with "None" as the only element
        Raises
            ValueError: less than one document queried (k<1)
        """
        # error checking
        k = int(k)
        if k<1:
            raise ValueError("you must query for at least one document")
        # query the vec db
        #rawdocs = self.vectordb.similarity_search(query=query_text, k=k)
        # rawdocs = self.vectordb.similarity_search_with_score(query=query_text, k=k)
        rawtitles = self.titledb.similarity_search_with_score(query=query_text, k=k)
        
        rawtxt = list()
        print(rawtitles)
        if len(rawtitles) > 0:
            for i, (doc, similarity) in enumerate(rawtitles):
                doctitle = doc.page_content
                for doc_iter in self.documents: 
                    if doc_iter.page_content.split('\n')[0] == doctitle and similarity < 1.4:
                        rawtxt.append(doc_iter.page_content)
                        # print('similarity = ', similarity)
            # print("######")
        if len(rawtxt)==0:
            return [None]
        else:
            return rawtxt

