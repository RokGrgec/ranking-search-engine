import pandas as pd
import numpy as np
import typing as tp
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data() -> tp.List[str]:
    """
    looad_data loads the 20-newsgroups dataset
    """
    try:
        newsgroups = fetch_20newsgroups(subset="all")
        data = newsgroups.data
        return data
    except Exception as e:
        raise e


newsgroups = load_data()

documents = newsgroups


def prepare_data() -> tp.Tuple:
    """
    prepare_data computes TF-IDF matrix for documents and returns
    a tuple of tfidf_matrix and vectorizer
    """
    # Compute TF-IDF matrix for documents
    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        # example of tfidf_matrix
        # array(['and', 'document', 'one',
        # 'second', 'the', 'third','this'], ...)
        tfidf_matrix = vectorizer.fit_transform(documents)

        return tfidf_matrix, vectorizer
    except Exception as e:
        raise e


def rank_doc(input_str: str) -> pd.DataFrame:
    """
    rank_doc takes input_word str that is being searched through
    documents and it is ranked with Cosine Similarity score

    method returns data as dataframe
    """
    try:
        tfidf_matrix, vectorizer = prepare_data()

        # Define a query and transform it using the same vectorizer
        query_vec = vectorizer.transform([input_str])

        # Calculate Cosine Similarity between query and each document
        cosine_similarities = cosine_similarity(tfidf_matrix, query_vec).flatten()

        # Rank Documents based on Cosine Similarity
        ranked_indices = np.argsort(cosine_similarities)[::-1]
        ranked_docs = [documents[i] for i in ranked_indices]
        ranked_scores = [cosine_similarities[i] for i in ranked_indices]

        # Convert results to a DataFrame for better visualization
        results_df = pd.DataFrame(
            {"Document": ranked_docs[:5], "Score": ranked_scores[:5]}
        )

        return results_df
    except Exception as e:
        return {"message": e}


def add_document_text(document) -> dict:
    """
    add_document_text add_document_text takes str as input param
    and adds that str to the list of documents
    """
    # Adds document as str to the list of documents
    try:
        documents.append(document.text)
        return {"message": "Document added"}
    except Exception as e:
        return {"message": e}
