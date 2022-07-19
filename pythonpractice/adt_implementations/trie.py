words = ["peter", "pumpkin", "pen", "penis", "pump"]
search_words = ["pete", "peni", "pen", "penis"]

class TrieNode():
    def __init__(self) -> None:
        self.is_end_of_word = False
        self.children = [None]*26 # 26 characters in english alphabet

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()

    def _char_to_index(self, char):
        return ord(char)-ord('a')

    def _index_to_char(self, char_index):
        return chr(char_index+ord('a'))

    def add_word(self, word) -> None:
        curr = self.root
        for i, char in enumerate(word):
            char_index = self._char_to_index(char)
            if not curr.children[char_index]: # this char does not exist
                curr.children[char_index] = TrieNode()
            curr = curr.children[char_index] # shift curr down for next iteration
            if i == len(word)-1:
                curr.is_end_of_word = True

    def search_word(self, word):
        curr = self.root
        for i, char in enumerate(word):
            char_index = self._char_to_index(char)
            if curr.children[char_index]:
                curr = curr.children[char_index]
                if i == len(word)-1 and curr.is_end_of_word:
                    return True
            else:
                return False
        return False

    # basically the same as search_word but no need check for end of word
    # i try to do it in a slightly different way for practice although it can be almost exactly the same as search_word
    def has_prefix(self, prefix) -> bool:
        curr = self.root
        for char in prefix:
            char_index = self._char_to_index(char)
            curr = curr.children[char_index]
            if not curr:
                return False
        return True
            

    def print_all_words(self) -> None:
        words_in_trie = []
        self._dfs_find_all_words(self.root, "", words_in_trie)
        print(words_in_trie)

    def _dfs_find_all_words(self, node, word, words_in_trie) -> None:
        if node.is_end_of_word:
            words_in_trie.append(word)
        for i, child in enumerate(node.children):
            if child:
                char = self._index_to_char(i)
                self._dfs_find_all_words(child, word+char, words_in_trie)




if __name__ == "__main__":
    trie = Trie()
    for word in words:
        trie.add_word(word)
    for word in search_words:
        print(trie.search_word(word))
    trie.print_all_words()
    print(trie.has_prefix("pea"))