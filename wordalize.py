import spacy

nlp = spacy.load("en_core_web_lg")


def checkSimilarity(a, b):
    doc1 = nlp(a)
    doc2 = nlp(b)
    
    return doc1.similarity(doc2)