words = ["peter", "pumpkin", "pen", "penis","pump"]
search_words = ["pete", "peni", "pen", "penis"]

class TrieNode():
    def __init__(self) -> None:
        self.is_end_of_word = False
        self.children = [None]*26 # 26 characters in english alphabet

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def add_word(self, word):
        parent = self.root
        for i, char in enumerate(word):
            child_index = self._char_to_index(char)
            if parent.children[child_index]:
                if i == len(word)-1:
                    parent.children[child_index].is_end_of_word = True
                else:
                    parent = parent.children[child_index]
            else:
                parent.children[child_index] = TrieNode()
                if i == len(word)-1:
                    parent.children[child_index].is_end_of_word = True
                parent = parent.children[child_index]

    # to get the index of the char in the children array of parent node
    def _char_to_index(self, char):
        return ord(char)-ord("a")

    def _index_to_char(self, index):
        return chr(ord("a")+index)

    def search_word(self, word):
        parent = self.root
        for i, char in enumerate(word):
            child_index = self._char_to_index(char)
            if not parent.children[child_index]:
                return False
            if i == len(word)-1 and parent.children[child_index].is_end_of_word:
                return True
            else:
                parent = parent.children[child_index]
        return False

    def print_all_words(self):
        visited = set()
        words_in_trie = []
        self._dfs_print_all_words(self.root, "", "", visited, words_in_trie)
        return words_in_trie

    def _dfs_print_all_words(self, node, char, word, visited, words_in_trie):
        word += char
        visited.add(node)
        if node.is_end_of_word:
            words_in_trie.append(word)
        # if not node.children: # cannot check all values in list are empty like that
        if all(child is None for child in node.children):
            return
        for i, child in enumerate(node.children):
            if child and child not in visited:
                char = self._index_to_char(i)
                self._dfs_print_all_words(child, char, word, visited, words_in_trie)

    def has_prefix(self, prefix):
        parent = self.root
        for char in prefix:
            char_index = self._char_to_index(char)
            if parent.children[char_index]:
                parent = parent.children[char_index]
            else:
                return False
        return True

    def has_prefix_dfs(self, prefix):
        visited = set()
        return self._dfs_has_prefix(self.root, "", "", visited, prefix)

    # using this only words for small test cases, but run time will be too long if trie is large because we check the entire thing
    def _dfs_has_prefix(self, node, char, word, visited, prefix):
        visited.add(node)
        word += char
        print(word, prefix)
        if word == prefix:
            return True
        if all(child is None for child in node.children):
            return
        for i, child in enumerate(node.children):
            if child and child not in visited:
                char = self._index_to_char(i)
                if self._dfs_has_prefix(child, char, word, visited, prefix):
                    return True

if __name__ == "__main__":
    trie = Trie()
    for word in words:
        trie.add_word(word)
    for word in search_words:
        print(trie.search_word(word))
    print(trie.print_all_words())
    print(trie.has_prefix("pet"))
