import spacy
from spacy.pipeline import EntityRuler

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Define the pattern for identifying person names
patterns = [
    {"label": "PERSON", "pattern": [{"POS": "PROPN"}, {"POS": "VERB"}]},
]

# Initialize the entity ruler
ruler = nlp.add_pipe("entity_ruler")

# Add the patterns to the ruler
ruler.add_patterns(patterns)

# Process text
text = "John was born in New York. Mary likes to dance."
doc = nlp(text)

# Print identified entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")