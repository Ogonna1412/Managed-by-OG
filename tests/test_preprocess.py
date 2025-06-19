import pytest
from rfm_classifier import RFMClassifier

def test_preprocess_basic():
    clf = RFMClassifier()
    assert clf.preprocess_text("Hello, WORLD!") == "hello world"

def test_preprocess_none():
    clf = RFMClassifier()
    assert clf.preprocess_text(None) == ""
