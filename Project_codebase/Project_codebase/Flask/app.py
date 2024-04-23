from flask import Flask, request, jsonify, render_template
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.metrics import edit_distance

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_query', methods=['POST'])
def process_query():
    data = request.json

    # Validate the request
    if 'query' not in data or 'k' not in data:
        return jsonify({'error': 'Invalid request. Missing "query" or "k" parameter.'}), 400

    query = data['query']
    k = data['k']

    # Spelling correction/suggestion
    corrected_query = correct_spelling(query)

    # Query expansion
    expanded_query = expand_query(corrected_query)

    # Search the dataset for relevant results
    results = search_results(expanded_query, k)

    return jsonify({'results': results, 'corrected_query': corrected_query, 'expanded_query': expanded_query})

def search_results(query, k):
    words = word_tokenize(query)
    results = []
    for word in words:
        synsets = wordnet.synsets(word)
        for synset in synsets:
            for lemma in synset.lemmas():
                results.append({
                    'id': len(results) + 1,
                    'word': lemma.name(),
                    'definition': synset.definition()
                })
                if len(results) >= k:
                    break
            if len(results) >= k:
                break
        if len(results) >= k:
            break
    return results

def correct_spelling(query):
    tokens = word_tokenize(query)
    corrected_tokens = [correct_word(token) for token in tokens]
    return ' '.join(corrected_tokens)

def correct_word(word):
    candidates = wordnet.synsets(word)
    if not candidates:
        return word
    candidate_words = set()
    for candidate in candidates:
        candidate_words.update(candidate.lemma_names())
    return max(candidate_words, key=lambda x: edit_distance(word, x))

def expand_query(query):
    tokens = word_tokenize(query)
    expanded_tokens = [expand_word(token) for token in tokens]
    return ' '.join(expanded_tokens)

def expand_word(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return ' '.join(synonyms)

if __name__ == '__main__':
    app.run(debug=True)
