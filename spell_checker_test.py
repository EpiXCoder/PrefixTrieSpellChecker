import unittest
from spell_checker import Trie, load_system_dictionary, is_word_spelled_correctly, suggest_corrections

class TestSpellChecker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trie = Trie()
        load_system_dictionary(cls.trie, '/usr/share/dict/words')

    def test_word_insertion(self):
        self.trie.insert('testword')
        self.assertTrue(self.trie.search('testword'))

    def test_spell_checking_correct_word(self):
        self.assertTrue(is_word_spelled_correctly(self.trie, 'example'))

    def test_spell_checking_incorrect_word(self):
        self.assertFalse(is_word_spelled_correctly(self.trie, 'exampel'))

    def test_suggestions(self):
        suggestions = suggest_corrections(self.trie, 'exampel')
        self.assertIn('example', suggestions)

if __name__ == '__main__':
    unittest.main()
