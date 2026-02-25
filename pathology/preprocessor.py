import re
import spacy

nlp = spacy.load("en_core_web_sm")


def preprocess(text: str) -> str:
    """
    Clean and normalize raw pathology report text.
    - Collapses extra whitespace
    - Normalizes multiple newlines
    - Strips leading/trailing whitespace per line
    """
    # Collapse multiple spaces/tabs into one
    text = re.sub(r'[ \t]+', ' ', text)

    # Normalize multiple newlines into one
    text = re.sub(r'\n{2,}', '\n', text)

    # Strip leading/trailing whitespace from each line
    lines = [line.strip() for line in text.splitlines()]
    text = '\n'.join(lines)

    return text.strip()


def tokenize(text: str) -> spacy.tokens.Doc:
    """
    Use spaCy to tokenize and tag the text.
    Returns a spaCy Doc object for NER downstream.
    """
    return nlp(text)