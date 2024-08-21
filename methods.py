import pandas as pd
import numpy as np
import typing as tp
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import scipy
import logging

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


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
current_documents_len = len(newsgroups)

documents = newsgroups
vectorizer = TfidfVectorizer(stop_words="english")


def prepare_data():
    """
    prepare_data computes TF-IDF matrix for documents and returns
    a tfidf_matrix
    """
    # Compute TF-IDF matrix for documents
    try:
        # example of tfidf_matrix
        # array(['and', 'document', 'one',
        # 'second', 'the', 'third','this'], ...)
        tfidf_matrix = vectorizer.fit_transform(documents)

        return tfidf_matrix
    except Exception as e:
        raise e

# prepare initial tfidf_matrix based on 20newsgroup dataset
tfidf_matrix = prepare_data()

def check_for_document_len_updates(documents, current_documents_len):
    '''
    check_for_document_len_updates checks for any document
    additions to the initial 20newsgroup documents dateset
    and returns True if there is new additions, False if not
    '''
    if len(documents) > current_documents_len:
        doc_len_lamda = len(documents) - current_documents_len
        current_documents_len += doc_len_lamda
        return True
    return False

def update_documents_matrix(new_document, tfidf_matrix):
    '''
    update_documents_matrix joins tfidf_matrix with newly
    created matrix based on newly added document
    '''
    new_tfidf_matrix = vectorizer.fit_transform(new_document)

    # Stack matrices horizontally (column wise) using hstack().
    # https://stackoverflow.com/a/63456961/8753568
    updated_tfidf = scipy.sparse.hstack([tfidf_matrix, new_tfidf_matrix])
    
    # update hardcoded tfidf_matrix to latest state
    tfidf_matrix = updated_tfidf

def rank_doc(input_str: str) -> pd.DataFrame:
    """
    rank_doc takes input_word str that is being searched through
    documents and it is ranked with Cosine Similarity score

    method returns data as dataframe
    """
    try:
        if check_for_document_len_updates(documents, current_documents_len):
            logger.info("if entered")
            update_documents_matrix(documents[-1], tfidf_matrix)
        
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
