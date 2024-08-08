import pandas as pd
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    # Load the 20-newsgroups dataset
    newsgroups = fetch_20newsgroups(subset='all')
    data = newsgroups.data

    return data

newsgroups = load_data()

documents = [newsgroups]

def prepare_data():
    # Compute TF-IDF matrix for documents
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(newsgroups)
    
    return tfidf_matrix, vectorizer


def rank_doc(input_word):
    try:
        tfidf_matrix, vectorizer = prepare_data()

        # Define a query and transform it using the same vectorizer
        query_vec = vectorizer.transform([input_word])

        # Calculate Cosine Similarity between query and each document
        cosine_similarities = cosine_similarity(tfidf_matrix, query_vec).flatten()

        # Rank Documents based on Cosine Similarity
        ranked_indices = np.argsort(cosine_similarities)[::-1]
        ranked_documents = [newsgroups[i] for i in ranked_indices]
        ranked_scores = [cosine_similarities[i] for i in ranked_indices]

        # # Convert results to a DataFrame for better visualization
        results_df = pd.DataFrame({
            'Document': ranked_documents[:5],
            'Score': ranked_scores[:5]
        })

        return results_df
    except Exception as e:
        raise e

def add_document_text(document):
    try:
        documents.append(document.text)
        return "Document added"
    except Exception as e:
        raise e
