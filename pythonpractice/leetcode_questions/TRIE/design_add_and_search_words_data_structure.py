# specific custom trie data structure for this leetcode question

# try using dict for children
# try using WordDictionary for children

class TrieNode():
    def __init__(self) -> None:
        self.is_eow = False
        self.children = [None]*26

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def _index_to_char(self, index):
        return chr(index+ord('a'))

    def _char_to_index(self, char):
        return ord(char)-ord('a')

    def addWord(self, word: str) -> None:
        curr = self.root
        for i, char in enumerate(word):
            index = self._char_to_index(char)
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            if i == len(word)-1: # last char
                curr.is_eow = True


    # def search(self, word: str) -> bool:
    #     def dfs(node, i):
    #         if node
    #     return dfs(self.root, 0)

    def print_all_words(self) -> None:
        words_in_trie = []
        self._dfs_find_all_words(self.root, "", words_in_trie)
        print(words_in_trie)

    def _dfs_find_all_words(self, node, word, words_in_trie) -> None:
        if node.is_eow:
            words_in_trie.append(word)
        for i, child in enumerate(node.children):
            if child:
                char = self._index_to_char(i)
                self._dfs_find_all_words(child, word+char, words_in_trie)
        
if __name__ == "__main__":
    word_dict = WordDictionary()
    words = ["bad", "mad", "dad", "daddy", "did"]
    search_words = ["pad", "bad", "mad", "d..", "d.d", ".ad", ".e."] 
                    #False, True, True,   True,  True,  True,  False
    for word in words:
        word_dict.addWord(word)
    word_dict.print_all_words()
    # for word in search_words:
    #     print(word_dict.search(word))

