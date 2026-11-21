class TrieNode:
    def __init__(self):
        self.Children = {}
        self.endOfNode = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.Children:
                cur.Children[c] = TrieNode()
            cur = cur.Children[c]
        cur.endOfNode = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.Children:
                return False
            cur = cur.Children[c]
        return cur.endOfNode 

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.Children:
                return False
            cur = cur.Children[c]
        
        return True

        