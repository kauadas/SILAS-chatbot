import spacy

nlp = spacy.load("pt_core_news_sm")

text = "Kauã trabalha no Google hoje as 18:00"

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)