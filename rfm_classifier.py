import re

class RFMClassifier:
    def __init__(self, stop_words=None):
        self.stop_words = set(stop_words or [])

    def preprocess_text(self, text):
        if text is None:
            return ""
        text = str(text).lower()
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)
        tokens = [t for t in text.split() if t not in self.stop_words]
        return " ".join(tokens)
