import pytest
from methods import documents, load_data, prepare_data, rank_doc, add_document_text
from main import Document


def test_load_data():
    data = load_data()
    assert data


def test_prepare_data():
    tfidf_matrix, vectorizer = prepare_data()
    assert vectorizer


def test_rank_doc():
    pass


def test_add_document_text():
    dummy_doc = Document(text="Dummy text.")
    add_document_text(dummy_doc)
    assert dummy_doc.text in documents
