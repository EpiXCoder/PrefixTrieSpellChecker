
from flask import Flask, jsonify, request
from flask_cors import CORS
from spell_checker import Trie, load_system_dictionary, suggest_corrections 
import os

app = Flask(__name__)
CORS(app)


trie = Trie()
dictionary_path = os.path.join(app.root_path, 'words')  
load_system_dictionary(trie, dictionary_path)

@app.route('/check_spelling', methods=['POST'])
def check_spelling():
    data = request.json
    word = data.get('word', '')
    if not word:
        return jsonify({'error': 'No word provided'}), 400
    
    is_correct = trie.search(word.lower())
    suggestions = []
    if not is_correct:
        suggestions = suggest_corrections(trie, word)
    
    return jsonify({'word': word, 'is_correct': is_correct, 'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)

