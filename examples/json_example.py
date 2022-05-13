import json
from pprint import pprint


with open('glossary.json', 'r') as f:
    glossary = json.load(f)

pprint(glossary)
glossary['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['para'] = "new value"

with open('glossary.json', 'w') as f:
    json.dump(glossary, f, indent=2)
