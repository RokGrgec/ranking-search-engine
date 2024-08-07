import pytest
from methods import newsgroups, load_data, prepare_data, rank_doc, add_document


def test_load_data():
    data = load_data()
    assert data

def test_prepare_data():
    tfidf_matrix, vectorizer = prepare_data(newsgroups)
    assert vectorizer
