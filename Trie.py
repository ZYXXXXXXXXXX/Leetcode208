class Trie_node:
    def __init__(self, val):
        self.val = val
        self.is_word = False
        self.child = {}

    def node_insert(self, word):
        if len(word) == 0:
            self.is_word = True
            return

        if word[0] in self.child:
            self.child[word[0]].node_insert(word[1:])
        else:
            self.child[word[0]] = Trie_node(word[0])
            self.child[word[0]].node_insert(word[1:])

    def node_search(self, word):
        if len(word) == 0:
            return False
        if word[0] not in self.child:
            return False
        elif word[0] in self.child and len(word) == 1:
            if self.child[word[0]].is_word:
                return True
            else:
                return False
        else:
            return self.child[word[0]].node_search(word[1:])

    def search_prefix(self, prefix):
        if len(prefix) == 0:
            return True
        if prefix[0] not in self.child:
            return False
        else:
            return self.child[prefix[0]].search_prefix(prefix[1:])


class Trie:
    def __init__(self):
        self.root = Trie_node('')

    def insert(self, word: str):
        self.root.node_insert(word)

    def search(self, word: str):
        return self.root.node_search(word)

    def startsWith(self, prefix: str):
        return self.root.search_prefix(prefix)


# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    obj = Trie()
    obj.insert("sting")
    obj.insert("string")
    print(obj.search("string"))
    print(obj.startsWith("str"))
    print(obj.search("kun"))
